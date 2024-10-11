# Python — язык со строгой типизацией.

# Python не разрешит сложить число 1 и строку '7', потому что это значения разных типов.
#print(1 + '7')  # TypeError: unsupported operand type(s)...

# Неизменяемость примитивных типов
first_name = 'Alexander'
#first_name[0] = 'B'
# Ошибка: TypeError: 'str' object does not support item assignment

# Есть большая разница между изменением значения переменной и изменением самого значения. Примитивные типы в Python поменять нельзя, а составные — можно. Также можно без проблем заменить значение переменной.


# 33 Явное преобразование типов

# str станет int
number = int('345')
print(number)  # => 345

converted_value3 = int(False)
print(converted_value3)  # => 0

converted_value4 = int(True)
print(converted_value4)  # => 1

converted_value5 = int(3.5)
print(converted_value5)  # => 3

# Точно так же можно преобразовать данные в строки str() и число с плавающей точкой float():
value = str(10)
print(value)  # '10'

value2 = str(True)
print(value2)  # 'True'

value3 = float(5)
print(value3)  # 5.0


# Неявно выполняется код float(3) + 1.2
value = 3 + 1.2
print(value)  # => 4.2


