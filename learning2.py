#https://www.youtube.com/watch?v=QywRrUSryVM

#case emulation
a = 42
if a < 0:
    print('a<0')
elif a < 10:
    print('a<10')
elif a < 100:
    print('a<100')
else:
    print('a>=100')

#for in list
l = [0,1,2,3,4]
for item in l:
    print(item)

#for in set (order by hash value)
for s in {5,6,1,3,7,60,20,10}:
    print(s)

#for in dict
dct = {'key3':'value3', 'key2':'value2', 4:5}
for k in dct:
    print(k, dct[k])

for v in dct.values():  #return only values of dict in list
    print(v)

#for inside string
for c in 'abcdef':
    print(c, end=' ')   #a b c d e f    end=' ' позволяет в одну строку выводить распечатку, по дефолту идет новая строка в качестве разделителя


#join - метод класса string, конкатенация
s = ''
l = ['la','-','la']
s = s.join(l)
print(s)    #la-la
print(' '.join(l))  #la - la    #первый символ ' ' - это разделитель
print(', '.join(l))  #la, -, la


#comprehantions - создание списка/сета/дикта циклом внутри, типа более эффективно по памяти
l = [str(val) + 'comp' for val in dct.values()]     #для каждого val в цикле делается инструкция в начале (перед for) и все это становится списком
print(l)    #['value3comp', 'value2comp', '5comp']

st = {val ** 2 for val in [1,2,3,4]}
print(st)   #{16, 1, 4, 9}

dct = {val : val ** 2 for val in [1,2,3,4]}
print(dct)  #{1: 1, 2: 4, 3: 9, 4: 16}

#цикл по каждому второму элементу (начиная с 1, т.е. 1, потом 3, потом 5 итд)
line = 'python'
print(line[::2])    #pto
print(type(line))   #<class 'str'>

values = [1,2,3,4,5]
print(values[::3])  #[1, 4]
print(values[::-1])  #[5, 4, 3, 2, 1]   #reverse list

#список через range
lst = list(range(10))
print(lst)      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10, 30, 5)))      #[10, 15, 20, 25]    от 10 включительно до 30 не включительно с шагом 5

#цикл через range
for i in (range(5)):
    print(i)

#цикл по списку
for i in (range(len(lst))):
    print(i, lst[i])


#распаковка тупла/списка = присваивание содержимого списока сразу нескольким переменным в одной строке
t = (16, 42)
a, b = t
print(a, b)     #16 42

#enumerate
print(values)           #[1, 2, 3, 4, 5]
e = enumerate(values)
print(e)                #<enumerate object at 0x0000026C3182B5C0>
print(next(e))          #(0, 1)     --индкс = 0, значение из values 1
print(next(e))          #(1, 2)     --индкс = 0, значение из values 1
print(list(e))          #[(2, 3), (3, 4), (4, 5)]  - выводит все, что осталось, итерация только 1 раз

#распаковка + enumerate в цикле - присваивает в i индекс из енума, а в val - значение
for i, val in enumerate(values):        #можно задать с какого элемента начинать enumerate(values, 3)
    print(i, val, end='  ')     #0 1  1 2  2 3  3 4  4 5


#break the cycle
for i in range(10, 100, 5):
    print(i)
    if i == 50:
        break
else:   #сюда заходит после конца цикла; когда break, в этот блок не заходит
    print('else section!')

#break in while cycle
while True:
    print('once')
    break

#continue - завершает текущую итерацию цикла, не доходя до конца, переход на следующую итерация
for i in range(1,8):
    print(i, end=' ')
    if i%2 == 0:
        print('is even')
        continue
        print('never printed')
    print('is odd') #сюда дойдет тоже только если число нечетное, но проще через else конечно, но тут смотрим на continue


#functions
def some_function():
    pass    #do nothing, return None

some_function()
print(type(some_function()))    #<class 'NoneType'>

def some_function():
    print('hello')
    return len('hello')
print(some_function())     #hello   5

#возвращаем тупл, распаковка в переменные
def func():
    return (43, 'text')
a,b = func()
print(a, b)     #43 text
t = func()
print(t, type(t))   #(43, 'text') <class 'tuple'>

#generator function - yield instead of return, возвращается одноразовый генератор
def gen():
    for i in range(3):
        yield i
g = gen()
print(next(g))  #0
print(next(g))  #1

#fibonacci function , default to 5
def fib(n=5):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
print(fib(100))     #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


#fibonacci recursion function - вычисляет фибу для определенного индекса, через рекурсию функция вызывает саму себя
def recur_fib(i):
    if i <= 1:
        return i
    return recur_fib(i-1) + recur_fib(i -2)
print(recur_fib(10))    #55


#map, reduce and generators
print(values)                           #[1, 2, 3, 4, 5]
mapped = map(lambda x: x + 3, values)   #возвращает генератор, содержащий последовательность, в которой каждый элемент увеличили на 3
print(mapped, type(mapped))             #<map object at 0x0000023F2CD3B2E0> <class 'map'>
print(list(mapped))                     #[4, 5, 6, 7, 8]

#filter
nums = range(-10, 20, 3)
print(list(filter(lambda x: -7 < x < 10, nums)))    #[-4, -1, 2, 5, 8]

#reduce
from functools import reduce
to_mul = range(1,7)
product = reduce(lambda x,y: x*y, to_mul)
print(product, type(product))   #720 <class 'int'>

#decorator - декоратор, механика изменения существующей функции, не переписываея ее, а навешивая доп.поведение во внешней функции-декораторе
#тогда при вызове изначальной фукнции, ее поведение меняется, при том что ее код не менялся, а применился код из декоратора