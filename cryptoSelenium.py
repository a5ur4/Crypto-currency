from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

service = Service()
option = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=option)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

urlBit = 'https://www.coingecko.com/en/coins/bitcoin'
urlETH = 'https://www.coingecko.com/en/coins/ethereum'
urlSOL = 'https://www.coingecko.com/en/coins/solana'
urlWhatsapp = 'https://web.whatsapp.com/'

driver.get(urlBit)

valueBit = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[1]/span').text
changeBit = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').text
upOrDownBit = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').get_attribute('class')

if upOrDownBit == 'gecko-up':
    with open('cryptoCoinGecko.txt', 'w') as file:
        file.write(f"\nBitcoin: {valueBit} {"+" + changeBit}")
elif upOrDownBit == 'gecko-down':
    with open('cryptoCoinGecko.txt', 'w') as file:
        file.write(f"\nBitcoin: {valueBit} {"-" + changeBit}")
else:
    print("Something went wrong")

driver.get(urlETH)

valueETH = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[1]/span').text
changeETH = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').text
upOrDownETH = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').get_attribute('class')

if upOrDownETH == 'gecko-up':
    with open('cryptoCoinGecko.txt', 'a') as file:
        file.write(f"\nEthereum: {valueETH} {"+" + changeETH}")
elif upOrDownETH == 'gecko-down':
    with open('cryptoCoinGecko.txt', 'a') as file:
        file.write(f"\nEthereum: {valueETH} {"-" + changeETH}")
else:
    print("Something went wrong")

driver.get(urlSOL)

valueSOL = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[1]/span').text
changeSOL = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').text
upOrDownSOL = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').get_attribute('class')

if upOrDownSOL == 'gecko-up':
    with open('cryptoCoinGecko.txt', 'a') as file:
        file.write(f"\nSolana: {valueSOL} {"+" + changeSOL}")
        file.write(f"\n")
elif upOrDownSOL == 'gecko-down':
    with open('cryptoCoinGecko.txt', 'a') as file:
        file.write(f"\nSolana: {valueSOL} {"-" + changeSOL}")
        file.write(f"\n")
else:
    print("Something went wrong")
    
driver.get(urlWhatsapp)

print("Please scan the QR code to login to WhatsApp Web")

wait = WebDriverWait(driver, 600)

try:
    searchBar = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'))
    )
    print("Logged in")
    
    searchBar.send_keys("") # Enter the name or number of the contact you want to send the message to
    searchBar.send_keys(Keys.ENTER)
    
    cryptoMessage = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
    )
    
    message = 'Hello there! Here are the current values of some cryptocurrencies on: ' + dt_string + '\n'
    message += ''.join(open('cryptoCoinGecko.txt').readlines())
    
    cryptoMessage.send_keys(message)
    
    inputEnter = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'))
    )
    
    time.sleep(2)
    inputEnter.send_keys(Keys.ENTER)
finally:
    driver.quit()