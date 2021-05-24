# -*- coding: utf-8 -*-
# %% 86
result = []
for i in range(99):
    if i % 11 == 0 and i % 3 != 0:
        result.append(str(i))
        
print(','.join(result))
# %% 87
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]

for i in items:
    if i % 2 != 0:
        items.pop(i)
print(items)        
# inaczej
# %%
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for item in items:
    if not item % 2 != 0:
        result.append(item)
print(result)
# %% 88
items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []

for i in items:
    if not i in result:
        result.append(i)
        
print(result)        
# %% 89
text = 'Python jest bardzo popularnym językiem programowania'

words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)
        
# %% 90
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []

for idx in probabilities:
    if idx > 0.50:
        result.append(idx)
        
print(result)
# %% 91
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []

for i in probabilities:
    if i < 0.50:
        result.append(0)
    else:
        result.append(1)
        
print(result)        
# %% 92
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']


freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1
 
print(freq)


# spoko opcja


a = {}
a['x'] = 1
a['y'] = 2
# %% 93

text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""

result = list(text)

for i in text:
    if i != ' ':
        result.append(i)
    else:
        result.append(', ')
        
print(result)        
        
        
# %%


text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""
# %% 
words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 10]
print(words)


# %% 94
indexes = [
    'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE', 
    'WIG-chemia', 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo',
    'WIG-informatyka', 'WIG-leki', 'WIG-media', 'WIG-motoryzacja',
    'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
    'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine',
    'WIG.GAMES', 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET',
    'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short', 'WIG20TR',
    'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech'
]
for i in indexes:
    if '20' in i or '30' in i:
        print(i)


# %% przydatna metoda
# %% 95
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}


for ticker, close in gaming.items():
    if close > 100.0:
        print(ticker)


# istotne iterowanie po slowniku

# %% 96
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for i in names:
    if i.isalpha() == True:
        print(f'Hello {i}!')
    




# %%













































    

