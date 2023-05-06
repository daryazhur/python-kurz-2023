"""
Zkopíruj si obsah souboru posta.txt do regex101 jako testovací řetězec. 
Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu. 
Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 nebo 742 45 FULNEK. 
Celkem by jich mělo být 18.
"""

import re
regularni_vyraz = re.compile(r"^[\d ]+[\w ]*[\d]*")


