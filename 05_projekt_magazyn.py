# -*- coding: utf-8 -*-
import sys


class Magazyn:
    
    def __init__(self, lista_produktow):
        self.lista_produktow = lista_produktow
    
    def wyswietl_dostepne_produkty(self):
        print('Dostepne produkty:')
        for produkt in self.lista_produktow:
            print(produkt)
    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwe produktu: >>> ')  
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
        print(f'Produkt {self.nazwa_produktu} zostal dodany do magazynu.')
    
    def usun_produkt(self):
        self.nazwa_produktu = input('Podaj nazwe produktu, do usuniecia: >>>')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print('Usunieto produkt z magazynu')
        else:
            print('Podanego produktu nie ma w magazynie')
            
# %%
magazyn = Magazyn(['mleko', 'woda', 'jajka']) 

while True:    
    print('Wprowadz 1 aby wyswietlic stan magazynu.')
    print('Wprowadz 2 aby dodac produkt.')
    print('Wprowadz 3 aby usunac produkt.')
    print('Wprowadz 4 aby zakonczyc.')
    
    wybor_uzytkownika = int(input('>>> '))
    if wybor_uzytkownika == 1:
        magazyn.wyswietl_dostepne_produkty()
    elif wybor_uzytkownika == 2:
        magazyn.dodaj_produkt() 
    elif wybor_uzytkownika == 3:
        magazyn.usun_produkt()   
    elif wybor_uzytkownika == 4:
        sys.exit()
# %%

















           