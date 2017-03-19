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


f = open('stockData.txt', 'w')
f2 = open('stockChange.csv','w')
f3 = open('aapl.csv', 'w')


def predict():
    #Step 1 Load Data
    X_train, y_train, X_test, y_test = lstm.load_data('aapl.csv', 50, True)

    #Step 2 Build Model
    model = Sequential()

    model.add(LSTM(
        input_dim=1,
        output_dim=2,
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
    predictions = lstm.predict_sequences_multiple(model, X_test, 50, 50)
    lstm.plot_results_multiple(predictions, y_test, 50)

def printStocks(d,p,s):
    global f
    global f2
    shares = 0
    prev = 35 # For CMG!!
    pos = []
    neg = []
    flatPos = []
    flatNeg = []
    f.write("\n==========================================\n")
    f.write(s + "\n")
    f.write("==========================================\n")
    for x in range(0, len(d)):
        money = float(p[x])
        temp = money - float(prev)
        perc = 0
        if temp > 0:
            perc = (money / float(prev))*100 - 100
            pos.append(perc)
        else:
            perc = 100 - (float(prev) / money)*100
            neg.append(perc)
        # Pattern Check
        prev = money
    pl.plot(range(0, len(pos)),pos,'r')
    pl.plot(range(0, len(neg)),neg,'b')
    posAvg = sum(pos)/len(pos)
    negAvg = sum(neg)/len(neg)
    posAvgHalf = posAvg/2
    negAvgHalf = negAvg/2
    f.write("\nPOS AVG : " + str(posAvg))
    f.write("\nNEG AVG : " + str(negAvg))
    f.write("\n");
    for x in range(0, len(d)):

        money = float(p[x])
        temp = money - float(prev)
        perc = 0
        if temp > 0:
            perc = (money / float(prev))*100 - 100
            pos.append(perc)
        else:
            perc = 100 - (float(prev) / money)*100
            neg.append(perc)
        prev = money
        f.write(str(d[x])+ " | " + str(money) + " | " + str(perc))
        f2.write(str(perc)+"\n")

        if perc > posAvgHalf:
            flatPos.append(perc)
            f.write("==== POSSIBLE SELL, GOOD GAIN ====")
            if perc > posAvg:
                f.write("==== SELL JACKPOT GAIN ====")
        if perc < negAvgHalf:
            flatNeg.append(perc)
            f.write("==== POSSIBLE BUY, GOOD LOSS ====")
            if perc < negAvg:
                f.write("==== BUY JACKPOT DROP ====")
        f.write("\n");
    #pl.plot(range(0, len(flatPos)),flatPos,'g')
    #pl.plot(range(0, len(flatNeg)),flatNeg,'g')



    # Evaluate
def evalStocks(i):
    global f3
    dates = []
    values = []
    count = 0
    processed_text = i.upper()
    stock = Share(processed_text)
    sName = stock.get_name()
    for value in stock.get_historical('2006-06-12', '2017-03-15'):
        if count == 1:
            #print value['Date'] + " | " + value['Close'] + " \n"
            dates.insert(0, value['Date'])
            values.insert(0, float(value['Close']))
            f3.write(str(value['Close'])+"\n")
            count = 0
        count = count + 1
    printStocks(dates,values,sName)
    #pl.show()

def getStocks():
    text = ['cmg']

    for i in text:
        print "STARTED " + i + " WAITING....."
        evalStocks(i)
        print "COMPLETED " + i + " WAITING....."
        time.sleep(1)
    print "DONE Predicting now ->->->->->->->->->"


if __name__ == "__main__":
    print "Cool"
    getStocks()
    predict()
    print "COMPLETED"

# Get Data In Dictonary Print Stuff


# Buy

# Sell
