import dotenv
dotenv.load_dotenv()

import requests
import os
from twilio.rest import Client
import time


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'accountSID'
auth_token = 'authtoken'
client = Client(account_sid, auth_token)

print(auth_token, account_sid)

def getBitcoinPrice():
    getPrice = requests.get('https://api.bybit.com/spot/v3/public/quote/ticker/price?symbol=BTCUSDT').json()
    btcPrice = getPrice['result']['price']
    return btcPrice

print(getBitcoinPrice())

def getEtheriumPrice():
    getPrice = requests.get('https://api.bybit.com/spot/v3/public/quote/ticker/price?symbol=ETHUSDT').json()
    ethPrice = getPrice['result']['price']
    return ethPrice
print(getEtheriumPrice())



while True:
    message = client.messages \
                    .create(
                        body=f"BitcoinPrice: {getBitcoinPrice()}",
                        from_='number given on Twilio',
                        to='yourPhoneNumber'
                    )

    print(message.sid)
    time.sleep(300)
