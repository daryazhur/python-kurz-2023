"""
Napiš program, který se zeptá uživatele na jeho přihlašovací jméno, e-mailovou adresu a heslo. 
Po každém zadaném údaji program ověří jeho správnost podle následujících pravidel:
    - uživatelské jméno smí obsahovat malá a velká písmena (nesmí obsahovat žádné jiné znaky), jeho minimálná délka 
    je 6 znaků a jeho maximální délka je 10 znaků.
    - heslo smí obsahovat malá a velká písmena, číslice, a následující speciální znaky: _, -, ., +, =. 
    Jeho minimálná délka je 12 znaků a jeho maximální délka je 30 znaků.
    - e-mail by měl být validním e-mailem 
"""

import re

regularni_vyraz_jmeno = re.compile(r"[A-Z|a-z]\w{6,10}")

jmeno = input('Zadej svoje uzivatelske jmeno: ')

jmeno_ok = regularni_vyraz_jmeno.fullmatch(jmeno)

print(jmeno_ok)

if jmeno_ok:
    print('Uzivatelske jmeno je platne, muzete zadat svuj email')
else:
    print('Uzivatelske jmeno neni platne')  

regularni_vyraz_heslo = re.compile(r'[A-Z|a-z|_|.|+|=]\w{12,30}')

heslo = input('Zadejte svoje heslo: ')

heslo_ok = regularni_vyraz_heslo.fullmatch(heslo)

print(heslo_ok)

if heslo_ok:
    print('Heslo je spravne')
else:
    print('Heslo neni spravne')    

regularni_vyraz = re.compile(r"\w+.?\w+@\w+\.\w+")

email = input("Zadej e-mail: ")

hledani = regularni_vyraz.fullmatch(email)

if hledani:
    print("E-mail je v pořádku")
else:
    print("Nesprávný e-mail")
