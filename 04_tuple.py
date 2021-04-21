# -*- coding: utf-8 -*-
#%% 50
wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
print(wig20 + mwig40)
# %% 51
wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')

#result = wig20 + mwig40
#print(result)
print(f'({wig20},{mwig40})')
# mozna tez w ten sposob
result = (wig20, mwig40)
print(result)
# %% 52

members = (('Kasia', 23), ('Tomek', 19))
a = (('Adam', 26), ('Dawid', 12))
b = (members + a)
print(b[0],b[2],b[1])

#mozna bylo lepiej, gamoniu!!
members = (members[0], ('Adam', 26), members[1])
print(members)    

# %% 53
default = ('YES', 'NO', 'NO', 'YES', 'NO')
print(f"Liczba wystąpień: {default.count('YES')}")

# %% 54
names = ('Monika', 'Tomek', 'Adam', 'Olaf')
dir(names)
print(f"('{names[2]}', '{names[0]}', '{names[3]}', '{names[1]}')")

# prostsza metoda! 
sorted_names = tuple(sorted(names))
print(sorted_names)
# %% 55
# lamba sortuje po 0 albo 1
info = (('Monika', 19), ('Tomek', 21), ('Adam', 18), ('Jarek', 30))

asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(f'Rosnąco: {asc}')
print(f'Malejąco: {desc}')

# %% 56
stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))
a = stocks[0]
b = a[1]
print(b[0])

# mozna bylo prosciej

print(stocks[0][1][0])
# print(stocks[1][0])

















