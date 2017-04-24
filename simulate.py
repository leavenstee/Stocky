import csv, sys
from random import randint
import stocky as stocky
# Predict on Dice Roll 3 every day
def sim_dice_roll_3_daily():
    print "\n====================="
    print "= DICE ROLL 3 DAILY ="
    print "====================="
    assetsarr = []
    for x in range(0, 10):
        money = 10000
        assets = 0
        shares = 0
        lastprice = 0
        filename = 'aapl1.csv'
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    lastprice = float(row[0])
                    #print "CURRENT CAPITAL: " + str(money) + " CURRENT SHARES HELD: " + str(shares)
                    num = randint(1,3)
                    if(num == 1):  # buy
                        #print "SUGGEST BUY"
                        if (money > float(row[0])):
                            amount = int(money/float(row[0]))
                            buyamount = amount*float(row[0])
                            money = money - buyamount
                            shares = shares + amount
                            #print "BOUGHT " + str(amount) + " SHARES AT " + row[0]
                    elif (num == 2): # Sell
                        #print "SUGGEST SELL"
                        if (shares > 1):
                            sellamount = shares*float(row[0])
                            money = money + sellamount
                            shares = 0
                            #print "SOLD " + str(shares) + " SHARES AT " + row[0]
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        assets = money + lastprice*shares
        #print "TOTAL ASSETS THROUGH 2016  "  +str(assets)
        assetsarr.append(assets)
    #endMoney.append(assets)
    avg = 0
    for i in assetsarr:
        avg = avg + i
        #print i
    print " ASSETS: " + str(assetsarr[0])


# Predict on Dice Roll 3 every week
def sim_dice_roll_3_week():
    print "\n======================"
    print "= DICE ROLL 3 WEEKLY ="
    print "======================"
    assetsarr = []
    for x in range(0, 10):
        money = 10000
        assets = 0
        shares = 0
        lastprice = 0
        count = 0
        filename = 'aapl1.csv'
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    if(count == 6):
                        lastprice = float(row[0])
                        #print "CURRENT CAPITAL: " + str(money) + " CURRENT SHARES HELD: " + str(shares)
                        num = randint(1,3)
                        if(num == 1):  # buy
                            #print "SUGGEST BUY"
                            if (money > float(row[0])):
                                amount = int(money/float(row[0]))
                                buyamount = amount*float(row[0])
                                money = money - buyamount
                                shares = shares + amount
                                #print "BOUGHT " + str(amount) + " SHARES AT " + row[0]
                        elif (num == 2): # Sell
                            #print "SUGGEST SELL"
                            if (shares > 1):
                                sellamount = shares*float(row[0])
                                money = money + sellamount
                                shares = 0
                                #print "SOLD " + str(shares) + " SHARES AT " + row[0]

                        count = 0
                    count = count + 1
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        assets = money + lastprice*shares
        #print "TOTAL ASSETS THROUGH 2016  "  +str(assets)
        assetsarr.append(assets)
    #endMoney.append(assets)
    avg = 0
    for i in assetsarr:
        avg = avg + i
        #print i
    print " ASSETS: " + str(assetsarr[0])


# Buy Every Monday Sell Every Thursday
def sim_buy_monday_sell_thursday():
    print "\n============================"
    print "= BUY MONDAY SELL THURSDAY ="
    print "============================"
    assetsarr = []
    for x in range(0, 10):
        money = 10000
        assets = 0
        shares = 0
        lastprice = 0
        num = 0
        filename = 'aapl1.csv'
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    lastprice = float(row[0])
                    #print "CURRENT CAPITAL: " + str(money) + " CURRENT SHARES HELD: " + str(shares)

                    if(num == 0):  # buy
                        #print "SUGGEST BUY"
                        if (money > float(row[0])):
                            amount = int(money/float(row[0]))
                            buyamount = amount*float(row[0])
                            money = money - buyamount
                            shares = shares + amount
                            #print "BOUGHT " + str(amount) + " SHARES AT " + row[0]
                    elif (num == 4): # Sell
                        #print "SUGGEST SELL"
                        if (shares > 1):
                            sellamount = shares*float(row[0])
                            money = money + sellamount
                            shares = 0
                            #print "SOLD " + str(shares) + " SHARES AT " + row[0]
                    elif (num == 7):
                        num = 0

                    num = num + 1
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        assets = money + lastprice*shares
        #print "TOTAL ASSETS THROUGH 2016  "  +str(assets)
        assetsarr.append(assets)
    #endMoney.append(assets)
    avg = 0
    for i in assetsarr:
        avg = avg + i
        #print i
    print " ASSETS: " + str(assetsarr[0])

# Predict on Nueral Net
def sim_neural_net():
    print "\n======================="
    print "= STOCKY - NUERAL NET ="
    print "======================="
    filename = 'pred.csv'
    predVal = 0
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            predVal = int(row[0])


    assetsarr = []
    for x in range(0, 10):
        money = 10000
        assets = 0
        shares = 0
        lastprice = 0
        num = 0
        first = False
        filename = 'aapl1.csv'
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    lastprice = float(row[0])
                    #print "CURRENT CAPITAL: " + str(money) + " CURRENT SHARES HELD: " + str(shares)

                    if(predVal > 10): # buy
                        if (first == False):
                            if (money > float(row[0])):
                                amount = int(money/float(row[0]))
                                buyamount = amount*float(row[0])
                                money = money - buyamount
                                shares = shares + amount
                                first = True
                                #print "BOUGHT " + str(amount) + " SHARES AT " + row[0]

            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        assets = money + lastprice*shares
        #print "TOTAL ASSETS THROUGH 2016  "  +str(assets)
        assetsarr.append(assets)
    #endMoney.append(assets)
    avg = 0
    for i in assetsarr:
        avg = avg + i
        #print i
    print " ASSETS: " + str(assetsarr[0])






sim_dice_roll_3_daily()
sim_dice_roll_3_week()
sim_buy_monday_sell_thursday()
sim_neural_net()
