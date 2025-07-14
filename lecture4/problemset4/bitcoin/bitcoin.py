import requests
import sys

try:
    URL =  "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(URL)
    data = response.json()
    extracted_dict = data.get("bpi", {})
    new_dict = extracted_dict.get("USD", {})
    rate = float(new_dict.get('rate_float'))
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    elif len(sys.argv) == 2:
        num = float(sys.argv[1])
        print(f"${num*rate:,.4f}")
        sys.exit(0)

except(requests.RequestException, ValueError):
    print("Command-line argument is not a number")
    sys.exit(1)
