"""
Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš 
například tak, že použiješ metodu .replace(). První parametr metody replace je znak, který chceš nahradit, a druhý 
parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".

Odkaz na dokumentaci metody replace: https://docs.python.org/3/library/stdtypes.html#str.replace
"""

def telefonni_cislo(cislo):
    if len(m) == 9: 
        tel = True
    else:
        print('Vase telefonni cislo neni platne')
        exit()  
    return tel
cislo=(str(input('Zadejte svoje telefonni cislo: ')))
m = cislo.replace(" ", "")
tel = telefonni_cislo(cislo)
print(tel)

def sms(znak):
    cena = 0.01667 * znak
    return cena  
text = input('Napiste zpravu: ')
znak = len(text)
cena = sms(znak)
print(f'Cena zpravy je {cena} Kc')   