"""
Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

Soubor si ulož a načti do slovníku.

Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", 
pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.json.
"""

import json
with open('body.json', encoding='utf-8') as file:
    info_body = json.load(file)

prospech = {jmeno: 'Pass' if pocet_bodu > 60 else 'Fail' for jmeno, pocet_bodu in info_body.items()}
#prospech = {hodnoceni:('Pass' if info_body[hodnoceni] > 60 else 'Fail') for hodnoceni in info_body}

with open('prospech.json', 'w', encoding='utf-8') as soubor:
    json.dump(prospech, soubor, ensure_ascii=False)
   


