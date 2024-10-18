#https://www.youtube.com/watch?v=tsTDujlI9GQ&t=383s

#целочисленное деление
print(10//4)    #2

#остаток от деления
print(10%3)     #1

#степень
print(4**3)     #64

#проверка типа объекта  type(_var)
li = []
print(type(li))     #<class 'list'>
print(type(3/2))    #<class 'float'>

#increment/decrement
i = 10
i =+ 1    #11
i -= 2    #9
i *= 2    #18
i /= 3    #6

#кавычки можно одинарные, можно двойные, разницы нет. Если внутри надо, то реверс (одинарные внутри двойных или наоборот)
s = 'Мальчик, ты "баклажан"'
print(s)    #Мальчик, ты "баклажан"
s = "Мальчик, ты 'баклажан'"
print(s)    #Мальчик, ты 'баклажан'

#экранирование, кавычка в кавычке, перенос строки
s = 'boy\'s eggpalnt. \nit\'s a new line'
print(s)    #boy's eggpalnt.
            #it's a new line

#перенос текста на несколько строк - ставим 3 одинарные кавычки в первой строке и еще 3 закрывающие в конце. Удобнее, чем много \n
s = '''Oh boy,
    you're
    an "eggplant"'''
print(s)

#строка - массив символов, индексация от 0
s = 'qwerty'
    #012345
print(s[0])     #q      первый символ
print(s[-1])    #y      последний - обратный порядок, индексация с -1     это аналогично s[len(s)-1]
print(s[-2])    #t      предпоследний
print(s[1:4])   #wer    то, что между индексами 1 и 4 (4 уже не входит)
print(s[:4])    #qwer   с самого начала по 4
print(s[-3:])   #rty    последние 3 символа
print(s[4:])    #ty     с 4-го до конца
print(s[2:-2])  #er     с 2-го до предпоследнего
print(len(s))   #6

#lists (changable)
a = [1,2,3,4,5]
print(len(a))   #5
print(type(a[1]))       #<class 'int'>  2
print(type(a[1:3]))     #<class 'list'>    [2,3]
print(5 in a)    #True проверка на вхождение в список

#change list content
a[1] = 10
print(a[1]) #10

a[:2] = [11,22,33]  #первые 2 элемента заменим на 3 новых
a.append(44)        #добавим в конец списка новый элемент
a.insert(0, 6)      #вставляет на нулевой индекс число 6, остальные сдвигаются
print(a)    #[6, 11, 22, 33, 3, 4, 5, 44]
a += [3, 4]    #добавляем новый список в конец
print(a)    #[6, 11, 22, 33, 3, 4, 5, 44, 3, 4]
a.pop()     #удаляет последний элемент
a.pop(3)     #удаляет индекс=3 элемент элемент
print(a)    #[6, 11, 22, 3, 4, 5, 44, 3]

#tuples (unchangable)
tpl = (5,6,7)
print(tpl)
print(type(tpl))    #<class 'tuple'>
print(tpl[2])   #7
#tpl[2] = 10     #TypeError: 'tuple' object does not support item assignment
print(5 in tpl)    #True проверка на вхождение в тупл
a += tpl    #тупл можно дописать в лист
print(a)    #[6, 11, 22, 3, 4, 5, 44, 3, 5, 6, 7]



#dict   (keys are uniq; changable)
dct = {'key' : 'value'}
print(type(dct))        #<class 'dict'>
dct['key2'] = 'eggs'    #add new key and value
print(dct)              #{'key': 'value', 'key2': 'eggs'}
print(dct.keys())       #dict_keys(['key', 'key2'])
print(dct.values())     #dict_values(['value', 'eggs'])
print(dct.items())      #dict_items([('key', 'value'), ('key2', 'eggs')])
print('key2' in dct)    #True проверка на вхождение ключа в словарь
dct['key'] = dct['key'] + '_ver2'
print(dct['key'])       #value_ver2
print(type({}))         #<class 'dict'>     пустой дикт

#Set (в отчиличе от словаря, множество содержит только значения, без ключей. Хм, а от списка тогда это чем отличается?
st = {1,2,3}
print(type(st))         #<class 'set'>
print(type(set()))      #<class 'set'>      пустой сет
st.add(4)
print(st)               #{1, 2, 3, 4}
print(4 in st)          #True проверка на вхождение значения в set

#можно добавить множество в список, это будет ссылка, когда сет поменяется, список тоже отразит изменение
a.append(st)
print(a)    #[6, 11, 22, 3, 4, 5, 44, 3, 5, 6, 7, {1, 2, 3, 4}]
st.add(5)
print(a)    #[6, 11, 22, 3, 4, 5, 44, 3, 5, 6, 7, {1, 2, 3, 4, 5}]
#наоборот тоже работает, можно менять сет через список
a[-1].add(6)
print(a)    #[6, 11, 22, 3, 4, 5, 44, 3, 5, 6, 7, {1, 2, 3, 4, 5, 6}]
print(st)   #{1, 2, 3, 4, 5, 6}

#string format
print('our list %s' %a)     #our list [6, 11, 22, 3, 4, 5, 44, 3, 5, 6, 7, {1, 2, 3, 4, 5, 6}]
print('s1 %s, s2 %s' % (42, 'some text'))   #s1 42, s2 some text
print('s1 %s, s2 %r' % (42, 'some text'))   #s1 42, s2 'some text'
print('our set: {}'.format(st))     #our set: {1, 2, 3, 4, 5, 6}
print('{}{}'.format(10,20))     #1020
print('{1} and {0} and {1} again'.format('crisps', 'fish'))   #fish and crisps and fish again
print('{val}{val2} {val3}'.format(val='on',val2='ly',val3='you'))   #only you
print('value: %.2f' % 12.377)               #value: 12.38
print('value: {:.2f}'.format(12.377))       #value: 12.38
print(f'array {a}, fl {12.377:.2f}')     #array [6, 11, 22, 3, 4, 5, 44, 3, 5, 6, 7, {1, 2, 3, 4, 5, 6}], fl 12.38

#lists in list (двумерных массивов нет)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)   #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])            #[4, 5, 6]
print(matrix[1][2])         #6


#ifthen
a=6
b=7
if a>b:
    print(a)
elif a==0:
    print(a*2)
else:
    print(b)    #7

#tern
print(a) if a>b else print(b)   #7