print('Dracarys!')
print("Dragon's mother")

# Если есть и двойные и одинарные кавычки внутри строки, то нужно экранирование \
# Экранируем кавычки вокруг No, чтобы интерпретатор распознал их как часть строки
print("Dragon's mother said \"No\"")  # => Dragon's mother said "No"
print('Dragon\'s mother said "No"')  # => Dragon's mother said "No"

# Если нужно вывести сам обратный слеш, то работает такое же правило.
print('\\') # => \

print('"Khal Drogo\'s favorite word is "athjahakar""')

# 14 Экранированная последовательность — специальная комбинация символов в тексте. Например, \n — это перевод строки.

# Перевод строки
print("- Are you hungry?\n- Aaaarrrgh!")

print("Joffrey loves using \\n = Line feed \nAnd \\t = Tab \nAnd \\r = Carriage return")
# Joffrey loves using \n = Line feed
# And \t = Tab
# And \r = Carriage return

print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

# 15 Конкатенация
print('Dragon' + 'stone')  # => Dragonstone
print("King's" + ' Landing')  # => King'sLanding
print('Winter' +  ' came' + ' for' + ' the' + ' House' + ' of' + ' Frey.')

# 16 Кодировка
# ASCII Table https://www.cs.cmu.edu/%7Epattis/15-1XX/common/handouts/ascii.html
print(chr(63))  # => ?

print(chr(126))  # => ~
print(chr(94))  # => ^
print(chr(37))  # => %









# 26. Интерполяция вместо конкатенации (предпочтительнее, т.к. более читабельная)

# конкатенация
first_name = 'Joffrey'
greeting = 'Hello'
print(greeting + ", " + first_name + "!")
# => Hello, Joffrey!


# интерполяция. Буква f указывает на то, что мы создаем f-строку — шаблон, в который с помощью фигурных скобок подставляются значения переменных. На выходе получается обычная строка.
first_name = 'Joffrey'
greeting = 'Hello'
print(f'{greeting}, {first_name}!')
# => Hello, Joffrey!

# еще пример
school = 'Hexlet'
what_is_it = f'{school} - online courses'
print(what_is_it)  # => Hexlet - online courses


# 27. Извлечение символов из строки

# вывести первую букву
first_name = 'Alexander'
print(first_name[0])  # => A
# print(first_name[9])  # =>  IndexError: string index out of range - вышли за границу индекса

# то же самое, но через переменную
first_name = 'Alexander'
index = 0
print(first_name[index])  # => A

#тут 0 индекс это служебный символ
magic = '\nyou'
print(magic[1])  # => y

# вывести последнюю букву через обратный индекс (тут уже не с нуля, а с -1, потом -2 итд)
first_name = 'Alexander'
print(first_name[-1])  # => r


# 28 Срезы строк

# вытащить год из строки, конечный индекс 10 не включается в подстроку, т.е. с 6 по 9
value = '12-08-2034'
year = value[6:10]
print(year)  # => 2034 - строка на выходе, не число

#срезы с открытым концом и началом
value = 'Hexlet'
print(value[3:])  # 'let'
print(value[:3])  # 'Hex'

# Можно указать даже отрицательные индексы. В таком случае отсчет идет с обратной стороны:
value = 'Hexlet'
# Правая граница отрицательная. Считаем -1 от конца строки
print(value[3:-1])  # 'le'
# Левая граница отрицательная. Считаем -5 от конца строки
print(value[-5:3])  # 'ex'

# У срезов есть третий необязательный параметр — шаг извлечения. По умолчанию он равен единице, но мы можем его изменить:
value = 'la-la-lend'
print(value[0:10:3]) # 'llld' - каждый третий символ

# можно комбинировать с открытыми границами
value = 'Hexlet'
print(value[:5:2])  # 'Hxe'
print(value[1::2])  # 'elt'

# инвертирование строки с помощью отрицательного шага
value = 'Hexlet'
# Пропускаем обе границы
print(value[::-1])  # 'telxeH'

# Если используется отрицательный шаг, и элементы среза извлекаются в обратном порядке — тогда и границы среза тоже нужно указывать в обратном порядке.
# Первой указывается правая граница среза, второй — левая:
value = 'Hexlet'
# Символ с индексом 1 не будет включен в подстроку
print(value[4:1:-1])  # 'elx'

# Срезы можно указывать не только через числа, но и с использованием переменных:
value = 'Hexlet'
start = 1
end = 5
print(value[start:end])  # 'exle'

# Соберем все вместе:
# value = 'Hexlet'
# value[::] = 'Hexlet'  # Вся строка
# value[:] = 'Hexlet'  # Вся строка
# value[::2] = 'Hxe'  # Четные по порядку символы
# value[1::2] = 'elt'  # Нечетные по порядку символы
# value[::-1] = 'telxeH'  # Вся строка в обратном порядке
# value[5:] = 't'  # Строка, начиная с шестого символа
# value[:5] = 'Hexle'  # Строка до шестого символа
# value[-2:1:-1] = 'elx'  # Все символы с предпоследнего до третьего в обратном порядке. Во всех случаях выборки от большего индекса к меньшему нужно указывать шаг



# 29 Multi-line строки
text = '''Пример текста,
состоящего из
нескольких строк
'''
print(text)

text = '''Здесь не нужно экранировать 'одинарные' 
и "двойные" кавычки'''
print(text)

# Еще multi-line строки могут становиться f-строками для интерполяции:
a = 'A'
b = 'B'

# Слева добавился f
text = f'''{a} и {b}
сидели на трубе
'''
print(text)