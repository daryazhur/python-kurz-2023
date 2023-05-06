"""
Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:
    platná data:
        2.2.2022
        13. 8. 1999
        4/5/2001
    neplatná data:
        5.123.458.91
        21.4
        8./9
"""

import re

regularni_vyraz = re.compile(r"(\d\.? ?\d\. ?\d{4})|(\d\/? ?\d\/ ?\d{4})")

data = input('Zadej datum: ')

data_ok = regularni_vyraz.fullmatch(data)

print(data_ok)

if data_ok:
    print('Datum je platne')
else:
    print('Datum neni platne')    