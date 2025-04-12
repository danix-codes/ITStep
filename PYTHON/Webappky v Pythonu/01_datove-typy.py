# Datove typy
## STRING = text
## INTEGER = cele cislo
## FLOAT = desetinne cislo
## BOOLEAN = True/False
#pozdrav = "Ahoj"
#cislo = 42
#desetinne_cislo = 3.14
#print(pozdrav)
#print(cislo)
#print(desetinne_cislo)
#Doucovani = True
#if (Doucovani == True):
#   print("Jsem doucovatel")

## list = seznam
#Znamky = [1, 2, 3, 4, 5]
#predmety = ["Matematika", "Fyzika", "AJ"]


znamka1 = int(input("Zadej prvni znamku: "))
znamka2 = int(input("Zadej druhou znamku: "))
znamka3 = int(input("Zadej treti znamku: "))
znamka4 = int(input("Zadej ctvrtou znamku: "))
znamka5 = int(input("Zadej patou znamku: "))
znamka6 = int(input("Zadej sestou znamku: "))
znamka7 = int(input("Zadej sedmou znamku: "))
znamka8 = int(input("Zadej osmou znamku: "))
znamka9 = int(input("Zadej devatou znamku: "))
znamka10 = int(input("Zadej desatou znamku: "))

# Tady se vypocte prumer
prumer = (znamka1 + znamka2 + znamka3 + znamka4 + znamka5 + znamka6 + znamka7 + znamka8 + znamka9 + znamka10) / 10

# Tady vypiseme prumer
print("Prumer znamek je: " + str(prumer))
print("Tento program je funkci a dosel na konec kodu!")