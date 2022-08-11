from cfonts import render
import pandas as pd
from isvalidticker import isvalid
import yfinance as yf
import os.path

def makeFavsList():
    favs = []
    inp=""
    while inp!="x":
        inp = str(input("Enter Stock Ticker: "))
        if inp=="x":
            break
        validity = isvalid(inp.upper())
        if validity:
            print(f"Adding {validity} to Favorites\n")
            favs.append(inp.upper())
        else:
            print("Invalid Stock ticker, ",inp)
            print("Try Again")
            continue
    return favs

def parseContext():
    parsed = {"username":"", "favorites":[]}
    if not os.path.exists('ctx.txt'):
        print("Welcome to Stockipy!\n")
        name = input("Enter your Name: ")
        parsed["username"]=name
        print("Any favorite Stocks? (Enter x to stop) ")
        favs = makeFavsList()
        with open('ctx.txt', 'w') as f:
            f.write(name)
            f.write('\n')
            for i in favs:
                f.write(str(i+"\n"))
    else:
        f = open("ctx.txt", "r")
        parsed["username"]=str(f.readline())
        rem = f.read().splitlines()
        parsed["favorites"]=rem
    return parsed

CTX = parseContext()

def getDefaultDetails(ticker):
    # get data on this ticker
    tickerData = yf.Ticker(ticker)
    i = tickerData.info
    details = {"Name": i['shortName'],"Current Price":i['currentPrice'],"Opening Price":i['open'],"Day H/L":f"{i['dayHigh']} / {i['dayLow']}", "52W H/L":f"{i['fiftyTwoWeekHigh']} / {i['fiftyTwoWeekLow']}"}
    return details

def showMenu(options):
    for sr,option in enumerate(options):
        print(f"{sr+1}) {option}")

def prettyPrintDict(dictionary):
    print("Details for "+dictionary['Name'])
    print("------------------------------------------------")
    n=dictionary.pop('Name')
    for k, v in dictionary.items():
        print(f"{k}: {v}")

output = render('Stockipy', colors=['yellow', 'red'], align='center')
print(output)
print('Welcome, ', CTX["username"], end="\n")



OPTIONS = ["Show your Favourites", "Search for a Specific Stock", "Show Today's Top Gainers/Losers", "Edit your Favorites", "Edit Name", "Exit"]
choice = -1


# driver
while (choice)!=6:
    showMenu(OPTIONS)
    choice = input("\n * Choose an option: ")
    if choice.isnumeric():
        choice=int(choice)
    if (choice==1):
        print("Fetching data for: ", " ".join(CTX['favorites']))
        for stock in CTX["favorites"]:
            print("\n")
            prettyPrintDict(getDefaultDetails(stock))

    elif (choice==2):
        #define the ticker symbol
        tickerSymbol = input("Enter Stock Symbol: ").upper()
        prettyPrintDict(getDefaultDetails(tickerSymbol))
        print("\n")
        
    elif (choice==3):
        print("3")

    elif (choice==4):
        pass

    elif (choice==5):
        print("5")

    elif (choice==6):
        print("6")

    else:
        print("Invalid Choice Try again")
        continue

    


