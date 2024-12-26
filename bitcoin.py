import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    rates = float(response['bpi']['USD']['rate'].replace(',', ''))
    multiplier = float(sys.argv[1])
    result = rates * multiplier
    print(f"${result:,.4f}")

except requests.RequestException:
    ...
except ValueError:
    sys.exit("Command-line argument is not a number")
