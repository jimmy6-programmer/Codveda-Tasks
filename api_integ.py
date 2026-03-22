import requests

# Define API Url
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    response = requests.get(url)

    if response.status_code == 200:

        # Convert data to json
        data = response.json()
        # Extract values
        price = data['bitcoin']['usd']
        # Display data
        print("Current bitcoin price:", "$" + str(price), "USD")
    else:
        print("Access denied")
        print(response.status_code)
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)            