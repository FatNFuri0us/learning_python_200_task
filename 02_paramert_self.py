# -*- coding: utf-8 -*-
# bez slowka pass python wyrzuci blad
# %%
class Drzewo:
    
    def wyswietl_info_o_drzewie(self):
        self.nazwa = 'Sosna'
        self.wiek = 30
        print(f'Drzewo {self.nazwa} ma {self.wiek} lat.')
        
drzewo = Drzewo() 
# %%
# male drzewo z przodu bo wykonujemy funkjce juz na malym drzewie
drzewo.wyswietl_info_o_drzewie()  
# %%
# drzewo w nawiasie bo potrzebujemy OBIEKTU do wykonania funkcji
Drzewo.wyswietl_info_o_drzewie(drzewo)
 