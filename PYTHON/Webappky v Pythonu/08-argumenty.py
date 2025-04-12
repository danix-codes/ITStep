import sys

def rezervace_letenky(jmeno, destinace, trida):
    if jmeno not in ["Daniel", "Bob", "Jirka", "Petr", "Karel", "Jana", "Eva", "Marie", "Lenka", "Lucie"]:
        print(f"Chyba: Pasazér {jmeno} neexistuje.")
        return

    if trida not in ["economy", "business", "first"]:
        print(f"Chyba: Třída {trida} neexistuje.")
        return

    print(f"Rezervace potvrzena pro {jmeno} do destinace {destinace} ve třídě {trida}.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        jmeno = input("Zadejte jméno: ")
        destinace = input("Zadejte destinaci: ")
        print("Vyberte třídu: economy, business, first")
        trida = input("Zadejte třídu: ")
        rezervace_letenky(jmeno, destinace, trida)
    else:
        rezervace_letenky(sys.argv[1], sys.argv[2], sys.argv[3])
