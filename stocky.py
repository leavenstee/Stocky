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

# Step 0 Pick Stock and Pull Data
rearray = []
text = 'amzn'
processed_text = text.upper()
stock = Share(processed_text)
today = dt.datetime.today().strftime("%Y-%m-%d")
for value in stock.get_historical('2010-06-12', '2016-12-30'):
        rearray.insert(0,str(value['Close']))
count = 0
f3 = open('aapl1.csv', 'w')
f4 = open('aapl.csv', 'w')
for i in rearray:
    if (count < len(rearray)-365):
        f3.write(i+"\n")
    f4.write(i+"\n")
    count = count + 1






#Step 1 Load Data
X_train, y_train, X_test, y_test = lstm.load_data('aapl.csv', 50, True, today)

#Step 2 Build Model
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
print 'compilation time : ', time.time() - start

#Step 3 Train the model
model.fit(
    X_train,
    y_train,
    batch_size=512,
    nb_epoch=1,
    validation_split=0.05)

#Step 4 - Plot the predictions!
predictions = lstm.predict_sequences_multiple(model, X_test, 50, 75)
lstm.plot_results_multiple(predictions, y_test, 50)
