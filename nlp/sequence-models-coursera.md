# Sequence Models for Time Series and NLP

Sequences are data points that are meaningfully ordered. Observations at earlier time points need to provide information about future points. We can take a slice of observation to make a prediction about future sequences.

### Examples of sequences:
* Movies and videos are sequences of images
* Predicting the next X, however there are many ways of doing this.

> How are images and sequences similar? LOCALITY 

### Types of sequences:
* One-to-sequence: image captioning
* Sequence-to-one: smart reply on gmail
* Sequence-to-sequence: translation

### Sequences to inputs

> What's a good size for our sliding window? 

Autocorrelation graphs can reveal dependencies (how much lag is there in the domain?). Sometimes dependencies are known.

### Model.py walkthrough

* The TIMESERIES_COL variable is the key to retrieve from features dictionary. 
* Create_time_series generates some random frequencies, amplitudes and noise to return 50 observations for random sine function.
* The train_and_evaluate function defines a custom estimator using the sequence regressor function. 
* Sequence regressor specifies which model function to retrieve and also compares against a benchmark. 
* All model functions accept features, mode and params. 

### Different types of models

#### Linear Model

The linear model uses tf.layers.dense without an activation function (no neural network) since the model is a linear combination of inputs. 

> Think about the relationship between what models try to capture and the aspects of the real world. Don't fit an irrelevant model. Think about underlying relationship. For example regularisation used to penalise model weights. 

> What if recency is important? Constrain the weights for better performance using exponential smoothing. Autoregressive ARMA models can be used to find relationships in moving averages. ARMA is a special case of linear models. 

#### Deep/Artificial Neural Network (DNN/ANN)

Using the sliding window, it is possible to model non-linear relationships by passing data into a DNN. DNN simply uses a non-linear combination of inputs. The solution involves adding 2 hidden layers:
    * First one maps to 10 nodes
    * Second one maps to 3 nodes

```
h1 = tf.layers.dense(X, 10, activation=tf.nn.relu)
h2 = tf.layers.dense(h1, 3, activation=tf.nn.relu)
```

#### Convolutional Neural Network (CNN)

Locality plays a role in both image recognition and sequence modelling. 

Steps in applying a convolution:
1. Flatten the input sequence.
2. Use conv1d to apply a number of filters to the sequence.
3. Use max_pooling1d to add some spatial invariance and downscaling.
4. Flatten the resulting output into a sequence.
5. Send it through a fully connected layer with the appropriate output node.

> Why doesn't CNN do much better than DNN?
The variable length problem. We can solve this using padding or bagging. Padding involves adding extra data to smaller length sequences or reducing sequences to the size of the smallest sequence. Bagging involves taking an average for each measured characteristic. Called 'bag of words' in natural language model. However, bagging disregards order. 
