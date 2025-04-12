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
# 1, 2, 3, --> možnosti
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
            soubor = open("hry.txt", mode="r", encoding="utf-8")
            print("Zobrazuji hry...")
            print("Je zde", len(hry), "her")
            temp = soubor.readlines()
            print(temp)
        elif vyber == 2:
            soubor = open("hry.txt", mode="w", encoding="utf-8")
            print("Přídání hry...")
            jmeno = input("Zadej jméno hry: ")
            hry.append(jmeno.lower() + "\n")
            soubor.writelines(hry)
            soubor.close()
        elif vyber == 3:
            print("Odebírám hru...")
            jmeno = input("Zadej jméno existujicí hry: ")
            hry.remove(jmeno.lower())
            soubor = open("hry.txt", mode="w", encoding="utf-8")
            #Dopiš mazání věcí
        elif vyber == 0:
            break
    else:
        print("Zadej správnou volbu!")
