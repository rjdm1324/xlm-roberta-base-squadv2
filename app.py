from transformers import AutoTokenizer, pipeline
from flask import Flask, request, jsonify, render_template
from queue import Queue, Empty
from threading import Thread
import time

app = Flask(__name__)

print("model loading...")

# Model loading

tokenizer = AutoTokenizer.from_pretrained("seongju/squadv2-xlm-roberta-base")

question_answer = pipeline(
    "question-answering",
    model="seongju/squadv2-xlm-roberta-base",
   tokenizer=tokenizer
)

requests_queue = Queue()    # request queue.
BATCH_SIZE = 1              # max request size.
CHECK_INTERVAL = 0.1

print("complete model loading")


def handle_requests_by_batch():
    while True:
        request_batch = []

        while not (len(request_batch) >= BATCH_SIZE):
            try:
                request_batch.append(requests_queue.get(timeout=CHECK_INTERVAL))
            except Empty:
                continue

            for requests in request_batch:
                try:
                    requests["output"] = make_answer(requests['input'])

                except Exception as e:
                    requests["output"] = e


handler = Thread(target=handle_requests_by_batch).start()


def make_answer(input):
    try:
        result = question_answer(question=input['question'], context=input['context'])
        return result

    except Exception as e:
        print('Error occur in script generating!', e)
        return jsonify({'error': e}), 500


@app.route('/generate', methods=['POST'])
def generate():
    if requests_queue.qsize() > BATCH_SIZE:
        return jsonify({'Error': 'Too Many Requests'}), 429
    try:
        args = []
        sentence = request.form['question']
        sentence2 = request.form['context']
        args.append(sentence)
        args.append(sentence2)
    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 500

    req = {'input': {'question': args[0],'context':args[1]}}
    requests_queue.put(req)
    while 'output' not in req:
        time.sleep(CHECK_INTERVAL)
    return req['output']


@app.route('/queue_clear')
def queue_clear():
    while not requests_queue.empty():
        requests_queue.get()

    return "Clear", 200


@app.route('/healthz', methods=["GET"])
def health_check():
    return "Health", 200


@app.route('/')
def main():
    return render_template('main.html'), 200


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')