# -*- coding: utf-8 -*-
# %% 41
text = 'Open,High,Low,Close'
print(text.split(','))
print(text)
# %% 42
text = """Python jest językiem ogólnego przeznaczenia.
Python jest popularny."""
print(text.split('\n'))
# mozna tez inna metoda: print(text.splitlines())
# %% 43
num = 34
print(f'0000{num}')
# powinna byc ta metoda
print(str(num).zfill(6))

# %% 44
url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
nurl = url.replace('-', ' ')
nurl = nurl[nurl.index('sc'):]
print(nurl)

# ok ale powinienem pociac stringi na listy i wyprintowac ostatnia liste:
url = ('https://e-smartdata.teachable.com/p/'
    'sciezka-data-scientist-machine-learning-engineer')
name = url.split('/')[-1]
name = name.replace('-', ' ')
print(name)
# galgan ze mnie jak nic
name = url.split('/')
name = url.split('/')[-1]

#%%
text = 'dawid/ da/wid dawid'
x = text[-1]
print(x)

y = text.split('/')
z = y[-1]

# %% 45
przedmioty = {'matematyka', 'polski'}
przedmioty.add('angielski')
print(przedmioty)
# %% 46
text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}
ntext = text.lower()
ntext = ntext.replace(' ', '') 
ntext = set(ntext.replace('.',''))
ntext = ntext.difference(vowels)
print(f'Liczba elementów: {len(ntext)}')

# jedna linijka mniej niz we wzorze:) fiu fiu, tylko ze mnie czytelnie:(
text = 'Programming in python.'
text = text.lower()
text = text.replace(' ', '')
text = text.replace('.', '')
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = set(text)
consonants = letters.difference(vowels)
print(f'Liczba elementów: {len(consonants)}')
# %% 47
# Roznica symetryczna dwoch zbiorow to zbior skladajacy sie
# wszystkich elementow tych zbiorow oprocz elementow wspolnych
# metoda symmetric_difference
# %% 47
A = {2, 4, 6, 8}
B = {4, 10}
print(f'Różnica symetrczyna: {A.symmetric_difference(B)}')

# %% 48
ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
a = (ad1_id.difference(ad2_id))
b = (ad2_id.difference(ad1_id))
c = a.add('007')
print(f"Wybrane ID: {c}")
c = ad1_id.difference(ad2_id).update(ad2_id.difference(ad1_id))
print(f'{ad1_id.difference(ad2_id)}
print(a, b)      
c = a.add('007')
print(c)
c = ad1_id.difference(ad2_id)
d = ad2_id.difference(ad1_id)
c.update(d)
print(c)
dir(set)
print(a.add('007'))
print(a)
# co ja zrobilem? takie proste!

ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
result = ad1_id.symmetric_difference(ad2_id)
print(f'Wybrane ID: {result}')

#%% 49
# metoda intersection -> elementy wspolne zbiorow
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
print(f'ID klientów: {is_clicked.intersection(is_bought)}')


































sdfsdfsdfwe














































































