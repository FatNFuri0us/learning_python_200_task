# -*- coding: utf-8 -*-

# 1

print('Ucz się Pythona!')

# 2

age = 20
print('mam {age} lat')

print(age)
print('Mam', age, 'lat.')


# corect answer: print(f'Mam {age} lat.')

# 3

a = 'Python'
b = '3.8'
print(f'Uczę się języka {a} w wersji  {b}')

# %% 4 
price = 199.99
print('Towar kosztuje', price)

# %% 5

price = 69.99
print(f'Tower kosztuje {price}')

#%% 6

price = 34.99
wage = 10 
print(f'Cena: {price} PLN. Waga: {wage} kg')
# %% 7
# poniżej zdefiniowane jest przybliżenie liczby pi
pi = 3.1415926535

# używając formatowania f-string wydrukuj przybliżenie
# liczby pi do drugiego miejsca po przecinku
# %%
print(f'Przybliżenie liczby pi: {pi:.2f}')
print(f'{pi: 2.4f}')

# %% 8
x = '-'
w = 'WERSJA 1.0.1'
print(x * 40)
print(w)
print(x * 40)
print(f'{x * 40} {w} {x * 40}')

print('-' * 40)
print('WERSJA: 1.0.1')
print('-' * 40)

# %% 9
print('=' * 40)
print('autor: jannowak@poczta.com')
print('data: 01-01-2021')
print('=' * 40)

# %% 10
print('summer#time#holiday')
print('summer', 'time', 'holiday', sep='#')

# %% 11
r = 5
pi = 3.14
P = pi*r**2
print(f'Pole koła wynosi {P} cm2')

# %% 12
r = 0.03
kwota = 1000
n = 5

x = kwota * (1 + r)**n 
print('Wartość końcowa inwestycji wynosi: ', str(x)[:7],'PLN')

# %% 13

a = 3 
b = 4 
c = 1

delta = b ** 2 - 4 * (a * c)
print(f'Delta wynosi: {delta}')

# %% 14
g = 4
a = 10
PW = a + g
OW = a + 10 * g
Suma = ((PW + OW) / 2) * 10
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {Suma}')
 

# niby dobrze, ale powinno byc:
    
a1 = 14
a10 = 50
n = 10
s10 = ((a1 + a10) / 2) * n    
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {Suma}')

# %% 15
a1 = 40
q = 2
S = a1 * ((1 - 2**6) / (1 - 6))
print(f'Suma pierwszych 6 wyrazów ciągu wynosi: {S}')

# zle, powinno byc 

a1 = 8
a2 = 8 * 2
n = 6
q = a2 / a1
s6 = a1 * ((1 - q**n) / (1 - q))
print(f'Suma pierwszych {n} wyrazów ciągu wynosi: {s6}')

# %% 16
# x**2 + 5x + 4 = 0
import math
a = 1 
b = 5
c = 4
delta = b ** 2 - 4 * a * c
x1 = (- b - math.sqrt(delta)) / 2 * a
x2 = (- b + math.sqrt(delta)) / 2 * a
suma = x1 + x2 
iloczyn = x1 * x2
print(f'x1+x2 = {suma}\nx1x2 = {iloczyn}')

# rozwianie ok, ale powinno byc 
a = 1
b = 5
c = 4
suma = -b / a
iloczyn = c / a
print(f'x1+x2 = {suma}\nx1x2 = {iloczyn}')

# %% 17
x1 = 2
y1 = 4
x2 = -4
y2 = 6
x = (x1 + x2) / 2
y = (y1 + y2) / 2
print(f'Środek odcinka AD: ({x}, {y})')
# %% 18
import math
x1 = 3
y1 = 2
x2 = -1
y2 = -1
AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'Odległość punktów A i B wynosi : {AB}')

# %% 19
# x**2 + 5x + 4 = 0
import math
a = 1
b = 5
c = 4
delta = b ** 2 - 4 * a * c
x1 = (-b - math.sqrt(delta)) / (2 * a)
x2 = (-b + math.sqrt(delta)) / (2 * a)
print(f'x1 = {x1}\nx2 = {x2}')

# jest ok, ale moglo by byc 
a = 1
b = 5
c = 4
delta = b ** 2 - 4 * a * c
delta_sqrt = delta ** (1/2)
x1 = (-b - delta_sqrt) / (2 * a)
x2 = (-b + delta_sqrt) / (2 * a)
print(f'x1 = {x1}')
print(f'x2 = {x2}')

# %% 20
a = 4
b = 3
c = 4.5
d = 5
x = (a * b * c * d) ** (1/4) 
print(f'Średnia geometryczna podanych liczb: {x:.2f}')

# ok ale mozany bylo lepiej
x1, x2, x3, x4 = 4, 3, 4.5, 5
geo = (x1 * x2 * x3 * x4)**(1/4)
print(f'Średnia geometryczna podanych liczb: {geo:.2f}')










































