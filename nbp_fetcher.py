
import requests
import csv

def fetch_exchange_rates():
    url = "http://api.nbp.pl/api/exchangerates/tables/C?format=json"
    response = requests.get(url)
    data = response.json()

    rates = data[0]['rates']

    with open('currencies.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['currency', 'code', 'bid', 'ask'])
        for rate in rates:
            writer.writerow([rate['currency'], rate['code'], rate['bid'], rate['ask']])

    return rates