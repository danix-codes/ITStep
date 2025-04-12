#Program, ktery bude generovat cisla podle rozmezi ktere zada uzivatel a tyto
#cisla vlozi do listu a ten list následně uloží do souboru.
import random

cisla_list = []

#Získávání Informací
rozmezi_od = int(input("Od kolikati chceš generovat čísla?: "))
rozmezi_do = int(input("Do kolikati chceš generovat čísla?: "))
pocet = int(input("Kolik chces cisel?: "))

#Tvoření čísel a vkladani do listu
for i in range(pocet):
    nahodneCisla = random.randint(rozmezi_od, rozmezi_do)
    cisla_list.append(str(nahodneCisla) + "\n")

print("Do listu se úspěšně přidaly tyto čísla:", cisla_list)
potvrzeni = input("Chcete tyto čísla přidat do souboru cisla.txt?(Y nebo N): ")
if potvrzeni == "Y":
    soubor = open("cisla.txt", mode="w", encoding="utf-8")
    soubor.writelines(cisla_list)
    soubor.close()