from onlinerequest import get_all_currencties, convert_currency
import sys

# 1. Приветствие
# 2. Описание функционала
# 3. Вывод списка валют
# 4. Ввод кода имеющейся валюты
# 5. Количество этой валюты
# 6. Ввод кода валюты конвертации
# 7. Итог/результат


# 1.
print("Добро пожаловать, уважаемый")

# 2.
print("""
Наша программа поможет Вам конвертировать вашу валюту:
- Выберите валюту, которую хотите перевести;
- Вводите количество этой валюты;
- Выберите валюту для конвертации

""")


# 3. Вывод списка валют
ALL_CURRENCIES = get_all_currencties()
count = 1
for currency in ALL_CURRENCIES:
    print(f'{count} -> {currency}')
    count += 1

# 4.
user_currency = input("Введите имеющуюся валюту: ")
user_currency = user_currency.upper()
if user_currency not in ALL_CURRENCIES:
    print("Нормальную валюту вводи, э")
    sys.exit()

# 5
current_amount = input("Введите имеющуюся сумму: ")
try:
    val = float(current_amount)
except ValueError:
    print("Нормальную сумму вводи, э")
    sys.exit()

# 6.
conversion_currency = input("Выберите валюту для конвертации: ")
conversion_currency = conversion_currency.upper()
if conversion_currency not in ALL_CURRENCIES:
    print("Нормальную валюту вводи, э")
    sys.exit()

result = convert_currency(from_currency=conversion_currency, to_currency=user_currency) * float(current_amount)
print(f"Итого {round(result, 3)}")
