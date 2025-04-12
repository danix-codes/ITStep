rychlost = int(input("Zadej rychlost: "))
if rychlost <= 50:
    print("Jedeš v obci.")
elif rychlost > 90 and rychlost < 130:
    print("Jedeš na dálnici.")
elif rychlost > 50 and rychlost <= 90:
    print("Jedeš mimo obec.")
elif rychlost > 130:
    print("Jedeš moc rychle. Jedeš rychlostí", rychlost, "km/h.")