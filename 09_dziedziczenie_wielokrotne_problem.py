# -*- coding: utf-8 -*-

class A:
    
    def metoda(self):
        print('Metoda z klasy A')
        
class B(A):
    
    def metoda(self):
        print('Metoda z klasy B')
        
class C(A):
    
    def metoda(self):
        print('Metoda z klasy C')

class D(B, C):
    
    pass
    
   # def metoda(self):
   #     print('Metoda z klasy D')

# %%
d = D()
d.metoda()
