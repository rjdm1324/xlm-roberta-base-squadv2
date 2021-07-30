# Title
QA service
---
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/rjdm1324/xlm-roberta-base-squadv2)
## Overview
---
- github : [github](https://github.com/rjdm1324/xlm-roberta-base-squadv2)
- huggingface : [huggingface](https://huggingface.co/seongju/squadv2-xlm-roberta-base)
- workspace : [workspace](https://ainize.ai/workspace/create?imageId=hnj95592adzr02xPTqss&git=https://github.com/rjdm1324/xlm-roberta-base-squadv2-workspace)

## How to make
----
1. Prepare a squad v2.0 dataset.
2. The xlm-roberta-base model was fine-tuned with squad 2.0.

## Usage
---
### how to run a Demo


endpoint : [ainize](https://main-xlm-roberta-base-squadv2-rjdm1324.endpoint.ainize.ai/)
- QA service
1. Fill the context box.
2. Fill the question box you want to find in context
3. Click submit button
- Example
1. Select the context example you want.
2. Select one of the three questions.
3. Click submit button
- Load button
1. You can import the txt file of the local by clicking load button.
2. Fill the question box you want to find in context
3. Click submit button
- Clear button
1. The question box and the context box are cleared.


## With cli
---
### Post Parameter


```
context = "context"
question = "question"
```

### input format
```
{
   "context" : "string"
   "question" : "string"
}
```
### output format

```
{
    "answer": "string",
    "end": number,
    "score": number,
    "start": number
}
```

### API Prediction Test

Using curl on the terminal:

```
$ curl -L -X POST 'https://main-xlm-roberta-base-squadv2-rjdm1324.endpoint.ainize.ai/generate' -F 'context="It involved the vast majority of the world'\''s countries—including all of the great powers—forming two opposing military alliances: the Allies and the Axis powers. In a total war directly involving more than 100 million personnel from more than 30 countries, the major participants threw their entire economic, industrial, and scientific capabilities behind the war effort, blurring the distinction between civilian and military resources."' -F 'question="How many people in total fought in World War II?"'

{
    "answer":"more than 100 million",
    "end":217,
    "score":0.40043753385543823,
    "start":196
}

```

### Healthy Check
Using curl on the terminal:

```
$ curl -L -X GET 'https://main-xlm-roberta-base-squadv2-rjdm1324.endpoint.ainize.ai/healthz'

{
  Health
}
```

## Acknowledgements
---
* [dataset](https://rajpurkar.github.io/SQuAD-explorer/)
* [code(fine-tunning dataset)](https://huggingface.co/transformers/custom_datasets.html)
* [code(model)](https://huggingface.co/transformers/model_doc/roberta.html#robertaforquestionanswering)
* [model](https://huggingface.co/xlm-roberta-base)
