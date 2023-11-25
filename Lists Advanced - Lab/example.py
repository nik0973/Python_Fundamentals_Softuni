import requests

def get_price_eur_usd():
    url = 'https://www.freeforexapi.com/api/live?pairs=EURUSD'

    try:
        response = requests.get(url)
        date = response.json()
        rate = date['rates']['EURUSD']['rate']
        return rate

    except requests.exceptions.RequestException as e:
        print('Error', e)


current_rate_EURUSD = get_price_eur_usd()
print(current_rate_EURUSD)