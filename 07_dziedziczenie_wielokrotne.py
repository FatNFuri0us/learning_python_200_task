# -*- coding: utf-8 -*-
# %%


class Czlowiek:
    
    pochodzenie = 'Ziemia'
    imie = 'jack'
    
    
class Polak:

    kraj = 'Polska'
    imie = 'Piotr'
    
# najpierw Klaa Pilkarz, pozniej szukas w k Czlowiek i na koniec w k Polak    

class Pilkarz(Czlowiek, Polak): 
    
    def info(self):
        print(f'utworzony obiekt pochodzi z planety {self.pochodzenie}\n '
              f'Kraj pochodzenia: {self.kraj}.\n'
              f'Nazwa obiektu: {self.imie}')
        
# %%

pilkarz_1 = Pilkarz()        
pilkarz_1.info()
