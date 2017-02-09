from yahoo_finance import Share
from pprint import pprint
import json

f = open('stockData.txt', 'w')

def printStocks(d,p,s):
    global f
    shares = 0
    capital = 1000
    prev = 44 # For CMG!!
    pos = []
    neg = []
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
        prev = money
        f.write(str(d[x])+ " | " + str(money) + " | " + str(perc))
        if perc > 13.4148875565:
            f.write("==== SELL ====")
            if shares > 0:
                capital = capital + (shares*int(shares))
                shares = 0
        if perc < -9.79928093728:
            f.write("==== BUY ====")
            if capital > money:
                locTemp = capital / money
                shares = shares + int(locTemp)
                capital = capital - (shares*int(locTemp))
        f.write("| MONEY " + str(capital) + "\n")
    f.write("\nPOS AVG : " + str(sum(pos)/len(pos)))
    f.write("\nNEG AVG : " + str(sum(neg)/len(neg)))
    f.write("\n+/- : " + str(capital - 1000))

def getStocks():
    text = ['CMG']
    i = text[0]
    dates = []
    values = []
    count = 0
    processed_text = i.upper()
    stock = Share(processed_text)
    sName = stock.get_name()
    for value in stock.get_historical('2006-01-01', '2016-12-01'):
        if count == 14:
            #print value['Date'] + " | " + value['Close'] + " \n"
            dates.insert(0, value['Date'])
            values.insert(0, value['Close'])
            count = 0
        count = count + 1
    printStocks(dates, values, sName)

if __name__ == "__main__":
    print "Cool"
    getStocks()

# Get Data In Dictonary Print Stuff


# Buy

# Sell
