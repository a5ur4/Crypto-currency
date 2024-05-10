from bs4 import BeautifulSoup
from datetime import datetime
import pywhatkit
import requests
import time

lista = []
contacts = []
now = datetime.now()

bitcoinPage = requests.get('https://www.binance.com/pt-BR/price/bitcoin')
ethPage = requests.get('https://www.binance.com/pt-BR/price/ethereum')
solPage = requests.get('https://www.binance.com/pt-BR/price/solana')

bitcoin = BeautifulSoup(bitcoinPage.content, 'html.parser')
eth = BeautifulSoup(ethPage.content, 'html.parser')
sol = BeautifulSoup(solPage.content, 'html.parser')

valueBit = bitcoin.find("div", class_="css-1bwgsh3")
valueEth = eth.find("div", class_="css-1bwgsh3")
valueSol = sol.find("div", class_="css-1bwgsh3")

currentChangeBit = bitcoin.find("div", class_="css-4j2do9")
currentChangeEth = eth.find("div", class_="css-4j2do9")
currentChangeSol = sol.find("div", class_="css-4j2do9")

data = [
    ("\nBitcoin:", valueBit.text.strip()),
    ("24hP/V:", currentChangeBit.text.strip()),
    ("\nEthereum:", valueEth.text.strip()),
    ("24hP/V:", currentChangeEth.text.strip()),
    ("\nSolana:", valueSol.text.strip()),
    ("24hP/V:", currentChangeSol.text.strip())
]

dt_string = now.strftime("Date and Hour: " + "%d/%m/%Y %H:%M:%S\n")

"""with open('numbers.txt', 'r') as f:
    contacts = [line.strip() for line in f]
    
for contact in contacts:
    print(contacts)"""

with open('currency.txt', 'w') as file:
    file.write(dt_string)
    for label, value in data:
        file.write(f"{label} {value}\n")
        
with open('currency.txt', 'r') as file:
    message = ''.join(file.readlines())

time.sleep(3)
pywhatkit.sendwhatmsg_instantly(contacts[0], message)

#made by: _a5ur4