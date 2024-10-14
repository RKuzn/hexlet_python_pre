# if
def guess_number(number):
    if number == 42:
        return 'You win!'
    return 'Try again!'

print(guess_number(42)) # You win!
print(guess_number(61)) # Try again!

# if-else
# Реализуйте функцию normalize_url(), которая выполняет нормализацию данных. Она принимает адрес сайта и возвращает его с https:// в начале.
def normalize_url(url):
    if url[:7] == 'http://':
        return f'https://{url[7:]}'
    else:
        if url[:8] == 'https://':
            return url
        else:
            return f'https://{url}'

print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
print(normalize_url('google.com'))     # => 'https://google.com'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'


# elif — «если не выполнено предыдущее условие, но выполнено текущее»
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'



def who_is_this_house_to_starks(family):
    if family == 'Karstark' or family == 'Tully':
        return 'friend'
    elif family == 'Lannister' or family == 'Frey':
        return 'enemy'
    else:
        return 'neutral'

print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral'


# Тернарный оператор
# конструкция, которая работает как if-else, но считается выражением. Единственный оператор в Python, который требует три операнда:
# Общий паттерн выглядит так: <expression on true> if <predicate> else <expression on false>. Т.е. сначала тру, потом условие посерединке, потом фалсе.
# И это отличается от скуля, где сначала условие, потом 1, потом 0 (

def abs(number):
    return number if number >= 0 else -number

# две версии фукнции - через if и через тернарный
def flip_flop(coin):
    if coin == 'flip':
        return 'flop'
    return 'flip'

print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'

def flip_flop(coin):
    return 'flop' if coin == 'flip' else 'flip'

print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'


# Оператор Match (Python 3.10+)

def count_items(count):
    # Объявляем переменную
    result = ''

    # Заполняем
    match count:
        case 1:
            result = 'one'
        case 2:
            result = 'two'
        case _:
            result = None

    # Возвращаем
    return result

# или так
def count_items(count):
    match count:
        case 1: #соответствует if
            return 'one'
        case 2:
            return 'two'
        case _: #соответствует ветке else. Как и else, указывать case _ необязательно
            return None

# Реализуйте функцию get_number_explanation(), которая принимает на вход число и возвращает объяснение этого числа.
def get_number_explanation(number):
    result = 'just a number'
    match number:
        case 666:
            result = 'devil number'
        case 42:
            result = 'answer for everything'
        case 7:
            result = 'prime number'

    return result

print(get_number_explanation(8))  # just a number
print(get_number_explanation(666))  # devil number
print(get_number_explanation(42))  # answer for everything
print(get_number_explanation(7))  # prime number

# или так
def get_number_explanation(number):
    match number:
        case 666:
            return 'devil number'
        case 7:
            return 'prime number'
        case 42:
            return 'answer for everything'
        case _:
            return 'just a number'