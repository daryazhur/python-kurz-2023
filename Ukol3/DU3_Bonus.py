"""
Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané 
během semestru. Pozor, bonusové body získali jen někteří žáci.

Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. Bodová rozhraní (vztahují se 
na součet) najdeš zde:

1: 90 a více
2: 70-89
3: 50-69
4: 30-49
5: 29 a méně
Výsledný slovník ulož jako JSON do souboru znamky.json.
"""

import json
with open('body.json', encoding='utf-8') as file:
    info_body = json.load(file)
with open('bonusy.json', encoding='utf-8') as soubor:
    bonus = json.load(soubor)

body_bonus = info_body.copy()
body_bonus.update(bonus) 
for value in bonus:
    if value in info_body:
        body_bonus[value] = bonus[value] + info_body[value]

#nove_znamky = []
nove_znamky = {}
for jmeno, hodnoceni in body_bonus.items():
    if hodnoceni >= 90:
       znamky = 1
    if hodnoceni <= 89:
        znamky = 2   
    if hodnoceni <= 69:
       znamky = 3
    if hodnoceni <= 49:
       znamky = 4
    else:
        znamky = 5  
    nove_znamky[jmeno] = znamky
    
with open('znamky.json', 'w', encoding='utf-8') as new_file:
    json.dump(nove_znamky, new_file, ensure_ascii=False)


           



