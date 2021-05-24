# -*- coding: utf-8 -*-
# %% 57
cities = ['Warszawa', 'Łódź', 'Kraków']
print(cities + ['Gdańsk'])
# moze tez byc metoda append, dodaje na stale

cities.append('Gdańsk')
print(cities)
# %% 58
idx = ['001', '002', '001', '003', '001']
print(f"Liczba wystąpień: {idx.count('001')}")
# %% 59
text = 'Programowanie w języku Python'
ntext = text.lower()
ntext = ntext.replace('ę', 'e')
ntext = ntext.replace(' ', '')
ntext = set(ntext)
ntext = sorted(ntext)
print(ntext[:10])
# mozna i tak jak na dole
text = text.lower()
text = text.replace('ę', 'e')
characters = list(set(text))
characters.remove(' ')
characters.sort()
print(characters[:10])
# %% 60
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)
# %% 61
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
# metoda append dodaje kolejna liste w liscie
print(day1)

# %% 62
techs = ('python', 'java', 'sql', 'aws')
x = list(techs)
x.sort()
print(tuple(x))
#%%
techs = ('python', 'java', 'sql', 'aws')
teshs = tuple(sorted(techs))
print(techs)
# %% 63
hashtags = ['summer', 'time', 'vibes']
hashtags = set(hashtags)
hashtags = 'summer time vibes'
hashtags.insert(2, '#')
hashtags.insert(4, '#')
print(hashtags)

dir(hashtags)
hashtags.insert(0, '#')
hashtags.insert(2, '#')
hashtags.insert(4, '#')

hashtags.insert(1, '#')

hashtags.insert(1, '#')
# powinno byc tak!

print('#' + '#'.join(hashtags))

'3' + '1' + '2'+ '4'.join(hashtags)
# %%
x = []



















































