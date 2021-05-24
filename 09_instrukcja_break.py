# -*- coding: utf-8 -*-
# %% 97
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
result = False

for i in list2:
    if i in list1:
        result = True
        break
print(result)    

# %% 98
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True

for idx in hashtags:
    if type(idx) != str:
        result = False
        break
print(result)    

        
# %% druga metoda

for hashtag in hashtags:
    if not isinstance(hashtag, str):
        result = False
        break
    
print(result)

# %%


a = ['sad', None, 'fsd']        

isinstance(a, list)
# %% 99
number = 1
 
if number > 1:
    for i in range(2, 11):
        if number % i == 0:
            print(f'{number} - nie jest pierwsza')
            break
    else:
        print(f'{number} - liczba pierwsza')
else:
    print(f'{number} - nie jest pierwsza')
   
        
# %% 100
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}















































