# Sequence Models for Time Series and NLP

## Working with sequences

Sequences are data points that are meaningfully ordered. Observations at earlier time points need to provide information about future points. We can take a slice of observation to make a prediction about future sequences.

### Examples of sequences:
* Movies and videos are sequences of images
* Predicting the next X, however there are many ways of doing this.

> How are images and sequences similar? 

### Types of sequences:
* One-to-sequence: image captioning
* Sequence-to-one: smart reply on gmail
* Sequence-to-sequence: translation

### Sequences to inputs

> What's a good size for our sliding window? 

Autocorrelation graphs can reveal dependencies (how much lag is there in the domain?). Sometimes dependencies are known.
