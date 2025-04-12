import os.path
import colorama

print("!##############! Vítám tě hráči! !##############!")
vyber = None
hry = []
jmenoSouboru = "jmeno.pripona"

colorama.init(autoreset=True)

# Funkce
print("Pro zacatek vyber soubor ze kterého číst a zapisovat")
print("!!!Soubor musí být ve stejné složce jako .py program!!!")
print("!!!a musí být za jménem také připona soubory(.txt, .docx,...)!!!")
counter = 0
while counter == 0:
    jmenoS = input("Zadej jméno souboru: ")
    if os.path.isfile(jmenoS):
        print(colorama.Fore.GREEN + "Správný název souboru, pokračuji...")
        counter = counter + 1
        jmenoSoubor = jmenoS
    else:
        print(colorama.Fore.RED + "Špatný název souboru")


def zobraz_hry():
    print("Zobrazuji hry...")
    with open(jmenoSouboru, "r") as soubor:
        obsah = soubor.read()
        if not obsah:
            print("Žádné hry nebyly nalezeny.")
            soubor.close()
        else:
            seznam_her = obsah.split("\n")
            print("Je zde", len(seznam_her), "her")
            for hra in seznam_her:
                print(hra)
                soubor.close()


def pridej_hru():
    print("Přídání hry...")
    jmeno = input("Zadej jméno hry: ")
    hry.append(jmeno.lower())
    uloz_do_souboru()


def odeber_hru():
    print("Odebírám hru...")
    jmeno = input("Zadej jméno existující hry: ")
    if jmeno.lower() in hry:
        hry.remove(jmeno.lower())
        uloz_do_souboru()
    else:
        print("Hra nenalezena.")


def uloz_do_souboru():
    with open(jmenoSoubor, "w") as soubor:
        for hra in hry:
            soubor.write(hra + "\n")
        soubor.close()


# Hlavní smyčka programu
while vyber != 0:
    print("[1] Zobraz hry")
    print("[2] Přidej hry")
    print("[3] Odeber hry")
    print("[0] Ulož a ukonči program")
    vyber = input("Vyber si možnost: ")

    if vyber.isnumeric():
        vyber = int(vyber)

        if vyber == 1:
            zobraz_hry()
        elif vyber == 2:
            pridej_hru()
        elif vyber == 3:
            odeber_hru()
        elif vyber == 0:
            break
    else:
        print("Zadej správnou volbu!")
