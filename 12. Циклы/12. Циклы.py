# 62 Цикл While


# Напишем функцию с простым циклом, который будет n раз выводить на экран строку 'Hello!':

def print_hello(n):
    counter = 0
    while counter < n:
        print('Hello!')
        counter = counter + 1

print_hello(2)
# => Hello!
# => Hello!

# функция выводит на экран числа от числа-аргумента до одного:
def print_numbers(number):
    counter = number
    while counter > 0:
        print(counter)
        counter = counter - 1
    print('finished!')

print_numbers(4)


# 63 Агрегация данных (Числа)

# умножение чисел диапазона
def multiply_numbers_from_range(start, finish):
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i +1
    return result

print(multiply_numbers_from_range(1,5))


# 64 Агрегация данных (Строки)

# функция, которая умеет умножать строку - в цикле происходит «наращивание» строки указанное количество раз:
def repeat(text, times):
    # Нейтральный элемент для строк — пустая строка
    result = ''
    i = 1

    while i <= times:
        # Каждый раз добавляем строку к результату
        result = result + text
        i = i + 1

    return result

# Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку:
def join_numbers_from_range(start, finish):
    i = start
    result = ''
    while i <= finish:
        result = result + str(i)
        i = i + 1
    return result


print(join_numbers_from_range(1, 5))


# 65 Обход строк

# пример кода, который печатает буквы каждого слова на отдельной строке:
def print_name_by_symbol(name):
    i = 0
    # Такая проверка будет выполняться до конца строки,
    # включая последний символ. Его индекс `length - 1`.
    while i < len(name):
        # Обращаемся к символу по индексу
        print(name[i])
        i = i + 1

name = 'Arya'
print_name_by_symbol(name)
# => 'A'
# => 'r'
# => 'y'
# => 'a'


# пример кода, который печатает буквы каждого слова на отдельной строке в обратном порядке:
def print_reversed_word_by_symbol(name):
    i = len(name)-1
    while i >= 0:
        print(name[i])
        i = i - 1

name = 'Arya'
print_reversed_word_by_symbol(name)


# 66 Условия внутри тела цикла

#функция, которая считает, сколько раз входит буква в предложение, без учета регистра .
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].upper() == char.upper():
            # Считаем только подходящие символы
            count = count + 1
        # Счетчик увеличивается в любом случае
        index = index + 1
    return count

print(count_chars('HexlEt', 'e'))  # 2
print(count_chars('HexlEt', 'E'))  # 2


# 67 Формирование строк в циклах

# Переворот строки - велосипед
def reverse_string(string):
    index = len(string) - 1
    reversed_string = ''

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        # То же самое через интерполяцию
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1

    return reversed_string

print(reverse_string('Game Of Thrones'))  # 'senorhT fO emaG'
# Проверка нейтрального элемента
print(reverse_string(''))  # ''

# Реализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины. Она принимает на вход два аргумента: строку и длину, и возвращает подстроку, начиная с первого символа:
def my_substr(string, length):
    i = 0
    substr = ''
    while i < length:
        substr = substr + string[i]
        i = i + 1
    return substr


string = 'If I look back I am lost'
print(my_substr(string, 1)) # => 'I'
print(my_substr(string, 7)) # => 'If I lo'


# 68 Пограничные случаи (заходит тестировщик в бар..)

# Реализуйте функцию-предикат is_arguments_for_substr_correct(), которая принимает три аргумента:
#
# строку;
# индекс, с которого начинать извлечение;
# длину извлекаемой подстроки.
# Функция возвращает False, если хотя бы одно из условий истинно:
#
# Отрицательная длина извлекаемой подстроки.
# Отрицательный заданный индекс.
# Заданный индекс выходит за границу всей строки.
# Длина подстроки в сумме с заданным индексом выходит за границу всей строки.
# В ином случае функция возвращает True.
#
# Не забывайте, что индексы начинаются с 0, поэтому индекс последнего элемента — это «длина строки минус 1».
#
def is_arguments_for_substr_correct(string, index, length):
    result = True
    if length < 0 or index < 0 or index >= len(string) or index + length > len(string):
        result = False

    return result

# Пример вызова:
#
string = 'Sansa Stark'
end = len(string) - 1
print(is_arguments_for_substr_correct(string, 2, -3))   # => False
print(is_arguments_for_substr_correct(string, -1, 3))   # => False
print(is_arguments_for_substr_correct(string, 4, 100))  # => False
print(is_arguments_for_substr_correct(string, 10, 10))  # => False
print(is_arguments_for_substr_correct(string, 11, 1))   # => False
print(is_arguments_for_substr_correct(string, 3, 3))    # => True
print(is_arguments_for_substr_correct(string, 0, 5))    # => True
print(is_arguments_for_substr_correct(string, end, 1))


# 69 Синтаксический сахар

# a = a + 1 → a += 1
# a = a - 1 → a -= 1
# a = a * 2 → a *= 2
# a = a / 1 → a /= 1

# принимающую на вход строку и символ, и возвращающую новую строку, в которой удален переданный символ во всех его позициях.
def filter_string(string, char):
    result = ''
    i = 0
    while i < len(string):
        if string[i] != char:
            result += string[i]
        i += 1
    return result

text = 'If I look back I am lost'
print(filter_string(text, 'I'))  # 'f  look back  am lost'
print(filter_string(text, 'o'))  # 'If I lk back I am lst'


# 70 Возврат из циклов

# поиск простого числа, выходим из цикла, если в процессе перебора смогли поделить без остатка (значит это не простое числа, которое делится на только 1 и на себя)
def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:    # нет смысла проверять вторую половину числа, там в любому случае будет 0 целых Х десятых
        if number % divider == 0:
            return False

        divider += 1

    return True

print(is_prime(1))  # => False
print(is_prime(2))  # => True
print(is_prime(3))  # => True
print(is_prime(4))  # => False

# Реализуйте функцию is_contains_char(), которая проверяет с учётом регистра, содержит ли строка указанную букву. Функция принимает два параметра:
# Строка
# Буква для поиска

def is_contains_char(text, char):
    i = 0
    while i < len(text):
        if text[i] == char:
            return True
        i += 1

    return False

print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => False
print(is_contains_char('Awesomeness', 'm'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False


# 71 Цикл For

# Например, если мы хотим перебрать символы в строке, то компьютер сам может понять, когда строка заканчивается.
# Для таких ситуаций в Python ввели цикл for. Он сам знает, когда нужно остановиться, так как работает только с коллекциями — наборами элементов, которые нужно перебрать.

# В коде выше for проходит по каждому символу в строке, записывает его в переменную symbol и вызывает внутренний блок кода, где эта переменная используется.
# Имя этой переменной может быть любым.
# Общая структура цикла for выглядит так: for <переменная> in <коллекция>.
text = 'code'
for symbol in text:
    print(symbol)


# Посмотрим, как реализовать функцию переворота строки через цикл for:
def reverse_string(text):
    # Начальное значение
    result = ''
    # char - переменная, в которую записывается текущий символ
    for char in text:
        # Соединяем в обратном порядке
        result = char + result
    # Цикл заканчивается, когда пройдена вся строка
    return result


print(reverse_string('go!'))  # => '!og'


# Теперь посчитаем количество упоминаний символа в строке без учета регистра:
# text - произвольный текст
# char - символ, который нужно учитывать
def chars_count(text, char):
    # Так как ищем сумму, то начальное значение 0
    result = 0
    for current_char in text:
        # приводим все к нижнему регистру,
        # чтобы не зависеть от текущего регистра
        if current_char.lower() == char.lower():
            result += 1
    return result

# chars_count('hexlet!', 'e')  # 2
# chars_count('hExlet!', 'e')  # 2
# chars_count('hExlet!', 'E')  # 2
# chars_count('hexlet!', 'a')  # 0

# принимает на вход строку и символ и возвращает новую строку, в которой удалён переданный символ во всех его позициях.
def filter_string(text, char):
    result = ''
    for i in text:
        if i.lower() != char.lower():
            result += i
    return result

text = 'If I look forward I win'
print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win'


# 72 Цикл for и функция range

# Функция range в Python является встроенной функцией, которая создает последовательность чисел внутри определенного диапазона. Ее можно использовать в цикле for для контроля количества итераций.

# У range() есть несколько вариантов использования:

# range(stop) создает последовательность от 0 до stop - 1
sum = 0
for i in range(10):
    sum += i
print(sum) # => 45

# range(start, stop) создает последовательность от start до stop - 1
for i in range(1, 4):
    print(i)
# => 1
# => 2
# => 3

# range(start, stop, step) создает последовательность из чисел от start до stop - 1, с шагом step
for i in range(3, 0, -1):
    print(i)
# => 3
# => 2
# => 1


# Реализуйте функцию print_table_of_squares(from, to), которая печатает на экран квадраты чисел. Она первое from и последнее to число печатает строку square of <число> is <результат>
def print_table_of_squares(fr, to):
     for i in range(fr, to + 1):
         print(f'square of {i} is {pow(i, 2)}')

print_table_of_squares(1, 3)
# # => square of 1 is 1
# # => square of 2 is 4
# # => square of 3 is 9