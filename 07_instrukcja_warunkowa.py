# -*- coding: utf-8 -*-
# %% 78
filename = '01012020_sales.xlsx'
if filename.endswith('xlsx'):
    print('TAK')
else:
    print('NIE')    

# %% 79
code = 'DSVNDOICSN'
if code.isupper():
    print('TAK')
else:
    print('no')    
# %% 80
number = 1.0    
if isinstance(number, int):
    print('tak')  
else:
    print('NIE')    
    
# %% 81
password = 'cskdnjcasa#!'
if len(password) >= 11:
    print('Hasło poprawne')
    
# mozna tez w jednej linijce:

print('Hasło poprawne') if len(password) > 10 else print('Hasło zle')   
# %% 82
password = 'cskdnjcasa#!'
print('Hasło poprawne') if len(password) > 10 and '!' in password else print('Hasło zle')
# %% 83
project_ids = ['02134', '24253']
project_id = '02135'

if project_id not in project_ids:
    project_ids.append(project_id)
    print(project_ids)
# %% 84
project_ids = {
    '01': 'open', 
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}    

if project_ids.get('02') == 'new':
    project_ids['02'] = 'open'
    print(project_ids)
# %% 85
item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove(item)
    print(items)

















