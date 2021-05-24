# -*- coding: utf-8 -*-
# %% 100


gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}
 
for ticker, info in gaming.items():
    if info[1] == 'PLN':
        continue
    info[0] = info[0] * 4.0
    info[1] = 'PLN'
print(gaming)


# %% 101
names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for i in names:
    if i == None:
        continue
    print(i)
    
# moze tez byc tak

for i in names:
    if i is None:
        continue
    print(i)    
    
# %% 102
counter = 0
number = 2
prime = []
while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1
 
print(','.join(prime))
# wazna liczenie

# %% 103
n = 1
pv = 1000
r = 0.04
fv = pv *(1 + r)

while fv < 2 * pv:
   for i in range(1, n):
       if fv > 2 * pv:
           break
   else:
           n += 1
           continue
print(f'Wartosc przyszła: {fv}. Liczba okresów{n} lat')    

# %%
n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)
 
while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f'Wartość przyszła: {fv:.2f} PLN. Liczba okresów: {n} lat')

# %% 104
max_iters = 10000 
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

max_iters = 10000 
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4
 
while previous_step_size > precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_prev - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1
 
print(f'Minimum lokalne w punkcie: {w_0:.2f}')



# %% 105
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = int((start + end) / 2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
 
if flag:
    print('Znaleziono')
else:
    print('Nie znaleziono')

#  hhmm

# %% 106
suma = 3000
counter = 0
try:
    result = suma / counter
    print(result)
except ZeroDivisionError:
    print('Dzielenie przez zero.')


# %% 107
try:
    with open('file.txt', r) as file:
        content = file.read()
except FileNotFoundError:
print('Nioe znaleziono pliku.')

# %% 108
users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'

try: 
    print(users['users_id'])
except KeyError:
    print('Klucz nie występuje w słowniku. Dodawanie klucza...')

users['004'] = None
print(users)
# tak byoby lepiej, mniej linijek

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'
 
try:
    print(users[user_id])
except KeyError:
    print(f'Klucz {user_id} nie występuje w słowniku. Dodawanie klucza...')
    users[user_id] = None
print(users)

# %% 109

Data,Otwarcie,Najwyzszy,Najnizszy,Zamkniecie,Wolumen
2020-04-01,302,314,300,310,12940
2020-04-02,310,315,305,313,10311
2020-04-03,313,318.5,312,318,12372
# %%
file = open('aa.txt', 'r')
for line in file:
    print(line)
    
x = tuple(file)
print(x)    
# %%    
print(file = open('aa.txt', 'r'))

# %%
with open('playway.txt', 'r') as file:
     lines = file.read().splitlines()
 
close = []
 
for idx, line in enumerate(lines):
    if idx > 0:
        close.append(int(line.split(',')[-2]))
 
close_avg = sum(close) / len(close)
print(f'3-dniowa średnia cena zamknięcia: {close_avg:.2f}')

# %% 110
with open('indeksy.txt', 'r') as file:
    a = file.read().splitlines()
    
lista = []

for i in a:
    if i.startswith('WIG'):
        lista.append(i)

print(lista)
# mozna prosciec

with open('indeksy.txt', 'r') as file:
     lines = file.read().splitlines()
 
indexes = [index for index in lines if index.startswith('WIG')]
print(indexes)
# %% 111
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
   
data = [(line.split(',')[0], line.split(',')[4]) for line in content]
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)]
    }
print(result)
# %% 112
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()


max = [0]
tab = [line.split(',') for line in content]
for i in content:
    if i == str:
        continue
    if i in '-':
        continue
        if i > max:
            max = i
        
print(f'Max Vol:{i}')


# %% 113
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()
 
volumes = [line.split(',')[-1] for line in content][1:]
volumes = [int(vol) for vol in volumes]
max_vol = max(volumes)
print(f'Max Vol: {max_vol}')


# %% 114
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
data = [(val[0], int(val[1])) for val in data]
max_vol = max([val[1] for val in data])
max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]
print(f'Data: {max_date}')




# %% 114
with open('num.txt', 'w') as file:
     for i in range(1, 19):
         if i % 2 == 0:
             print(i, file=file)   
              
              


# mozna tez tak

numbers = list(range(1, 20))
even = [number for number in numbers if number % 2 == 0]
 
with open('num.txt', 'w') as file:
    for num in even:
        file.write(str(num) + '\n')

# %% 115

import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}


with open('stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)

# %% 116
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]


with open('users.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    for user in users:
        file.write(','.join(user) + '\n')

# %% 117

































































































































