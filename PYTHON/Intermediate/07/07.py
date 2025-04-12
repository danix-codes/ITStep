import random

soucet = -1
soucin = -2
pocitadlo = 0
prvniCislo = None
druheCislo = None
tretiCislo = None
ctvrteCislo = None
pateCislo= None

while soucet != soucin:
    prvniCislo = random.randint(1, 50)
    druheCislo = random.randint(1, 50)
    tretiCislo = random.randint(1, 50)
    ctvrteCislo = random.randint(1, 50)
    pateCislo = random.randint(1, 50)
    
    soucet = prvniCislo + druheCislo + tretiCislo + ctvrteCislo + pateCislo
    soucin = prvniCislo * druheCislo * tretiCislo * ctvrteCislo * pateCislo
    pocitadlo +=1
    
print("Nalezeny cisla", prvniCislo, druheCislo, tretiCislo, ctvrteCislo, pateCislo)
print("Na",pocitadlo,"pokusu")