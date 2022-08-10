from lib2to3.pgen2.literals import evalString
from cfonts import render, say
import pandas as pd
import requests
import yfinance as yf
import os.path

output = render('Stockipy', colors=['yellow', 'red'], align='center')
print(output)

OPTIONS = ["Show your Favourites", "Search for a Specific Stock", "Show Today's Top Gainers/Losers", "Edit your Favorites", "Edit Name", "Exit"]
choice = -1

def parseContext():
    if not os.path.exists('ctx.txt'):
        with open('ctx.txt', 'w') as f:
            f.write('readme')
    else:
        print("file exists")
    return ["File"]

def getDefaultDetails(ticker):
    # get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    i = tickerData.info
    details = {"Name": i['shortName'],"Current Price":i['currentPrice'],"Opening Price":i['open'],"Day H/L":f"{i['dayHigh']} / {i['dayLow']}", "52W H/L":f"{i['fiftyTwoWeekHigh']} / {i['fiftyTwoWeekLow']}"}
    return details

def showMenu(options, context=None):
    for sr,option in enumerate(options):
        print(f"{sr+1}) {option}")

def prettyPrintDict(dictionary):
    print("Details for "+dictionary['Name'])
    print("------------------------------------------------")
    n=dictionary.pop('Name')
    for k, v in dictionary.items():
        print(f"{k}: {v}")

CTX = parseContext()
# driver
while (choice)!=6:
    showMenu(OPTIONS)
    choice = input("\n * Choose an option: ")
    if choice.isnumeric():
        choice=int(choice)
    if (choice==1):
        print("1")
    elif (choice==2):
        #define the ticker symbol
        tickerSymbol = input("Enter Stock Symbol: ")
        tickerData = yf.Ticker(tickerSymbol)
        prettyPrintDict(getDefaultDetails(tickerSymbol))
    elif (choice==3):
        print("3")

    elif (choice==4):
        print("4")

    elif (choice==5):
        print("5")

    elif (choice==6):
        print("6")

    else:
        print("Invalid Choice Try again")
        continue

    


