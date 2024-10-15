import requests
from pprint import pprint

# explore

# https://freecurrencyapi.com/
# API_KEY = 'fca_live_mL8LwHPBU8Drw0owNOGZ5oIC7TzxEW4nJvrex0xl'
# url = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies=RUB'
# print(url)  # https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_mL8LwHPBU8Drw0owNOGZ5oIC7TzxEW4nJvrex0xl&currencies=RUB
#
# response = requests.get(url)
# print(response)  # <Response [200]> - это ок, успешный запрос
# data_info = response.json()
# print(response.json())  # {'data': {'RUB': 96.1223232247}}
#
# # курс рубля можно вытащить так
# rub_currency = data_info['data']
# print(rub_currency['RUB'])  # 96.1223232247
#
# # или так, тип более устойчиво, если такого узла в джисоне нету
# rub_currency = data_info.get('data', None)
# print(rub_currency['RUB'])  # 96.1223232247
#
# rub = rub_currency['RUB']
# print(round(rub, 2))  # 96.12


# main functions
# секция импорт наверху

API_KEY = 'fca_live_mL8LwHPBU8Drw0owNOGZ5oIC7TzxEW4nJvrex0xl'

# функция конвертирования
def convert_currency(from_currency, to_currency):
    # url = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies={from_currency}'
    url = (f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies={from_currency}'
           f'&base_currency={to_currency}')
    try:
        response = requests.get(url)
        data_info = response.json()
        currency = data_info.get('data', None)
        currency_value = currency.get(from_currency)
        #print(f'Стоимость {to_currency} = {currency_value} {from_currency}')
        return currency_value
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        print(f"Failure - Unable to establish connection: {e}.")
        return 0
    except Exception as e:
        print(f"Failure - Unknown error occurred: {e}.")
        return 0



# функция, возвращающая список валют
def get_all_currencties():
    all_currency_url = f'https://api.freecurrencyapi.com/v1/currencies?apikey={API_KEY}&currencies=&base_currency='
    response = requests.get(url=all_currency_url)
    all_currency_data = response.json().get('data', None)
    # pprint(all_currency_data)
    # print(all_currency_data.get('ZAR'))
    print(type(all_currency_data))
    return all_currency_data

# print(get_all_currencties())
# print(convert_currency('RUB','EUR'))
# print(convert_currency('EUR','RUB'))