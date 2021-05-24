# -*- coding: utf-8 -*-
# %% 117
x = -1.5
expression = 'x**2 + x'
print(eval(expression))
# %% 118
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

print(isinstance(var1, tuple))
print(isinstance(var2, tuple))
print(isinstance(var3, tuple))
print(isinstance(var4, tuple))
print(isinstance(var5, tuple))

# %% 119

characters = ['k', 'b', 'c', 'j', 'z', 'w']
print(f'Pierwsza: {min(characters)}\nDruga: {min(characters)}')

# mozna tez tak
print(f'Pierwsza: {min(characters)}')
print(f'Ostatnia: {max(characters)}')
# %% 120
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

x = zip(ticker, full_name)
print(list(x))
# %% 121
items = (' ', '0', 0.1, True)


print(all(items))
# %% 122
items = ('', 0.0, 0, False)

print(any(items))

# %% 123
number = 234
x = bin(number)
x = x[2:]
print(x.count('1'))
# %% 124 
def maximum(x, y):
    if x >= y:
        return x
    else:
        return y
    
maximum(7, 6)  
# %% 125

def maximum(x, y, z):
    if x >= y and x >= z:
        print(x)
    else:
        if y >= x and y >= z:
            print(y)
        else:
            print(z)
maximum(4, 2, 1)
maximum(-3, 2, 5)        


# %% 126
def multi(numbers):
    wynik = 1
    for number in numbers:
        wynik *= number
    return wynik


numbers = [-4, 5, 2]
multi(numbers)
### istotne mnozenie zawartosci listy  / tupli, nie bylo wczesniej
# %% 127
words = ['python', 'sql']
def map_longest(words):
    dl = []
    for word in words:
        dl.append(len(word))
    return max(dl)
 # %%   
map_longest(words)


# %% 128
lista = ['programowanie', 'python', 'java', 'sql']
lista = ['java','swl']
def filter_ge_6(lista):
    dl = []
    for i in lista:
        if len(i) > 5:
            dl.append(i)
    print(dl) 

filter_ge_6(lista)   
# %% 129    
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n -1)   




# %% mozna tez tak

def factoial(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

# %% 130

def co unt_str(words):
       total = 0
       for item in words:
           if isinstance(item, str):
            total += 1
            return total
    
# %% 131       
fiufiu = [1, '#hello', 'python', 'gsadsado'] 
def count_str(fiufiu):
    tal = 0
    for item in fiufiu:
        if isinstance(item, str) and len(item) > 2:
            tal += 1
    return tal
    
    
  
count_str(fiufiu)    
    
# %% 132
words = [1, 5, 3, 2, 2, 4, 2, 4, 'er', 'er', 'w']
def remove_duplicates(words):
    l = []
    for i in words:
        if i not in l:
            l.append(i)
    return l    


# %% mozna bylo prosciej

def remove_duplicates(items):
    return list(set(items))
# %% 133
items = [1, 2, 3, 4]
def is_distinct(items, w = []):
    
    for i in items:
        if i not in w:
            w.append(i)
        else:
            return False
    return True        
## monza bylo proscieji znacznie lepiej

def is_distinct(items):
    return len(items) == len(set(items))
# %% 134
def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)


#%%
function(3)
function(5, ['a', 'b', 'c'])
function(6)
### wazne !!!

def function(idx, l=None):
    if l is None:
        l = []
    for i in range(idx):
        l.append(i ** 3)
    print(l)
### wazne !!!    
# %% 135 
def function(*args, **kwargs):
    print(args, kwargs)
#%%    
function(3, 4)    
function(x=3, y=4)
function(1, 2, x=3, y=4)
# %% 136
def is_palindrome(x):
    if x[0:] == x[::-1]:
        return True
    else:
        return False


### mozna tez inaczej
def is_palindrome(string):
    inverse = string[::-1]
    return True if string == inverse else False

# %% 137
stocks = ['playway', 'boombit', 'cd projekt']
def change(stocks):
    return [len(i) for i in stocks]


change(stocks)

## mozna tez inaczej

stocks = ['playway', 'boombit', 'cd projekt']
length = list(map(lambda stock: len(stock), stocks))
print(length)


# %% 138
items = [(1, 7), (1, 3), (4, 1), (4, 2), (0, 7), (1, 1), (4, 0), (1, 2)]
def sort_list(items):
    return sorted(items, key=lambda item: item[1])



# %% 139 
lambda x, y : x + y + 2

### czemu nie w jednej linijca?
func_2 = lambda x, y: x + y +2

# %% 140
items = [(3, 4), (2, 5), (1, 4), (6, 1)]
items.sort(key=lambda item: item[0]**2 + item[1]**2)
print(items)




### ja zrobilem tak i tez wyszlo
def sortowanko(items):
    return sorted(items, key=lambda item: (item[0]**2) + (item[1]** 2) )


print(sortowanko(items))
# %% 141
stocks = [{'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}]


stocks.sort(key=lambda i: i['price'])
print(stocks)

# %% 142 FILTER
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]
def sortowank0(stocks):
    l = []
    for i in stocks:
        if i['indeks'] == 'mWIG40':
           l.append(i)
    print(l)     
sortowank0(stocks)
### mozna bylo znacznie szybciej dzieki funkcji FILTER

print(list(filter(lambda item: item['indeks'] == 'mWIG40', stocks)))

# %% 143

def so(stocks):
    l =[]
    for i in stocks:
        if i['indeks'] == 'mWIG40':
            l.append(True)
        else:
            l.append(False)
    print(l)        
                    

so(stocks)
# %% mozna bylo z funkca MAP, zwraca wartosc bool
print(list(map(lambda x: x['indeks'] == 'mWIG40', stocks)))


# %% 144
items = ['P-1', 'R-2', 'D-4', 'F-6']
l = []
for i in items:
    i[1] == ''
    l.append(i)
print(l)    
# %%
print(list(map(lambda i: i.replace('-', ''), items)))

# %% 145

num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

print(list(map(lambda i, x: i % x, num1, num2)))





# %% 146



fnames = ['sfsf.txt', 'sfgsdfg.txt']


def file_gen(fnames):
    for fname in fnames:
        if fname.endswith('.txt'):
            yield fname




print(file_gen(fnames))
# %% 

def liczby():
    for i in range(11):
        yield i * 2

for parzysta in liczby():
    print(parzysta)

# %% 147
def enum(items):
    idx = 0
    for item in items:
        yield (idx, item)
        idx += 1

    
# %% 148 

def dayname(bzium):
    days = ['pon', 'wt', 'sr', 'czw', 'pt' ,'sb', 'nd']
    yield days[bzium - 1]
    yield days[bzium]
    yield days[(bzium +1)]

# %% 149
dice = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6] 

def rzut():
    l = []
        for i, x in dice1, dice2:
            i + x
    
print(l)    
# %%
omega = {(i, j, k, l, m) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7) for l in range(1, 7) for m in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] + pair[2] + pair[3] +pair[4] > 26}
print(f'P-stwo: {len(sum_gt_10) / len(omega)}')



omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}
print(f'P-stwo: {len(sum_gt_10) / len(omega):.2f}')



# %% 150 METODA SPLIT, ze stringow tworzy LISTY
desc = "Playway: Playway to producent gier komputerowych."
bzium = desc.lower().replace(':', '').replace('.', '').split()
bzium2 = {i for i in bzium}
print(len(bzium2))
# %% 151 
omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0]** 2 + pair[1]** 2 >= 45}
print(f'P-stwo: {len(sum_gt_10) / len(omega):.2f}')

### mozna tez w ten sposob

omega = {(x, y) for x in range(1, 7) for y in range(1, 7)}
a = {(x, y) for x, y in omega if x**2 + y**2 >= 45}
prob = round(len(a) / len(omega), 2)
print(f'P-stwo: {prob}')

# %% 152
omega = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
sum_gt_10 = {(x, y, z) for x, y, z in omega if (x + y + z) % 7 == 0}
print(f'P-stwo: {len(sum_gt_10) / len(omega):.2f}')

# %% 153
omega = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
sum_gt_10 = {(x, y, z) for x, y, z in omega if (x + y + z) % 2 != 0}
print(f'P-stwo: {len(sum_gt_10) / len(omega):.2f}')

# %% 154
omega = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
sum_gt_10 = {(x, y, z) for x, y, z in omega if x % 2 != 0 if y % 2 != 0 if z % 2 != 0}
print(f'P-stwo: {len(sum_gt_10) / len(omega):.3f}')

# %% 155

with open('gaming.txt','r') as file:
    text = file.readlines()


text = [line.replace('\n', '') for line in text]
text = [line for line in text if len(line) > 0]
print(text)

# %% 156 ROUND DO ZAOKRAGLANIA
tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]
price = [round(x + (x * tax), 2) for x in net_price]
print(price)
# #
for x in net_price:
    l = []
    l.append(x +(x * tax))
    print(l)

###
tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]
gross_price = [round(price * (1 + tax), 2) for price in net_price]
print(gross_price)


# %% 157 WZOR NA INWESTYCJE

pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

final = [round(pv *(1 + i)** n, 2) for i in rate]
print(final)

x = pv *(1 + 0.01) ** n
print(x)
# %% 158 
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
final = [round((pv *(1 + i)** n) -pv, 2) for i in rate]

## monza tez tak
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
fvs = [pv * (1 + r)**n for r in rate]
interest = [round(fv - pv, 2) for fv in fvs]
print(interest)

# %% 159

lines = [line for line in lines if len(line) > 0]
lines = [line.split() for line in lines]
print(lines)
# %% 160

lines = lines.lower()
lines = lines.replace(',', '').replace('.', '')
tokens = lines.split()
tokens = [token for token in tokens if len(token) > 7]
tokens.sort()
print(tokens)

# %% 161
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
data2 = data.items()
data2 = [data2]
print(data2)


### prosciej

wynik = [[key, value] for key, value in data.items() ]
print(wynik)

# %% 162
bzium = {x:x ** 2 for x in range(1, 8)}
print(bzium)


# %% 163

stocks = ['Playway', 'CD Projekt', 'Boombit']
bzium = {x:len(x) for x in stocks}
print(bzium)

# %% 164
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
reverse = {key:value for value, key in stocks.items()}
print(reverse)
reverse = {x:y for x in stocks.values() for y in stocks.keys()}
print(reverse)
x = reversed(stocks)
r


print(stocks.items())
print(stocks.keys())
print(stocks.values())

# %% 165
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
bzium = {x:y for x, y in stocks.items() if y > 100}
print(bzium)
# %% 166
abc = [1, 2, 3]
bzium = [{x:x**1 for x in range(1, 10)}]
bzium2 =[{x:x**2 for x in range(1, 10)}]
bzium3 = [{x:x**3 for x in range(1, 10)}]
cel = bzium + bzium2 + bzium3jh
print(cel)
### znacznie lepiej:
    
data = [{i: i**j for i in range(1, 10)} for j in range(1, 4)]
print(data)

# %% 167 CIEKAWE ITEROWANIE
indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['liczba spółek', 'spółki', 'kapitalizacja']
properties.sort()
stocks = [{x:None for x in properties}]
stocks2 = {x:y for x in indeks for y in stocks}
print(stocks2)
### znacznie lepsza opcja
indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['liczba spółek', 'spółki', 'kapitalizacja']
data = {idx: {i: None for i in properties} for idx in indeks}
print(data)

# %% 168
indeks = ['WIG20', 'mWIG40', 'sWIG80']
data = {key: val for key, val in enumerate(indeks)}
print(data)

# %% 169

import calendar
print(calendar.calendar(2020))
dir(calendar)
print(datetime)

# %% 170
print(calendar.month(2020, 6))

# %% 171
from datetime import date
date1 = date(2020, 6, 1)
date2 = date(2020, 7, 18)
diff = date2 - date1
print(diff)

# %% 172

import re
string = 'Python 3.8'
result = re.findall(pattern=r"\d", string=string)
print(result)


# %% 173
import re


string = '!@#$%^&45wc'
result = re.findall(pattern=r"\w", string=string)
print(result)
# %% 174
import re


raw_text = "Wyślij email na adres: info@template.com lub sales-info@template.it"
result = re.findall(r"[\w\.-]+@[\w\.-]+", raw_text)
print(result)

dir(re)
# %% 175
import re


text = 'Programowanie w języku Python - od A do Z'
result = re.split(pattern=r"\s+", string=text)

# %% 176
import string

dir(string)

print(string.ascii_letters)
print(string.ascii_uppercase)
# %% 177 ciekawy modul
from collections import Counter


items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']

counter = Counter()
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
for item in items:
    counter[item] += 1
print(counter)
# %% 178

import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))



print(sigmoid(100))
# %% 179
import random


random.seed(10)

items = ['python', 'java', 'sql', 'c++', 'c']
choice = random.choice(items)
print(choice)

# %% 180
import random


random.seed(15)

items = ['python', 'java', 'sql', 'c++', 'c']
items = ['python', 'java', 'sql', 'c++', 'c']
random.shuffle(items)
print(items)
# %% 181

import pickle
ids = ['001', '003', '011']
dir(pickle)

with open('data.pickle', 'wb') as file:
    pickle.dump(ids, file)
# %% 182

import json


stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
dir(json)

stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
result = json.dumps(stocks, sort_keys=True, indent=4)
print(result)
# %% 183
y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]
def accuracy(y_true, y_pred):
    counter = 0
    for i, j in zip(y_true, y_pred):
        if i == j:
            counter += 1
    return round(counter / len(y_true), 4)
 
print(accuracy(y_true, y_pred))
# %% 184
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]
 
def mae(y_true, y_pred):
    return round(sum([abs(i[1] - i[0]) for i in zip(y_true, y_pred)]) / len(y_true), 3)

# %% 185

def mse(y_true, y_pred):
    return round(sum([(i[1] - i[0])**2 for i in zip(y_true, y_pred)]) / len(y_true), 3)   


# %% 186

def relu(x):
    return max(0, x)
#%% 187
def flatten(items):
    result = []
    for item in items:
        result.extend(item)
    return result
# %% 188


def transfer_zeros(items):
    result = []
    counter = 0
    for item in items:
        if item == 0:
            counter += 1
        else:
            result.append(item)
    result.extend([0] * counter)
    return result

# %% 189

def euclidean_distance(x, y):
    squared_diff = [(i - j)**2 for i, j in zip(x, y)]
    return (sum(squared_diff)) ** 0.5

# %% 190

def arange(start, stop, step=1):
    result = []
    for i in range(start, stop, step):
        result.append(i)
    return result
# %% 191

def concat(l1, l2):
    result = []
    for i, j in zip(l1, l2):
        result.append([i[0], j[0]])
    return result

# %% 192
def identity(n):
    array = [[0]*n for i in range(n)]
    for idx, item in enumerate(array):
        item[idx] = 1
    return array
# %% 193
def fill_value(height, width, value):
    return [[value] * width for i in range(height)]
# %% 194
def trace(array):
    total = 0
    for idx, item in enumerate(array):
        total += item[idx]
    return total

# %% 195
def transpose(array):
    width = len(array[0])
    result = []
    
    for i in range(width):
        pair = []
        for item in array:
            pair.append(item[i])
        result.append(pair)
    return result
# %% 196

def max_prob(array):
    result = []
 
    for item in array:
        max_val = max(item)
        for idx, val in enumerate(item):
            if val == max_val:
                result.append([val])
    return result
# %% 197

def detect_class(array):
    result = []
 
    for item in array:
        max_val = max(item)
        empty = [0] * len(item)
        for idx, val in enumerate(item):
            if val == max_val:
                empty[idx] = 1
                result.append(empty)
    return result
# %% 198
def dot_product(vec1, vec2):
    return sum([v * w for v, w in zip(vec1, vec2)])
# %% 199
def count_none(items):
    counter = 0
    for item in items:
        if not item:
            counter += 1
    return counter
# %% 200
def top_n(items, n):
    items.sort(reverse=True)
    return items[:n]































































































































































hgjh


















































































































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
