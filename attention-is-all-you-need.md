# Attention is all you need

## Initial Thoughts (Abstract)
* Attention is all you need has no recurrence. Models proposed in this paper are transformers which are doing especially well with machine translation. The other method is to use bidirectional LSTMs.
* "sequence transduction" are sequence to sequence models e.g. translation. 
* Current models are based on RNN/CNN with an encoder and a decoder. The encoder & decoder are connected through an attention mechanism. 
* This paper did not develop attention, they got rid of everything other than attention. 
* http://jalammar.github.io/illustrated-transformer/
* For English to French attention trained for 3.5 days, WaveNet was much longer. RNN have specific properties which make training slower. 

## Introduction 

* Language model: way of guessing what word comes next. 
* Encoder-decoder: Encoder (recurrent model) takes input string and decoder gives output based on information and weights from the encoder. 
* Recurrent models: Compute the words before to compute the current word. Things must be in order which makes the whole batch harder to parallelise since need to do word n-2 before word n. 
* Memory constraints: RNN requires more threads and using a big batch size doesn't make a difference in performance.    
* The fundamental sequential computation problem is just an inherent quality of the system. I don't know the word you say till you say it. 
* Attention allows to upweight and downweight things in the sequence irrelevant of how far back in the past they were. 
* Transformer also known as "Fully Attentive Network", no recurrence so no sequential dependencies. 
* Good transformer explanation: http://nlp.seas.harvard.edu/2018/04/03/attention.html

## Background

* Coreference resolution: if the pronoun and subject are further apart it will take more time to say they are related. 
* Self-attention: should up-weight parts of a sentence more relevant to the task at hand and down-weight the irrelevant areas. E.g. in reading comprehension look for the answer. 
* End-to-end memory networks: still recurrence (passing hidden weight to specific items) but instead of happening at embedding layer, it's happening at attention layer? 
* Tranformer: first transduction model relying entirely on self-attention.

## Model architecture

### Encoder 
* Modelling words -> vector
* 6 segments
* Each segment has the multi head attention
* Each segment has a feed forward neural network
* Residual connection around each of the 2 sub layers - feed back in the untransformed version as well as the multi-head attention. Then take the normalization of both. 

### Decoder
* vector -> first ouput, second output, third output... 
* 6 segments
* Each segment has the multi head attention.
* Each segment has the feed forward neural network.
* Each segment also has the masked multi-head attention. This takes in just the output embeddings. Output of this is combined with the output of the encoder. 
* Modify self-attention sub-layer in decoder to prevent leaks from subsequent positions (can't look at the words being guessed). This is known as MASKING hence masked multi head attention. 
* Shifting right means can't look at the current position word in output embeddings. 

### Attention

* Refer to jalllamar illustrated transformer blog.
* Function mapping a query (vector) and a set of key-value pairs (vector) to an output. 
* Query = vector projections from trained matrix, dim(matrix) = 64
* Key = vector projection from same trained matrix
* Value = from another trained matrix (length of embedding)
* Output computed as weighted sum of values. 
* Weight computed by a compatibility function of the query with the corresponding key. 
* Scaled dot product attention: query . key. 
* Softmax normalises and sums probabilities to 1.
* Multiply softmax weight by value to drown out irrelevant words and keep the important ones. 
* Sum up the weight values.

### Multi-head attention
* Linear units are 3-D (tensors).
* Scaled dot product attention is 2-D (vector) and h is the number of dimensions.
* Concat converts vector into scalar.
* Allows to look at sequence simultaneously
* Dot product gets large - for large values of d<sub>k</sub>, very small gradients hence it is normalised by division. 
* DECODER ATTENTION LAYERS: Queries are trained from the previous decoder layer (i.e. output) whereas keys and values are trained from the encoder output.
* ENCODER ATTENTION LAYERS: These use self-attention everything comes from previous encoder layer. 



* Auto regressive: consumes previously generated symbol. Depends on "thought vector" + previous word. 
* Input embeddings: semantics? 
* Output embeddings: vocabulary of the output then produce probabilities based off all words.  
* Stacked self attention: 
* Multi-head attention: 