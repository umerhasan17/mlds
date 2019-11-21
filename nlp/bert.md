# Pre-training of Deep Bidirectional Transformers for Language Understanding

## Initial Thoughts - Abstract
* Bidirectional + transformers i.e. LSTMs
* Language representation models - more syntactic in nature?
* Transfer learning - using 1 problem solution to help solve another one. BERT can "create state-of-the-art models for a wide range of tasks, such as question answering and language inference, WITHOUT substantial task-specific architecture modifications." 
* SQuAD answers middle school questions

## Introduction

### Logical inference: 

Input: Roger has 5 cats.
Does he have dogs? -> I don't know
How many cats does he have? -> 5 / who's He?

### Other types of tests:
* Paraphrasing: Equival sentence same meaning
* SQuAD: Answer questions
* Cloze Test: Fill in the blanks
* GLUE: meta analysis across a number of tasks
* BLUE: not best metric as good score doesn't imply human readable. 

### Differences to other models
* Peters et al. looks forward and back independently unlike BERT. 
* More general (same general architecture leads to less time spent).
* Creates more all encompassing solution than previous models. 
* Elmo is using bidirectional LSTMs with attention whereas BERT uses bidirectional transformer? 
* Fine-tuning approaches try to use transfer learning to update the model for the specific task.
* Basically unlimited data available for unsupervised pre-training. However, supervised tasks effective with large datasets. Therefore, transfer learning from supervised learning is possible. The takeaway is that this general approach will work on supervised tasks as well. 
* Indepth comparisong to OpenAI GPT in later section because that uses the same transformer model whereas ELMO uses bidirectional LSTMs. STILL WHAT'S THE DIFFERENCE? OpenAI is not bidirectional (uses constrained self-attention).
* BERT is similar to how speech production works but not perception because in production we know what words will come after. 

## BERT

* BERT can move between tasks very quickly. 
* BERT is a statistical model for word to come next compared to Attention paper which is a sequence to sequence model. BERT only uses the encoder. 

### Architecture
* Multi layer BTE based on original implementation in Attention is all you need. But only for the encoder not the decoder. 
* Parameters: L = encoder units, H = embedding length, A = attention heads (simultaneously learning, trained independently)
* GPT only looks in the past, BERT looks in past + future. 
* L = number of blocks stacked.
* H = size of input embedding + hidden size.
* A = self-attention heads.

### Input Representation
* Can take 2 inputs and transform into 1 input sequence. Constructed by summing the corresponding token, segment and position embeddings. 
* Using learned position embeddings with 'supported sequence lengths' up to 512 tokens. 
* The first word (token of every sentnece) is a label which tells you the class of the sentence. 
* There are special \[SEP\] tokens to split sentences. 

### Pre-training
