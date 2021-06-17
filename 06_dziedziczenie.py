# -*- coding: utf-8 -*-
# %%


class Czlowiek:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        
    def info(self):
        print(f'{self.imie} {self.nazwisko}')
        
        
class Pilkarz(Czlowiek):
    
    def __init__(self, imie, nazwisko, klub):
        super().__init__(imie, nazwisko)
        self.klub = klub
    
    def info_o_zawodniku(self):
        print(f'klub: {self.klub}')
        
# %%
pilkarz_1 = Pilkarz('Robert', 'Lewandowski', 'Bayeryn')        
pilkarz_2 = Pilkarz('krzys', 'piatek', 'ac milan')        

# %%
pilkarz_1.info()
pilkarz_2.info()

# %%
pilkarz_1.info_o_zawodniku()
pilkarz_2.info_o_zawodniku()

# jesli zmienimy info na traie samo to python printuje KLUB, wpierw szuka bo "zagniezdzonych"

# %%
# zmieniamy opcje na metode super

class Czlowiek:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        
    def info(self):
        print(f'{self.imie} {self.nazwisko}')
        
        
class Pilkarz(Czlowiek):
    
    def __init__(self, imie, nazwisko, klub):
        super().__init__(imie, nazwisko)
        self.klub = klub
    
    def info(self):
        super().info()
        print(f'klub: {self.klub}')
        
# %%        
pilkarz_1 = Pilkarz('antosia', 'dolba', 'lipiny')
pilkarz_1.info()
fdg


























        
    
    

