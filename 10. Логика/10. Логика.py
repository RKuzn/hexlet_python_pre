# 51 Логический тип

# Логическая операция типа 5 > 4 или password == text — это выражение. Его результат — специальное значение True («истина») или False («ложь»). Это новый для нас тип данных — bool.
# Наряду со строками (str) и целыми и рациональными числами, тип bool (булев) — это один из примитивных типов данных в Python.
result = 5 > 4
print(result)  # => True
print('one' != 'one')  # => False
print(10.5 == 10.5)  # => True

# Попробуем написать простую функцию, которая принимает на вход возраст ребенка и определяет, младенец ли он. Младенцами считаются дети до года:

def is_infant(age):
    return age < 1

print(is_infant(3))  # => False


# 52 Предикаты
# Функция is_infant() — это функция-предикат или функция-вопрос. Предикат отвечает на утвердительный вопрос «да» или «нет», возвращая значение типа bool. Предикаты во всех языках принято именовать особым образом для простоты анализа. В Python предикаты начинаются с префикса is или has:
#
# is_infant() — «младенец ли?»
# has_children() — «есть ли дети?»
# is_empty() — «пустой ли?»
# has_errors() — «есть ли ошибки?»
# Функция считается предикатом, если она возвращает булевы значения True или False.



# напишем функцию проверки четности:

def is_even(number):
    return number % 2 == 0

print(is_even(10))  # => True
print(is_even(3))   # => False


# 54 Логические операторы And/ Or, Отрицание Not

#Теперь представим, что мы хотим купить квартиру, которая удовлетворяет таким условиям: площадь от 100 квадратных метров и больше на любой улице ИЛИ площадь от 80 квадратных метров и больше, но на центральной улице Main Street.
#Напишем функцию, которая проверит квартиру. Она принимает два аргумента: площадь — число и название улицы — строку:

def is_good_apartment(area, street):
    return area >= 100 or (area >= 80 and street == 'Main Street')

print(is_good_apartment(91, 'Queens Street'))  # => False
print(is_good_apartment(78, 'Queens Street'))  # => False
print(is_good_apartment(70, 'Main Street'))    # => False

print(is_good_apartment(120, 'Queens Street'))  # => True
print(is_good_apartment(120, 'Main Street'))    # => True
print(is_good_apartment(80, 'Main Street'))     # => True

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(is_leap_year(2018)) # false
print(is_leap_year(2017)) # false
print(is_leap_year(2016)) # true

# Реализуйте функцию is_palindrome(), которая определяет, является ли слово палиндромом или нет.
def is_palindrome(word):
    word_low = word.lower()
    return word_low == word_low[::-1]

print(is_palindrome('шалаш')) # true
print(is_palindrome('хекслет')) # false)

# Реализуйте функцию is_not_palindrome(), которая проверяет что слово НЕ является палиндромом:
def is_not_palindrome(word):
    return not is_palindrome(word)

print(is_not_palindrome('шалаш')) # false
print(is_not_palindrome('яга')) # false


# 56 Результат логических выражений

# Оператор ИЛИ будет проверять значения слева направо, и возвращает первый аргумент, который может быть преобразован в True или последний. В данном примере это число 42.
print(0 or False or '' or [] or 42 or "Hello")  ## 42

# Оператор И будет проверять значения слева направо и возвращать первый аргумент, который может быть преобразован в False или последний. В данном примере это пустой список ([]).
print(42 and "Hello" and [] and 0)  ## []

# Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой. Если да, то возвращается 'yes' иначе 'no'
# Проверить то, является ли переданный параметр строкой, можно при помощи функции isinstance():

def string_or_not(value):
    return isinstance(value, str) and 'yes' or 'no'

print(string_or_not('Hexlet')) # 'yes'
print(string_or_not(10)) # 'no'
print(string_or_not('')) # 'yes'
print(string_or_not(False)) # 'no'