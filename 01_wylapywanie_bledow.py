# -*- coding: utf-8 -*-
# %%
1 / 0

# %%
4 + '4'

# %%
int('f')
# %%
float('sd')
# %%
try:
    1 / 0
except:
    print('Nie dzieli się przez zero')

# %%
try:
    1 / 0
except ZeroDivisionError:
    print('Nie dzieli się przez zero')
except TypeError:
    print('Zly typ.') 
# %%
try:
    4 + '4'  
except TypeError:
    print('Nie mozna dodawac tekstu do liczby') 
# %%
try:
    int('sd')  
except ValueError:
    print('Zly tekst.') 
# %%
while True:
    try:
        x = int(input('Podaj liczbe: ')) 
        break
    except ValueError:
        print('Nie wprowadziles poprawnej wartosci')
# %%
try:
    with open('test.txt', 'r') as file:
        for line in file:
            print(line)        
except FileNotFoundError:
    print('Plik nie istnieje')    
# %%
raise TypeError('Bład.')  
# %%
raise ValueError('Bład wartosci.')  
# %%
def divide(x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print('Dzielenie przez zero!')
    except ValueError:
        print('Musisz wprowadzic liczbę')

# divide(3, 0)
divide('1', '2')
divide('1', 'dsd')
























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    