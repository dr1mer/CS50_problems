# Outputs the current cost of Bitcoins in USD to four decimal places using coindesk API

import json
import sys
import requests

if len(sys.argv)!=2:
    print("Missing command-line argument")
    sys.exit(1)
elif sys.argv[1].isalpha():
    print("Command-line argument is not a numbe")
    sys.exit(1)
else:
    n = float(sys.argv[1])
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dolar = r.json()
    amount=dolar["bpi"]["USD"]["rate"].replace(",","")
    amount=float(amount)
    print(f"${amount*n:,.4f}")
