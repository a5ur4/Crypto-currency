from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime

service = Service()
option = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=option)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

urlBit = 'https://www.coingecko.com/en/coins/bitcoin'
urlETH = 'https://www.coingecko.com/en/coins/ethereum'
urlSOL = 'https://www.coingecko.com/en/coins/solana'

driver.get(urlBit)

valueBit = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[1]/span').text
changeBit = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').text
upOrDownBit = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').get_attribute('class')

if upOrDownBit == 'gecko-up':
    with open('cryptoCoinGecko.txt', 'w') as file:
        file.write(f"Bitcoin: {valueBit} {"+" + changeBit} {dt_string}")
elif upOrDownBit == 'gecko-down':
    with open('cryptoCoinGecko.txt', 'w') as file:
        file.write(f"Bitcoin: {valueBit} {"-" + changeBit} {dt_string}")
else:
    print("Something went wrong")


driver.get(urlETH)

valueETH = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[1]/span').text
changeETH = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').text
upOrDownETH = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').get_attribute('class')

if upOrDownETH == 'gecko-up':
    with open('cryptoCoinGecko.txt', 'a') as file:
        file.write(f"\nEthereum: {valueETH} {"+" + changeETH} {dt_string}")
elif upOrDownETH == 'gecko-down':
    with open('cryptoCoinGecko.txt', 'a') as file:
        file.write(f"\nEthereum: {valueETH} {"-" + changeETH} {dt_string}")
else:
    print("Something went wrong")

driver.get(urlSOL)

valueSOL = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[1]/span').text
changeSOL = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').text
upOrDownSOL = driver.find_element(By.XPATH, '//*[@id="gecko-coin-page-container"]/div[4]/div/div[1]/div[2]/div[2]/span').get_attribute('class')

if upOrDownSOL == 'gecko-up':
    with open('cryptoCoinGecko.txt', 'a') as file:
        file.write(f"\nSolana: {valueSOL} {"+" + changeSOL} {dt_string}")
elif upOrDownSOL == 'gecko-down':
    with open('cryptoCoinGecko.txt', 'a') as file:
        file.write(f"\nSolana: {valueSOL} {"-" + changeSOL} {dt_string}")
else:
    print("Something went wrong")