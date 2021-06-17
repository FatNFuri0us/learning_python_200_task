# -*- coding: utf-8 -*-

# public: zmienna
# protected:_zmienna
# private: __zmienna

# %%

class Spolka:
    
    def __init__(self, rodzaj, rynek, gielda):
        self.rodzaj = rodzaj
        self._rynek = rynek
        self.__gielda = gielda
        
class KGHM(Spolka):

    def __init__(self, rodzaj, rynek, gielda, nazwa):
            super().__init__(rodzaj, rynek, gielda)
            self.nazwa = nazwa
            print(f'A publiczne: {self.rodzaj}')
            print(f'A chroniony: {self._rynek}')
            #print(f'A prywatny: {self.__gielda}')

# %% 
spolka = Spolka('spolka akcyjna', 'glowny', 'gpw warszawa') 
print(f'A publiczne: {spolka.rodzaj}')
print(f'A chroniony:{spolka._rynek}')
# print(f'A prywatny: {spolka.__gielda}')

# %%

kghm = KGHM('spolka akcyjna', 'glowny', 'gpw warszawa', 'bzium')

# zeby sie dobrac do zmiennej prywatnej, wpisac Spolka przed __

print(f'A prywatn: {kghm._Spolka__gielda}')
          
