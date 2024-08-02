# Web Scraping de Criptomoedas

Este repositório contém dois scripts de exemplo para realizar web scraping de informações sobre criptomoedas utilizando BeautifulSoup e Selenium.

## Requisitos

- Python 3.x
- BeautifulSoup
- Requests
- Selenium
- WebDriver para o navegador de sua escolha (Edge, Chrome, Firefox, etc.)
- pywhatkit (opcional, para envio de mensagens via WhatsApp)

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/a5ur4/Crypto-currency.git
    cd Crypto-currency
    ```

2. Instale as dependências:
    ```sh
    pip install beautifulsoup4 requests selenium pywhatkit
    ```

## Scripts

### 1. `cryptoBeautifulSoup.py`

Este script utiliza BeautifulSoup para obter informações sobre as criptomoedas Bitcoin, Ethereum e Dogecoin a partir do Google Finance. As informações coletadas incluem o preço atual e a variação nas últimas 24 horas.

#### Uso

1. Execute o script:
    ```sh
    python cryptoBeautifulSoup.py
    ```

2. O script irá salvar as informações coletadas em um arquivo `cryptoBeautifulSoup.txt` e enviar uma mensagem via WhatsApp (se configurado).

### 2. `cryptoSelenium.py`

Este script utiliza Selenium para obter informações sobre as criptomoedas Bitcoin, Ethereum e Solana a partir do CoinGecko. As informações coletadas incluem o preço atual e a variação nas últimas 24 horas.

#### Uso

1. Certifique-se de ter o WebDriver instalado e configurado corretamente.
2. Execute o script:
    ```sh
    python cryptoSelenium.py
    ```

3. O script irá salvar as informações coletadas em um arquivo `cryptoCoinGecko.txt`.

## Contribuição

Se desejar contribuir com este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License.
