# -*- coding: utf-8 -*-
# %% 21
a1 = 1
S = 1 / (1 - 1/2)
print(f'Suma ciągu wynosi: {S}')
# %% 22
a, b, c = 10, 11, 9
SA = (a + b + c) / 3
od = (((a - SA) ** 2 +(b - SA) ** 2 + (c - SA) ** 2) / 3) ** (1/2)
print(f'Odchylenie standardowe zestawu danych wynosi: {od:.2f}')


#%% 23
filename = 'view.jpg'
print(filename[5:])
# mozna tez 
print(filename[-3:])

# %% 24
string = 'PKV-89415-PLN'
x = string[:3] + string[-3:]
print(x)
# %% 25
string = '1 0 0 1 0 1'
nstring = string[0: :2]
print(f'Znaleziona liczba: {nstring}')
x = 1 * 2 ** (0) + 0 * 2 ** 1 + 1 * 2 ** 2 + 0 * 2 ** 3 + 0 * 2 ** 4 + 1 * 2 ** 5
print(f'Znaleziona liczba: {x}')

# haha jest na to metoda:
string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Znaleziona liczba: {number}')
# %% 26
text = 'Kurs Python'
print(text[::-1])
# %% 27
var1 = ''
var2 = ' '
var3 = '\n'
print(type(var1))
print(type(var2))
print(type(var3))

# %% 28
var1 = None
var2 = False
var3 = 'True'
# %% 29
flag = False
isinstance(flag, bool)
# %% 30
text = 'python jest popularnym językiem programowania.'
print(text.capitalize())
# %% 31

text = 'python jest popularnym językiem programowania.'
print(f"Liczba wystąpień: {text.count('p')}")

# %% 32
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'

print(f"code1: {code1.endswith('2020')}")
print(f"code2: {code2.endswith('2020')}")
# %% 33
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

print(f"path1: {'youtube' in path1}")
print(f"path2: {'youtube' in path2}")

# w przypadku mozna rowniez inna metoda ".startswith()"
    
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'
print(f"path1: {path1.startswith('youtube')}")
print(f"path2: {path2.startswith('youtube')}")
# %% 34
path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'

print(f"path1: {path1.find('scientist')}")
print(f"path2: {path2.find('scientist')}")
print(f"path3: {path3.find('scientist')}")
# %% 35
code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'
print(f'code1: {code1.isalnum()}')
print(f'code2: {code2.isalnum()}')
# %% 36
text = 'Google Colab'
print(text.lower())
#%% 37
text = 'Google Colab'
print(text.upper())
# %% 38
text = '  Google Colab   '
print(text.strip())
# %% 39
code = 'FVNISJND-XX'
print(code.replace('-', ' '))
# %% 40
text = '340-23-245-235'
print(text.replace('-', ''))








































