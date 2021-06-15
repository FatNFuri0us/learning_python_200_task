# -*- coding: utf-8 -*-
# Sprawdź i wypisz ile unikatowych elementów znajduje się w liście A.
# %% 1
A = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 5, 43, 4, 6]

# Twój kod tutaj
b = list(len(set(A)))

print(len(b))

c = []
for i in A:
    if i not in c:
        c.append(i)
        
print(c)
# %% 2
a = 'dfsfsdfsd'
a_lista = list(a)
a_lista[1] = 'X'
a = "".join(a_lista)

# %% 3
L = [1, 2, 3, 4, True, (1, 2)]
T = (4, 5, 6, False, ['x', 'y'])

L[2] = 'trzy'
T[2] = 'szeć'
# %% 4

szafka = [[[],[],[]],[[],[],[]],[[],[],[]]]
szafka[1][1] = 'dlugopis'
print(szafka)
print('sd')
for szuflada in szafka:
    print(szafka)
# %%
A = [[1, 2], [3, 4]]    
A[1][0] = 'trzy'
print(A)
# %% 5
K = (('król', {2:'królewna', 1: ['córka', 'wróbel']},'5'),('żółw', 'wiewiórka'))
print(K[0][1][1][1])    

# %% 6
D = {123456789: 'Jan Kot', 999888777: 'Anna Lis', 111222333: 'Jan Kot'}
print(D[123456789])
print(D)

D = {'imie': 'Anna', 'imie': 'Karolina', 'imie': 'Żaneta', 2: 'df', 'imie': 'fufiu'}
print(D['imie'])

# %% 7
C = {[4, 5]: [16, 25]}
C = {(4, 5): [16, 25]}
print(C[4, 5])

C = {{1:2}: 'jeden_dwa'}
# %% 8

D = {1: 'Ala', 2: 'ma', 3: 'kota'}

for key in D:
    print(D[key])
# %% 9
## werja python od ktorej slowniki maja gwarantwane numerowanie 3.7

# %% 10
x = "myszydokazujągdykotanieczują"
l ={}
for i in x:
    if i not in l.keys():
        l[i] = 1
    else:
        l[i] += 1
       

# %%
S = {x:x+1 for x in range(10000) if x%23 == 0}


for i in S.keys():
    if i == 7430:
        print(True)
    else:
        print(False)
        break




### mozna prosciej
if 7430 in S.keys():
    print(True)
else:
    print(False)
### albo jeszcze lepiej
print(True if 7430 in S.keys() else False)
# %% 11
x = "myszydokazujągdykotanieczują"

for i in l.values():
    if i == 4:
        print(True)
    else:
        print(False)
        break
# %%
if 4 in l.values():
    print(True)
else:
    print(False)   
# %%    
print(True if 4 in l.values() else False)    


print(list(l.values())) 
# %% 
pensje = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}
print(sum(pensje.values()))
# %% 12

jezyki = ['Python', 'Java', 'C#', 'Ruby']
## 1 metoda
print(list(reversed(jezyki)))
## 2 metoda
jezyki.reverse()
jezyki_odwrocone = jezyki
print(jezyki_odwrocone)
## 3 metoda
jezyki_2 = jezyki[::-1] ## parametr [start:stop:skok]
print(jezyki_2)
## 4 metoda
jezyki_3 = []
for jezyk in jezyki:
    jezyki_3.insert(0, jezyk)
print(jezyki_3) # wsadza na 0 miejsce kazdy kolejne


odwroc_mnie = ['trudne', 'takie', 'bylo', 'nie', 'To']
odwrocona = odwroc_mnie[::-1]
print(odwrocona)
# %% 13
z = 'kajak'
if z == z[::-1]:
    print(True)
else:
    print(False)

##
def palindrom(x):
    if x == x[::-1]:
        return True
    else:
        return False
##
print(True if z == z[::-1] else False)
# %%


##
def palindromy(x):
    poczatek = 0
    koniec = len(x) - 1
    while poczatek <= koniec:
        if x[poczatek] != x[koniec]:
            return False
        else:
            poczatek += 1
            koniec -= 1
    return True        

palindromy("adacadal")
# %% 14
a = []
b = []
## start, stop, skok
a = list(range(1, 11))
b = list(reversed(range(1, 101, 3)))
B = list(range(100, 3, -3))
# range to nie funkcja tylko TYP DANYCH - zwraca sekwencje liczb, lepsza wydajnosc niz w python 2
print(list(range(-5, 6)))
list(range(-5, 6, 2))
# %% 15
L = [11, 22, 33, 44, 55, 66, 77, 88, 99, 1010]
s = 'a nMozh^tKysPW 9ęxi b$uML'

# range(start,stop,krok)
# mojedane[start:stop:krok]
print(L[0:5]) ## print(L[:5])
print(s[::-2])
print(s[-1::-2])

a = '!ooe&sj7?czaa()lmxuo,t2fa^4rtngk'
print(a[-2::-3])
# %% 16
a = "python_moj_kod.py"
b = "python_notatki.txt"



def fiufiu(x):
    start = 'python'
    koniec = 'yp.'
    if x[0:6] == start and x[-1:-4:-1] == koniec:
        return True
    else:
        return False

fiufiu(a)
## duzo prosciej x[-3:] = '.py'
a[0:6]
a[-1:-4:-1]
# %%
z = "In the face of ambiguity, refuse the temptation to guess."
print(z[-6:])
# %% 16
imiona = ['Adam', 'Stanislaw', 'Maria', 'Zofia', 'Mikolaj']


print(list(enumerate(imiona, 1)))
idx = 1
for i in imiona:
   print(idx, i)
   idx += 1

# %% 
for num, imie in enumerate(imiona, 1):
    print(num, imie)
# %%
A = [1, 1, 4, 9]
idx = 0
for i in A:
    print(idx, i)
    idx += 1

for num, imie in enumerate(A):
    print(num, imie)

# %% 17
A = [4, 5, 7, -3, 2, 8, -10, 15]
print(max(A)-min(A))

###
A = sorted(A)
print(A[-1] - A[0])
# %%
najmnniejsza = A[0]
najwieksza = A[0]
for liczba in A:
    if liczba < najmnniejsza:
        najmnniejsza = liczba
    elif liczba > najwieksza:
        najwieksza = liczba
print(najwieksza - najmnniejsza)        
# %%
A = [x**2 + 3 for x in range(10)]
print(True if max(A) > 99 else False)
# %% 18

def boom(x, y):
    if x % y == 0:
        return True
    else:
        return False


print(boom(4, 2))
#%% DUZO LEPSZY SPOSOB
def bom(x, y):
    return(x % y == 0)



print(bom(-8, -4))
print(bom(12, 4))
print(-5 % 3)
#%%
a = 123454321 

b = 11111 
print(True if a % b == 0 else False)
# %% 19
def dodaj_do_listy(n, lista=[]):
    lista.append(n)
    print(lista)



# %%
dodaj_do_listy(1)
dodaj_do_listy(2, [4, 5])
dodaj_do_listy(3)


### lista=[] gdy nie podamy to bedzie to i tak, ale lista zostaje przechowana w pamieci
### argument domyslny 

def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

# rozwiazanie tego problemu

# %% 20
L = [1, 2, 3, 4, 5, 6]
L1 = [x for x in range(5)]
L2 = [x**2 for x in L]
L3 = [x for x in L if x % 2 == 0]
L4 = ['Parzysta' if x % 2 == 0 else 'Nieparzysta' for x in range(5)]
L5 = [(x, x + 10) for x in L]
D1 = {x:x % 2 == 0 for x in L}

# %% 
v =(x for x in range(5))
print(list(v))

A1 = [x + 1 for x in range(5, 12)]

# %% 21

print(1 == False) # operator porownania wartosci czy wartosc po lewej jest rowna wrtosci po prawej
print(1 is True) # operator porowania identycznosci, czy obiekty sa identyczne




print(id(1), id(True))



A = [1, 2, 3]
B = [1, 2, 3]
print(A == B)
print(A is B)
a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)
print(a == b)
x = 'kotek'
y = 'kotek'
print(x == y)
print( x is y)

# jest tylko jeden obiekt w pamieci, listy sa modyfikowalne dlatego sprawdza w 2 miejscach

# %% 22

print(False is False)
print(True is False)
print(False is False is False)# (false is false)
# porownanie lancuchowe 
print(1 < 3 == 5) # (True) and (False)
print(1 < 5 == 5 == 5 < 10)

# %% 23
#lambda argument: wyrazenie

lambda x: x + 2

def zwieksz_liczbe(x):
    return x+2


L = [('Anna', 82), ('Robert', 33), ('Artur', 40), ('Feliks', 56)]
L_posortowana = sorted(L, key = lambda x: x[1])

print(L_posortowana)


S = ['Anna', 'Robert', 'Artur', 'Feliks'] 

S_posortowana = sorted(S, key = lambda x:x[-1])
print(S_posortowana)

# %% 24
A = [1, 2, 3, 4, 5]
B = A # kopiowanie REFERENCJI
C = A[:] # C = list(A) # kopiowanie WARTOSCI
B[0] = 111
print(B)
print(A)
print(C)


#A i B wskazuje na ta sama liste
#C dzieki zapisowi [:] tworzy w pamieci kolejna liste do ktorej C sie odwoluje

print(id(A))
print(id(B))
print(id(C))


L = [0, 1, 2, 3]
# %% 25
x = 10 # zmienna globalna

def f():
    x = 11 # zmienna lokalna, stworzona w wyniku funkcji po czym znika
    print(x)
    
f() 
print(x)   

#%%

def f():
    global x
    x = 111
    y = 12
    print(x, y)
    
f()
print(x)

# %% 26
with open('moj_plik.txt', 'w') as f:
    for n in range(1, 101):
        f.write(str(n) + '\n')

# %%
with open('moj_plik.txt', 'r') as f:
    z_pliku = f.readlines()

print(z_pliku)
# readlines odczytuje plik linijka po linijce i zaspisuje w formie listy

# %%


with open('przeczytaj_mnie.txt', 'r', encoding='utf-8') as f:
   print(f.read())
# %% 27
import random


A = [random.randint(0, 100) for i in range(5)]
B = [random.randint(0, 100) for i in range(5)]
H = [random.randint(0, 100) for i in range(5)]

max_v = 0
licznik = 0
for a in A:
    for b in B:
        for h in H:
            licznik += 1
            if a * b * h > max_v: # 125 operacji
                max_v = a * b * h
                
print(max_v)
print(licznik)

# %%
print(max(A) * max(B) * max(H)) # 15 operacji

# %% 28
from drukarka import wydrukuj_imie



def wydrukuj_imie(imie):
    print(imie)




wydrukuj_imie("Marta")


# jesli w module jest taka sama nazwa funkcji wtedy python czyta ta zdefiniowana ostanio

# zmiana nazwy funkcji:
    
from drukarka import wydrukuj_imie

def wydrukuj_imie_lokalna(imie):
    print(imie)   

## uzycie aliasu

from drukarka import wydrukuj_imie as wydrukuj_mnie_z_drukarki

def wydrukuj_imie(imie):
    print(imie)

# %% 29

import muzyka.trabka
import muzyka.perkusja

muzyka.trabka.graj()
muzyka.perkusja.graj()



import bbb.trabka
from muzyka import trabka
from muzyka import perkusja
trabka.graj()
perkusja.graj()


from bbb import trabka
trabka.gra()

from muzyka.trabka import graj

graj()
# %% 30

print(1 is not True in [1, 2, 3]) 

# %% 31
nazwiska = ['jan kot', 18, 'ANNA KRÓL', 'jÓzef BYK', ['nie', 'wasza', 'sprawa'], 'ROBERT wąż']
#filter(funkcja, sekwencja)

nazwiska_wyczyszczone = list(filter(lambda x: type(x) is str, nazwiska))
nazwiska_wyczyszczone = list(filter(lambda x: type(x) is str, nazwiska))
#map(funkcja, sekwencja)


poprawione = list(map(lambda x: x.lower().title(), nazwiska_wyczyszczone))
# %% 32
def dodaj_gwiazdki(funkcja):
    def funkcja_udekorowana():
        print('***')
        funkcja()
        print('***')
    return funkcja_udekorowana    



# %%
@dodaj_gwiazdki
def f():
    print('Czesć, jestem f()')



f()
# %% 33
def zwracaj_kolejne_parzyste():
    for n in range(2,20,2):
        yield n



z = zwracaj_kolejne_parzyste()
print(z)

print(zwracaj_kolejne_parzyste())
print(next(z))
#%%
for i in range(9):
    print(next(z))
# %%

y = ('a' * n for n in range(5))

#%%
for i in range(5):
    print(next(y))

## zuzywa mniej pamieci, liczy po kolei, NIE tworzy lisdty z miliona elementow
## sekwencje bez konca, NIE ma listy bez konca, generatow moze miec


# %%

def x():
    for n in range(1, 11):
        yield n * 5
    
#%%
blum = x()
for i in range(10):
    print(next(blum))
# %%
x()

print(next(x()))

w = (5 * n for n in range(1, 11))
print(w)
print(next(w))
#%%
for i in range (10):
    print(next(w))

# %% 34
assert 1 == 1

assert 1 == 2
#%%
def dodawanie(a, b):
    return a + b + 1

def test_dodawanie_intow():
    assert dodawanie(2, 3) == 5
    
def test_dodawanie_stringow():
    assert dodawanie('a', 'b') == 'ab'    



test_dodawanie_intow()
test_dodawanie_stringow()
# %%
# pytest 
# unittest

pytest MP1_10.py




print(dodawanie(1, 3))
# %% 35

class Pies:
    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa
# %%        
maly_pies = Pies('Pikus', 'ratlerek')          
duzy_pies = Pies('Killer', 'doberman')

print(maly_pies)
print(maly_pies.imie, maly_pies.rasa)
print(duzy_pies.imie, duzy_pies.rasa)
# %%
class Kot:
    def __init__(self, imie, kolor):
        self.imie = imie
        self.rasa = kolor
        
k = Kot('Mruczek', 'czarny')        
print

# %% 36
class Pies:
    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa


    def __str__(self):
        return f"Pies rasy {self.rasa} mam na imie {self.imie}"

fiu = Pies('dawid', 'fujara')
maly_pies = Pies('Pikus', 'ratlerek') 
print(fiu)

# %%
class Kot:

    def __init__(self, imie, kolor):
        self.imie = imie
        self.kolor = kolor
        
    def __str__(self):
        return f"Kot {self.imie} jest {self.kolor}"

k = Kot("Mruczek", "rudy")


print(k)

# %% 37

class ZwierzeLadowe:
    def przedstaw_sie(self):
        print("Jestem zwierzęciem lądowym.")
    def biegaj(self):
        print("Biegam tu i tam.")
        
        
        
class ZwierzeMorskie:
    def przedstaw_sie(self):
        print("Jestem zwierzęciem morskim.")
    def plywaj(self):
        print("Pływam tu i tam.")


class SwinkaMorska(ZwierzeLadowe, ZwierzeMorskie):
    pass # nie chcemy wpisywac kodu i nie chcemy zeby python sie czepial



swinka = SwinkaMorska()
swinka.przedstaw_sie()
swinka.biegaj()
swinka.plywaj()


# priorytetem w dziedziczeniu jest KLASA ktora wpisalismy po lewo
# %% 38

class Matematyka:
    def __init__(self):
        self.pi = 3.14
        
    def policz_obwod_okregu(self, r):
        return 2 * self.pi * r
    
    @staticmethod
    def dodaj(a, b):
        return a + b
   # @staticmethod    
   # def dodaj_i_pomnoz(a,b):
   #     return dodaj(a,b) * 2
    #
    @classmethod    
    def dodaj_i_pomnoz(cls,a,b):
        return cls.dodaj(a,b) * 2


m = Matematyka()
m.policz_obwod_okregu(5)
Matematyka.dodaj(2, 3)
print(m.policz_obwod_okregu(5))
print(Matematyka.dodaj(2, 3))



print(Matematyka.dodaj_i_pomnoz(2, 3))
# %% 39
#FIZZ BUZZ


def fizzbuzz(n):
    for num in range(1, n+1):
        if num % 15 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(str(num))



fizzbuzz(30)
# %% 

def fizzbu(n):
    for num in range(1, n+1):
        wynik = ''
        if num % 3 == 0:
            wynik += 'Fizz'
        if num % 5 == 0:
            wynik += 'Buzz'
        if num % 3 != 0 and num % 5 != 0:
            wynik = str(num)
        print(wynik)    




fizzbu(30)
# %% 40
# CIAG FIBONACCIEGO

def FIBONACCIEGO_r(n): # 0(2 ^n)
    if n <= 1:
        return n
    return FIBONACCIEGO_r(n - 1) + FIBONACCIEGO_r(n -2)






print(FIBONACCIEGO_r(6))

print(FIBONACCIEGO_r(216))


# %%
def fibi(n):
    p, d = 0, 1
    for _ in range(n):
        p, d = d, p + d
    return p    



print(fibi(1000))
# %% 41
# Rekurencyjne wypisywanie katalogu

# os.listdir - zwraca zawartosc danego katalogu
# os.path.join - laczy dwa stringi w sciezke czytalna dla danego systemu operacyjnego
# os.path.isdir - sprawdz czy pod nadana sciezka znajduje sie katalog
import os


def wypisz_zawartosc_katalogu(sciezka_do_katalogu):
    for element in os.listdir(sciezka_do_katalogu):
        sciezka_do_elementu = os.path.join(sciezka_do_katalogu, element)
        if os.path.isdir(sciezka_do_elementu):
            wypisz_zawartosc_katalogu(sciezka_do_elementu)
        else:
            print(sciezka_do_elementu)
# %%
wypisz_zawartosc_katalogu(r'C:/Users/admin/Desktop/Bestia KODOwania/testowy')



os.listdir(r'C:/Users/admin/Desktop/Bestia KODOwania/testowy')
os.path.join(r'C:/Users/admin/Desktop/Bestia KODOwania/testowy','zagniezdzony' )
os.path.isdir(r'C:/Users/admin/Desktop/Bestia KODOwania/testowy\\a.txt')

# %% 42
# Wyszukiwania binarne
P = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]
# szuka w bardzo wydajny sposob

# %%
lewy = 0
szukana = 100
prawy = len(P) - 1
while lewy <= prawy:
    srodkowy = (lewy + prawy) // 2 # dzielenie calkowite bez reszty
    if P[srodkowy] == szukana:
        print(f'Liczba {szukana} znajduje sie na liscie')
        break
    elif P[srodkowy] < szukana:
        lewy = srodkowy + 1
        
    else:
        prawy = srodkowy - 1
else:
    print(f'Liczby {szukana} nie ma na liscie')        
        
#%% 43
# Big 0 zlozonosc obliczewniowa


# 0(1) gdy tylko 1 lub kilka operacji
# gdy szukamy slowniku

## 0(Log(n)) wyszukiwanie binarne, zlozonosc logarytmincza
### O(n) - np czytanie listy o 15 elementach = 15 
#### O(n * Log(n)) quicsort
##### O(n**2) pomnozyc kazdy element listy * kazdy element listy
###### O(2**n) 

# O(1) -          sprawdzenie czy element jest w słowniku (tablicy hashującej)
# O(log(n)) -     wyszukiwanie binarne
# O(n) -          jednokrotne przejrzenie listy o długości n
# O(n * log(n)) - (wydajne) sortowanie (timsort, quicksort)
# O(n**2) -       mnożenie każdego z każdym z elementów na liście
# O(2**n) -       Fibonacci rekurencyjnie

import math       # poniższy kod wyświetla wykres przedstawiający porównanie różnych złożoności obliczeniowych
                  # przy użyciu popularnej bibliteki matplotlib
import matplotlib.pyplot as plt

seria0 = [1] * 10
seria1 = list(range(1,11))
seria2 = [math.log(x) for x in seria1]
seria3 = [math.log(x) * x for x in seria1]
seria4 = [x**2 for x in seria1]
seria5 = [2**x for x in seria1]

plt.plot(seria0, label="O(1)")
plt.plot(seria2, label="O(log(n))")
plt.plot(seria1, label="O(n)")
plt.plot(seria3, label="O(n * log(n))")
plt.plot(seria4, label="O(n**2)")
plt.plot(seria5, label="O(2**n)")

plt.legend()
plt.show()


# %% 45
# DYNAMICZNE TYPOWANIE
from typing import List

def przeliteruj(word: str) -> List[str]:
    return 5



print(przeliteruj('Python'))
print(przeliteruj(1))

# %% 46

# PEP8 !

import os
import math

import modul_zewnetrzny

import moj_fajny_modul


class KlasyDuzymiLiterami    # 2 linijkki nad i pod
    pass


zmienne_malymi_literami  = 'snake case'

def funkcja_rowniez_malymi_litermia # 1 linijka pod i nad
    pass

A = [1, 3, 2]
B = ['tak','jest','zle']


# %% 46
# pip


# w lini kodu "pip install"



from colorama import init, Fore, Back, Style
init()
print(Fore.RED + "Tekst na czerwono")
print(Back.YELLOW + '... na zółtyn tle')
print(Style.RESET_ALL + '... i znowu normalnie')

# PyPI
# %% 47
# dir i help
# %% 48
# PROSTA SKLADNIA

czytanie kodu ma byc przyjemne

## BRAK NAWIASOW KLAMROWYCH
wciecia zamiast klamer {}{}{}


# JEZYK INTERPRETOWANY
czytany linijka po linijce

jest wolniejszy!!
# DYNAMICZNIE TYPOWANY
# DUZO BILBLIOTEK

# WADY?
#%% 49

fiu fiu
# %% 50



import this




















































































































































































































































































    
    
    
    
    
    
    
    
