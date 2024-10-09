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


