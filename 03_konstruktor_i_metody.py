# -*- coding: utf-8 -*-
# dwie linie puste przed i po stworzeniu "CLASSY"
#%%


class Drzewo:
    
    def __init__(self, nazwa, wiek, wysokosc):
        self.nazwa = nazwa
        self.wiek = wiek
        self.wysokosc = wysokosc
        
    def czy_chronione(self):
        if self.wiek >= 20 and self.wysokosc >= 20:
            print(f'Drzewo o nazwie {self.nazwa} pod ochroną.')
        else:
            print(f'Drzewo o nazwie {self.nazwa} nie jest pod ochrona.')
    def postarz_o_rok(self):
        self.wiek += 1       
        
# %%
drzewo_1 = Drzewo('Sosna', 35, 25)        
drzewo_2 = Drzewo('Brzoza', 15, 18)    
#%%
print(drzewo_1.nazwa)
print(drzewo_2.nazwa)

# %%
drzewo_1.czy_chronione()
drzewo_2.czy_chronione()
# %%
print(drzewo_1.wiek)
drzewo_1.postarz_o_rok()
print(drzewo_1.wiek)
