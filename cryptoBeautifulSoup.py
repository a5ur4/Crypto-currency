from bs4 import BeautifulSoup
from datetime import datetime
import pywhatkit
import requests
import time

lista = []
contacts = []
now = datetime.now()

bitcoinPage = requests.get('https://www.google.com/finance/quote/BTC-BRL')
ethPage = requests.get('https://www.google.com/finance/quote/ETH-BRL')
dogePage = requests.get('https://www.google.com/finance/quote/DOGE-BRL')

bitcoin = BeautifulSoup(bitcoinPage.content, 'html.parser')
eth = BeautifulSoup(ethPage.content, 'html.parser')
doge = BeautifulSoup(dogePage.content, 'html.parser')

valueBit = bitcoin.find("div", class_="YMlKec fxKbKc")
valueEth = eth.find("div", class_="YMlKec fxKbKc")
valueDoge = doge.find("div", class_="YMlKec fxKbKc")

currentChangeBit = bitcoin.find("div", class_="JwB6zf")
currentChangeEth = eth.find("div", class_="JwB6zf")
currentChangeDoge = doge.find("span", class_="JwB6zf")

data = [
    ("\nBitcoin:", valueBit.text.strip()),
    ("24hP/V:", currentChangeBit.text.strip()),
    ("\nEthereum:", valueEth.text.strip()),
    ("24hP/V:", currentChangeEth.text.strip()),
    ("\nDogecoin:", valueDoge.text.strip()),
#    ("24hP/V:", currentChangeDoge.text.strip())
]

dt_string = now.strftime("Date and Hour: " + "%d/%m/%Y %H:%M:%S\n")

"""with open('numbers.txt', 'r') as f:
    contacts = [line.strip() for line in f]
    
for contact in contacts:
    print(contacts)"""

with open('cryptoBeautifulSoup.txt', 'w') as file:
    file.write(dt_string)
    for label, value in data:
        file.write(f"{label} {value}\n")
        
with open('cryptoBeautifulSoup.txt', 'r') as file:
    message = ''.join(file.readlines())

time.sleep(3)
pywhatkit.sendwhatmsg_instantly(contacts[0], message)