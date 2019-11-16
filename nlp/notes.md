# Methods of Text Classification
* Bag of words
* Neural network with word2vec embeddings
* First text 

## Neural Network with Word2Vec
 * Bag of words uses 1 hot encoding for every single word in input (sparse 1 hot encoded vector).
 * Neural networks have a dense representation (using word2vec embeddings).
 * Can then take sum of word2vec vectors to provide a satisfactory text descriptor (baseline descriptor)
 * Instead, do a neural network over embeddings. Furthermore, we can analyse n-grams with a sliding window. 
 * 1-D convolutions are when the window is slided only in one direction, usually this is time (one word after the next)
 * However, we can use maximum pooling over time to look for a specific activation at any point in time. 

### Word2Vec
* Words are assigned to a vector.
* Can therefore do lots of mathematical operations and analysis on words.
* Words that have a similar context tend to have collinear vectors.
* Similar words are similar in terms of cosine distance (similar to dot product).