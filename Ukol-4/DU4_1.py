"""
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
- Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
    -> První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud 
    je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, 
    jinak vrátí hodnotu False.
- Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
    -> Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. 
- Pokud není platné, vypíše chybu
- V opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:
- Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
- Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s 
řetězcem "+420".
"""
def telefonni_cislo(cislo):
    if len(cislo) == 9: 
        return True 
    if len(cislo) == 13:
        if cislo[:2] == '+420':
            return True
        return True    
    else:
        return False
            
cislo=(str(input('Zadejte svoje telefonni cislo: ')))
tel = telefonni_cislo(cislo)
print(tel)

def sms(text):
    return(int(len(text)/180)+1)*3 

text = input('Napiste zpravu: ')
cena = sms(text)
print(f'Cena zpravy je {cena} Kc')   
