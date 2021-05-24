# -*- coding: utf-8 -*-
# %% 64
# SLOWNIK DICT {} zasada KLUCZ - WARTOSC

'Poland', 'Warsaw'
'Germany', 'Berlin'
'Austria', 'Vienna'

x ={'Poland':'Warsaw', 'Germany':'Berlin', 'Austria':'Vienna'}
print(x)
# %% 65

capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'}
print(capitals.keys())
# %% 66
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'}
print(capitals.values())
# %% 67
dir(capitals)
print(capitals.items())
# %% 68
print(capitals.get('Austria'))
# %% 69
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}}
print(stocks.get('PLW'))
# %% 70
# wycinanie w listach
print(stocks['TEN']['Ten Square Games'])
# %% 71
# podstawianie nowe listy

stocks['CDR'] = 310
print(stocks['CDR'])

# %% 72
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}}
stocks['BBT'] = { 'Boombit': 23}
print(stocks.values())

# %% 73
ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]

# sortowanie listy po indexie, przydatna metoda
print(list(enumerate(ticker)))

# %% 74
ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]

print(dict(enumerate(ticker)))
x = dict(enumerate(ticker))
y = list(enumerate(ticker))

# w liscie otrzymumemy tuple, w slowniku stringu
# %% 75

project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

result = list(set(project_ids.values()))
result.sort()
print(result)


x = set(project_ids.values())
y = list(set(project_ids.values()))



x.sort()
y.sort()
# %% 76
stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}
del stats['ruch']
print(stats)
# %% 77
users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
print(users.get('004', 'nieokreślony'))

users.get('004', 'bzium')




















































