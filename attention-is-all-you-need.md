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