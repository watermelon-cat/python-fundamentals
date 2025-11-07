#import librarys
import requests                            #to make HTTP request to the Polygon.io API
import datetime                           #For formatting and working with dates
import matplotlib.pyplot as plt

#SETUP SECTION+++++
API_KEY = "9q27K7yNvxYCj3KLj_qrmd6CpwTgrkOQ"                #replace this with your actual Polygon.io API key
TICKER = "DUOL"                                   #Ticker symbol for the stock you want to look up ( ex. Dualinogo)
START_DATE = "2021-07-01"                         #Duolingo IPO'd in July 2021, so we can start here
END_DATE = "2024-07-01"                           #You can update this to today or a different end date

#function: Fetch daily stock prices
def fetch_stock_data(ticker, start_date, end_date):
    #construct the URL for Polygon's Aggregates ( BARS) endpoint
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}"
    
    #set up parameters for the request
    params = {
        "adjusted": "true",           #use adjusted prices (takes splits/dividends into account)
        "sort": "asc",                #sort by oldest to newest
        "limit": 50000,               #fetch up to 50,000 records at once (safe for long time spans)
        "apikey": API_KEY             #fetch yout personal API key
    }
    
    #sent the HTTP GET request
    response = requests.get(url, params=params)
    
    #Parse the response into JSON format
    data = response.json()
    
    #check if the response contains the expected 'results' key
    if "results" not in data:
        print("Error:", data.get("error", "Unknown issue")) #Show error messafe if avaliable
        return [] #return an empty list if something went wrong
    
    return data["results"] #return the list of daily data points

#MAIN ========================

#call the function to get data
stock_data = fetch_stock_data(TICKER, START_DATE, END_DATE)

#loop through and display the first few days of results
for day in stock_data[:5]: #Only print the first 5 days to keep it short
    #convert the timestamp from milliseconds to readable date
    date = datetime.datetime.fromtimestamp(day["t"] / 1000).strftime("%Y-%m-%d")
    
    #print out the key stock data for that day
    print(f"{date} | Open: {day['o']} | High: {day['h']} | Low: {day['l']} | Close: {day['c']}")
    
#if data is empty, exit early with a message
if not stock_data:
    print("No data returned. Check the API key, ticker, or date range.")
else:
    #Convert timestamps to datetime objects for plotting
    dates = [datetime.datetime.fromtimestamp(day["t"] / 1000) for day in stock_data]
    
    #Extract the closing prices for each day
    close_prices = [day["c"] for day in stock_data]
    
    #=== Plot the data ===
    plt.figure(figsize=(12,6)) #set the size of the plot
    plt.plot(dates, close_prices, label=f'{TICKER} Closing Price', color = "green") #plot the close prices
    plt.title(f'{TICKER} Stock Price (Since IPO)') #title of graph
    plt.xlabel("Date") #label for the x-axis
    plt.ylabel("Price (USD)") #Label for the y-acis
    plt.grid(True)  #add gridlines for better readablility
    plt.legend() #show the legend with the ticker name
    plt.tight_layout() #adjust layout to avoid overlap
    plt.show() #display the final graph
