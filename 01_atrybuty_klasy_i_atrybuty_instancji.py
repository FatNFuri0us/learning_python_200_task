# -*- coding: utf-8 -*-
# klase identyfikujesz komenda class, z duzej litery
# %%
# nazwa, wiek i wysokosc to atrybuty klasy
class Drzewo:
    
    nazwa = 'Sosna'
    wiek = 40
    wysokosc = 25

drzewo_1 = Drzewo()    
drzewo_2 = Drzewo()
# %%
id(drzewo_1)
id(drzewo_2)

# %%
dir(drzewo_1)

# %%
drzewo_1.nazwa
drzewo_1.wiek
drzewo_1.wysokosc
# %%
# atrybuty intancji 
# %%
drzewo_1.stan = 'dobry'

print(dir(drzewo_1))
# do drzewo 2 NIE MA przypisanego stanu
print(dir(drzewo_2))

# do Drzewo jesli dodasz -> p dodaje "miejsce" do drzewo 1 i drzewo 2
# %%
Drzewo.miejsce = 'las'
print(drzewo_2.miejsce)

drzewo_2.miejsce = 'park'
print(drzewo_2.miejsce)*






























