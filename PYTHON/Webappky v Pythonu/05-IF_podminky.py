rychlost = input("Zadej rychlost: ")
rychlost = int(rychlost)

if rychlost <= 50:
    print("Jedete v obci.")
elif rychlost > 50 and rychlost <= 90:
    print("Jedete mimo obec.")
elif rychlost > 90 and rychlost <= 130:
    print("Jedete na dálnici.")
else:
    print("Jedete moc rychle.")
