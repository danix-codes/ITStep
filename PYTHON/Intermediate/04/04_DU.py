import colorama

# Initialize colorama
colorama.init()

print(colorama.Fore.YELLOW + "Vítej v počitateli času!")
print(colorama.Fore.YELLOW + "-------------------------")
print(colorama.Fore.YELLOW + "Vyber si možnost")
print(colorama.Fore.YELLOW + "1. Převod na sekundy")
print(colorama.Fore.YELLOW + "2. Převod z Sekund na Hodiny")
print(colorama.Fore.YELLOW + "-------------------------")

while True:
    volba = input("Vyber si možnost: ")

    if volba.isnumeric():
        volba = int(volba)

        if 1 <= volba <= 2:
            break
        else:
            print(colorama.Fore.RED + "Špatná volba! Zadej znovu!")
    else:
        print(colorama.Fore.RED + "Špatná volba! Zadej znovu!")

if volba == 1:
    # Převod na sekundy
    hodiny = int(input("Zadej počet hodin: "))
    minuty = int(input("Zadej počet minut: "))
    sekundy = hodiny * 3600 + minuty * 60
    print(colorama.Fore.GREEN + f"Celkem sekund: {sekundy}")
elif volba == 2:
    # Převod z sekund na hodiny
    sekundy = int(input("Zadej počet sekund: "))
    hodiny = sekundy // 3600
    minuty = (sekundy % 3600) // 60
    print(colorama.Fore.GREEN + f"Celkem hodin: {hodiny}, minut: {minuty}")

colorama.deinit()
