from polygon import RESTClient

# Initialize the RESTClient with your API key
api_key = '21ZQIG71np20Edlffle1jqHi678i0Mcb'
rest_client = RESTClient(api_key)

# Retrieve historical aggregate data for a stock symbol
symbol = 'AAPL'
start_date = '2024-02-01'
end_date = '2024-02-05'

# Make the request to retrieve historical aggregate data
resp = rest_client.stocks_equities_aggregates(symbol, 1, 'day', start_date, end_date)

# Process the response
print(resp)

# Remember to close the RESTClient
rest_client.close()
