def vypis(slovo, pocet):
    for i in range(pocet):
        print(slovo)

# temp = input("Co chces aby se vypsalo?: ")
# pocet = int(input("Kolik chces vypsat toto temp?: "))

# vypis(temp, temp)
print("!##############! Vítám tě hráči! !##############!")
print("Vítej v menu")
vyber = None
hry = []
#1, 2, 3, --> možnosti
# 0 --> Ukončit program
while (vyber != 0):
    print("[1] Zobraz hry")
    print("[2] Přidej hry")
    print("[3] Odeber hry")
    print("[0] Ukonči program")
    vyber = input("Vyber si možnost: ")

    if vyber.isnumeric():
        vyber = int(vyber)

        if vyber == 1:
            print("Zobrazuji hry...")
            print("Je zde", len(hry), "her")
            print(hry)
        elif vyber == 2:
            print("Přídání hry...")
            jmeno = input("Zadej jméno hry: ")
            hry.append(jmeno.lower())
        elif vyber == 3:
            print("odebírám hru...")
            jmeno = input("Zadej jméno existujicí hry: ")
            hry.remove(jmeno.lower())
        elif vyber == 0:
            break
    else:
        print("Zadej správnou volbu!")
