# def upravJmeno(upravene_jmeno):
#     noveJmeno1 = upravene_jmeno.upper()
#     noveJmeno2 = upravene_jmeno.lower()
#     return noveJmeno1, noveJmeno2

# jmeno = input("Zadej jmeno: ")
# print("Ahoj", upravJmeno(jmeno)) 
global cas
cas = int(input("Zadej cas v sekundach: "))
def casRozdeleniHodiny(cas):
    hodiny = cas // 3600
    return hodiny
def casRozdeleniMinuty(cas):
    minuty = (cas % 3600) // 60
    return minuty
def casRozdeleniSekundy(cas):
    sekundy = (cas % 3600) % 60
    return sekundy
vyber = input("Zadej co chces vypsat (hodiny, minuty, sekundy): ")
if vyber == "hodiny":
    print(casRozdeleniHodiny(cas))
elif vyber == "minuty":
    print(casRozdeleniMinuty(cas))
elif vyber == "sekundy":
    print(casRozdeleniSekundy(cas))
else:
    print("Neplatna volba")

