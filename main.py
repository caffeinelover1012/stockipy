from cfonts import render
import pandas as pd
from isvalidticker import isvalid
import yfinance as yf
import os.path
import matplotlib.pyplot as plt


def makeFavsList(p=True):
    favs = []
    inp = ""
    while inp != "x":
        inp = str(input("Enter Stock Ticker: "))
        if inp == "x":
            break
        validity = isvalid(inp.upper())
        if validity:
            if p:
                print(f"Adding {validity} to Favorites\n")
            favs.append(inp.upper())
        else:
            print("Invalid Stock ticker, ", inp)
            print("Try Again")
            continue
    return favs


def parseContext():
    parsed = {"username": "", "favorites": []}
    if not os.path.exists('ctx.txt'):
        print("Welcome to Stockipy!\n")
        name = input("Enter your Name: ")
        parsed["username"] = name
        print("Any favorite Stocks? (Enter x to stop) ")
        favs = makeFavsList()
        with open('ctx.txt', 'w') as f:
            f.write(name)
            f.write('\n')
            for i in favs:
                f.write(str(i+"\n"))
    else:
        f = open("ctx.txt", "r")
        parsed["username"] = str(f.readline())
        rem = f.read().splitlines()
        parsed["favorites"] = rem
    return parsed


CTX = parseContext()


def getDefaultDetails(ticker):
    # get data on this ticker
    tickerData = yf.Ticker(ticker)
    i = tickerData.info
    details = {"Name": i['shortName'], "Current Price": i['currentPrice'], "Opening Price": i['open'],
               "Day H/L": f"{i['dayHigh']} / {i['dayLow']}", "52W H/L": f"{i['fiftyTwoWeekHigh']} / {i['fiftyTwoWeekLow']}"}
    return details


def showMenu(options):
    for sr, option in enumerate(options):
        print(f"{sr+1}) {option}")


def prettyPrintDict(dictionary):
    if not dictionary.get('Name'):
        dictionary['Name']=dictionary['shortName']
    print("Details for "+dictionary['Name'])
    print("------------------------------------------------")
    n = dictionary.pop('Name')
    for k, v in dictionary.items():
        print(f"{k}: {v}")
    print("\n")

def getAllDetails(ticker):
    # get all data on this ticker
    tickerData = yf.Ticker(ticker)
    return tickerData.info

output = render('Stockipy', colors=['yellow', 'red'], align='center')
print(output)
print('Welcome, ', CTX["username"], end="\n")


OPTIONS = ["Show your Favourites", "Search for a Specific Stock",
           "View Historical data of a given Stock", "Create a MATPLOT Graph of multiple tickers","Edit your Favorites", "Edit Name", "Exit"]
choice = -1


# driver
while (choice) != len(OPTIONS):
    showMenu(OPTIONS)
    choice = input("\n * Choose an option: ")
    if choice.isnumeric():
        choice = int(choice)
    if (choice == 1):
        CTX = parseContext()
        print("Fetching data for: ", " ".join(CTX['favorites']))
        for stock in CTX["favorites"]:
            prettyPrintDict(getDefaultDetails(stock))

    elif (choice == 2):
        # define the ticker symbol
        tickerSymbol = input("Enter Stock Symbol: ").upper()
        prettyPrintDict(getDefaultDetails(tickerSymbol))
        moreInfo = input("Want More Info? (y/n): ")
        if moreInfo=='y':
            prettyPrintDict(getAllDetails(tickerSymbol))
        elif moreInfo=='n':
            print("Ok")
        else:
            print("Invalid Input. Try Again.")
            
    elif (choice == 3):
        tickerSymbol = input("Enter Stock Symbol: ").upper()
        ticker = yf.Ticker(tickerSymbol)
        startDate = input("Enter Start Date: (YYYY-MM-DD): ")
        endDate = input("Enter End Date: (YYYY-MM-DD): ")
        try:
            tickerHistorical = ticker.history(start=startDate, end=endDate)
            print(tickerHistorical)
        except:
            print("Invalid Input")
    elif (choice==4):
        print("Enter all stocks you'd like to graph (x to stop): ")
        stcks = makeFavsList(p=False)
        print("Enter Time Period. Options: ")
        period = ["1d",  "5d",  "1mo",  "3mo",  "6mo",  "1y",  "2y",  "5y",  "10y",  "ytd",  "max"]
        print(" ".join(period))
        pchoice = input("Enter Time Period: ")
        if pchoice.lower() not in period:
            print("Invalid Input")
            timePeriod = input("Enter Time Period: ")
        print("Got it, please wait...")
        for stck in stcks:
            yf.Ticker(stck).history(period=pchoice)['Close'].plot(label=stck, legend=True,ylabel = "Price", title="Stock Prices")
        plt.show()
    elif (choice == 5):
        print("Enter new Favourite List (x to stop): ")
        fav = makeFavsList()
        with open('ctx.txt', 'w') as f:
            f.write(CTX["username"])
            f.write('\n')
            for i in fav:
                f.write(str(i+"\n"))
    elif (choice == 6):
        newName = str(input("Retype Name: "))
        CTX['username'] = newName
        with open('ctx.txt', 'w') as f:
            f.write(newName)
            f.write('\n')
            for i in CTX["favorites"]:
                f.write(str(i+"\n"))
        print("Name changed to ", newName)

    elif (choice == 7):
        print("Thank you for using Stockipy!")

    else:
        print("Invalid Choice Try again")
        continue
