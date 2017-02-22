from yahoo_finance import Share
from pprint import pprint
import json
import time
import numpy as np
import pylab as pl


f = open('stockData.txt', 'w')

def printStocks(d,p,s):
    global f
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
    pl.plot(range(0, len(flatPos)),flatPos,'g')
    pl.plot(range(0, len(flatNeg)),flatNeg,'o')



    # Evaluate
def evalStocks(i):
    dates = []
    values = []
    count = 0
    processed_text = i.upper()
    stock = Share(processed_text)
    sName = stock.get_name()
    for value in stock.get_historical('2006-01-01', '2016-12-01'):
        if count == 7:
            #print value['Date'] + " | " + value['Close'] + " \n"
            dates.insert(0, value['Date'])
            values.insert(0, float(value['Close']))
            count = 0
        count = count + 1
    printStocks(dates,values,sName)
    pl.show()

def getStocks():
    text = ['GE']

    for i in text:
        print "STARTED " + i + " WAITING....."
        evalStocks(i)
        print "COMPLETED " + i + " WAITING....."
        time.sleep(30)
    print "DONE"


if __name__ == "__main__":
    print "Cool"
    getStocks()

# Get Data In Dictonary Print Stuff


# Buy

# Sell
