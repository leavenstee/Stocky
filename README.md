![Stocky Logo](/stocky_banner.png)
#### Developed by Steven Lee
#### Supervised by Dr. Martin Allen at University of Wisconsin - La Crosse

Prefix
======

My project started with my personal idea to apply machine learning
topics to the stock market to create a stable income. The origins of
this topic came from my own personal losses in stock trading. I was
dealing with very minimal amounts of money compared to major trading
firms that have large quantities of money moving every day. The basis of
the project was going to be a set capital investment running through a
machine learning method and having it generate a minimum wage income. I
began thinking of ways to approach this and then met with Professor
Allen at University of Wisconsin La Crosse to try and come up with the
best way to develop a solution.

Intro
=====

When first starting this project I gathered information to try to define
the problem. I purchased the book Python for Finance: Analyze Big
Financial Data by Yves Hilpisch. This book was extremely valuable in
exposing me to many resources to use in addressing a solution. After
having decided I was going to write this project with Python, I
discovered libraries that will help me identify methods for collecting
data. I chose to use the Yahoo Finance API which allowed me to pull in
data from over a range of dates. I was then able to create a list of
daily closing prices of a selection of stocks. The stock I initially
tested was Chipotle Mexican Grill (CMG). I selected CMG because its
historical price trend exhibited significant growth over an extended
period of time. CMG’s stock price history indicated that if I had
invested in CMG on November 23, 2003 at \$23 a share, the valuation
would have increased to over one million dollars. This raised the
question: could I possibly have seen this increase coming when making an
initial investment?

Averaging Data
==============

I started by trying to categorize the stock valuation historical data,
taking the complete data set and dividing it into five categories. These
categories were Major Loss, Loss, Flat, Gain, Major Gain. To categorize
the data, I averaged every gain and every loss. If it was above our
upper average then it would be considered a Major Gain. Then I applied
the same process to my losses. This categorizing data was helpful but
also problematic because this is a corrupted data set with the risk of
major dips.

Tensorflow and LSTM
===================

To develop a plan of attack I looked into possible current machine
learning techniques. I had some knowledge of linear regression, but
discover quickly that I needed to learn more. By searching the Internet
I was able to find Tensorflow which is an open source software library
for numerical computation using data flow graphs. While this approach
seemed to fit, I experienced a steep learning curve to jump into this
massive library of information. I searched for tutorials and found one
that would provided a great introduction to the use of of Tensorflow in
the analysis of financial data. I determined that a neural network would
allow me to develop the predictive model that I sought. The type of
neural network I decided to use is called a LSTM (Long Short Term
Memory) and is a recurrent neural network (RNN) architecture (an
artificial neural network). Like most RNNs, a LSTM network is universal
in the sense that given enough network units it can compute anything a
conventional computer can compute, provided it has the proper weight
matrix, which may be viewed as its program.

Stocky
======

Stocky is my application of developed as part of this study. I am taking
the technologies from previous sections along with APIs such as Yahoo
Finance and merge them to create a predictive model. From the previous
section, I am taking the LSTM provided by Tensorflow and letting it
parse through stock data from date to date. When the data is done
processing a graph is provided with the predicted model based on
normalized values. These normalized values give me a predicted curve for
the year I am wishing to evaluate. Going into detail from the steps
above I am linking multiple libraries and APIs. I am including the
Tensorflow, Math Libraries, Yahoo Finance, and other minor libraries.
Comments in the code on the following pages demonstrate how the software
works.

``` {.python language="Python"}
from yahoo_finance import Share
from pprint import pprint
import json
import time
import numpy as np
import pylab as pl
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm, time
import datetime as dt

# My next step is using the Yahoo Finance API to pull in stock data 
# from 2013 to 2016.
# This will be our data to learn on. In this time some formatting is done so 
# we are  able to compare to actual data.

rearray = []
text = 'AAPL'
processed_text = text.upper()
stock = Share(processed_text)
today = dt.datetime.today().strftime("%Y-%m-%d")
for value in stock.get_historical('2013-06-12', '2016-12-30'):
        rearray.insert(0,str(value['Close']))
count = 0
f3 = open('aapl1.csv', 'w')
f4 = open('aapl.csv', 'w')
for i in rearray:
    if (count < len(rearray)-365):
        f3.write(i+"\n")
    f4.write(i+"\n")
    count = count + 1
    
# Now I was able to take the data that is stored in the CSV to be learned on.

X_train, y_train, X_test, y_test = lstm.load_data('aapl.csv', 50, True, today)

# Next was to implement features of the LSTM. I was taking in one 
# input dimension and the out putting 50 dimensions. This can be 
# seen as an over kill since I only need one dimension but to preserve 
# the randomness. Now I was also able to begin learning on the data set.

model = Sequential()
model.add(LSTM(
    input_dim=1,
    output_dim=50,
    return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(
    100,
    return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(
    output_dim=1))
model.add(Activation('linear'))
start = time.time()
model.compile(loss='mse', optimizer='rmsprop')

# The training the model is used with the it function from the LSTM.
# Fitting to the the past data we have will allow us to predict using 
# previous trials to see how close we could be on future stock data.

model.fit(
    X_train,
    y_train,
    batch_size=512,
    nb_epoch=1,
    validation_split=0.05)

# The last step is plotting and calculating the base risk analysis. 
# If the risk is too high it will not invest and then hold money 
# into predictions are looking more positive.

predictions = lstm.predict_sequences_multiple(model, X_test, 50, 30)
lstm.plot_results_multiple(predictions, y_test, 50)
```

Simulation
==========

The goal of my simulation was to have my Stocky application working
slightly better than random. My first thoughts was to research common
random acts in stock trading. I came up with three methods that gave me
so reasonable random results. First, I implemented 3 Sided Dice Roll
Daily. This method would be a random number one through three that would
make a decision on that day. If it hits one, it would buy as many shares
as possible. If it hits a 2 it would sell has many shares that I could
sell. if it hit three it would hold the current shares. My next method
was similar but was applied weekly vs daily with a 3 sided dice. My last
method was to buy every Monday and sell Every Thursday. This does what
the title says, buying the maximum amount of shares then liquidate on
Thursdays. These random methods would then run against Stocky and would
compare results. For Stocky the method would call for it to learn on 3
years. I chose three years because some data could be learned on but
would in reality not be corresponding to learning data. For Stocky, it
is simulating in a single line prediction over just the year 2016. The
starting capital will be \$10,000 dollars. In the end assets will be
based off current capital and also how many shares are held at the
current price point.

Results
=======

to 1.0 & Stocky Nueral Net & 3 Dice Roll Daily & 3 Dice Roll Weekly &
Buy Monday, Sell Thursday\
Amazon.com Inc. (AMZN) & \$11,238.39 & \$11,251.02 & \$9,4783.40 &
\$10,363.23\
Chipotle Mexican Grill Inc. (CMG) & \$10,000.00 & \$10,228.69 &
\$14,363.85 & \$653.77\
Apple Inc. (AAPL) & \$10,000.00 & \$9,990.33 & \$2,783.72 & \$2,023.60\

The results in the table above were incredibly positive. The way the
code is evaluated is it takes the prediction from the graphs below and
creates a risk analysis. In the first simulation with AMZN the risk was
enough that it was willing to invest in the 2016 fiscal year and ended
up being right by making a sum of money. The following two simulations
(CMG) and (AAPL) did not have as positive of a prediction as shown in
the graphs. So Stocky evaluated that as too risky to invest so it held
out the \$10,000. From the table it did pay off in some cases versus the
random but in others did not invest as correctly. My goal from this test
is to not lose money which out of the handful of simulations I ran I
never lost a cent!

![Apple Inc.]

![Amazon.com Inc.]

![Chipotle Mexican Grill Inc.]

Future Application
==================

The results I had obtained were extremely positive and unexpected. When
I embarked on this journey I thought I would learn a little about
machine learning and its applications. I was able to claim a small
victory in this project, realizing the power of this model and realizing
that there are many applications I will be able to take away from this.
My next step will be to put this into a GUI (Graphical User Interface).
After the GUI is created I would like to implement a random stock
picking method to recommend stocks that would be found as a positive
increase. Lastly I would like to have multiple models to be able to
reassure the predictions of my model. By this I plan on running my
machine somewhere between 10 and 20 times and average out the
predictions. Since these models have a bit of randomness reassuring my
predictions would be a great future application.

<span>9</span> Hilpisch, Yves. Python for Finance: Analyze Big Financial
Data. Beijing: O’Reilly, 2015. Print.

Welcome to Python.org. (2017). Python.org. Retrieved 5 May 2017, from
https://www.python.org/

TensorFlow. (2017). TensorFlow. Retrieved 5 May 2017, from
https://www.tensorflow.org/

llSourcell/How-to-Predict-Stock-Prices-Easily-Demo. (2017). GitHub.
Retrieved 5 May 2017, from
https://github.com/llSourcell/How-to-Predict-Stock-Prices-Easily-Demo
