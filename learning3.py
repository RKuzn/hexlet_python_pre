#https://www.youtube.com/watch?v=cEeY0opsVMw
#2 main data structure  - series (1-dim vertical array) and data frame (2-dim array like table)
import numpy as np
import  pandas as pd

#make series from list object
lst = ["Pandas", "Matplotlib", "Numpy"]
s = pd.Series(lst)
print(s, type(s))   #0 Pandas    1 Matplotlib   2 Numpy     object <class 'pandas.core.series.Series'>

#another way + custom index
s = pd.Series([2, np.nan, 7, -3, 0], index = ['a','b','c','d','e'])
print(s)
print(s.index, type(s.index))   #Index(['a', 'b', 'c', 'd', 'e'], dtype='object')    <class 'pandas.core.indexes.base.Index'>

#series from dictionary, keys = indexes, values = values
dct = {'q':1, 'p':2, 'r':3, 'f':0.25}
s = pd.Series(dct)
print(s)
print(s[0])         #1.0
print(s[1:3])       #p    2.0     r    3.0
print(s[s <= 1])    #q    1.00    f    0.25
print(s[(s >= 1) & (s < 3)])    #q    1.0   p    2.0
print(s['p'])         #2.0
print(s[['p', 'f']])         #p    2.00     f    0.25
print(s[[1,3]])              #p    2.00     f    0.25

#add item
s['rrr'] = 1000
print(s)

#drop item - label, index, axis, etc
s2 = s.drop(labels=['p', 'rrr'])
print(s2)

#astype приводит все значения в серии к заданному типу
s3 = s.astype(np.int16)
print(s3)

#read and save csv
#s = pd.read_csv("filename.csv", nrows=1)
#s.to_csv('filename.csv')


#Dataframe - 2 dim array
data = [[4,7,10], [5,8,11], [6,9,12]]
print(data, type(data))     #[[4, 7, 10], [5, 8, 11], [6, 9, 12]] <class 'list'>
df = pd.DataFrame(data)
print(df)
#   0  1   2
#0  4  7  10
#1  5  8  11
#2  6  9  12

#прописываем индексы для строк и столбцов
df = pd.DataFrame(data, index = ['a','b','c'], columns=['x','y','z'])
print(df)
#   x  y   z
#a  4  7  10
#b  5  8  11
#c  6  9  12

#df from dict, keys become columns
dct = {'name':['ivan', 'gosha', 'masha'],
       'age':[27, 32, 45]}
df = pd.DataFrame(dct)
print(df)
#    name  age
#0   ivan   27
#1  gosha   32
#2  masha   45

df.info()   #типы столбцов + размер памяти под df
print(df['name'].nunique(), df['name'].unique())    #3      ['ivan' 'gosha' 'masha'] - уник. значения в столбце
df2 = df['name'].apply(lambda x: x.upper())     #для всех значений в стоблце поднимаем регистр
print(df2)

#выборки
df = pd.DataFrame(
    {'name':['ivan', 'gosha', 'masha'],
     'age':[27, 32, 45],
     'country':['kz','ru','bel']})
print(df['age'], type(df['age']))        # можно и проще - print(df.age)    <class 'pandas.core.series.Series'>
print(df[['name', 'age']], type(df[['name', 'age']]))   #подвыборка столбцов <class 'pandas.core.frame.DataFrame'>

#print(df.loc['row_label_name'])    #доступ к строке по метке строки, если она задана была, обычно это просто числа, тогда iloc
print(df.iloc[0])   #доступ по индексу строки
#name       ivan
#age          27
#country      kz

#фильтрация
print(df[df['age']>30][['name', 'age']])    #фильтрует и возвращает только указанные столбцы

#добавление столбца
df['new_age'] = df.age * 2
df['new_col'] = [50,30,70]
print(df)
#    name  age country  new_age  new_col
#0   ivan   27      kz       54       50
#1  gosha   32      ru       64       30
#2  masha   45     bel       90       70

print(df.age.mean())    #среднее значение по столбцу 34.66

#объединения
df2 = df.append(df)   #добавляет строки в конец
print(df2)

df3 = pd.concat([df, df], axis=1)   #дописывает колонки в конец, строк должно быть одинаково
print(df3)
