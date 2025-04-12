print("Jakou chceš pizzu?")
print("1. 33cm")
print("2. 40cm")
print("3. 50cm")
print("4. s Extra sýrem")
print("5. vyzvednuti v pizerii")
print("6. Dovoz domu")
vyber = input("Vyber si (můžeš vybrat více možností oddělených čárkou): ")

total_price = 0
discount_applied = False

for char in vyber:
    if char == "1":
        print("Vybral jsi si pizzu 33cm. Stoji 180kč")
        total_price += 180
    elif char == "2":
        print("Vybral jsi si pizzu 40cm. Stoji 270kč")
        total_price += 270
    elif char == "3":
        print("Vybral jsi si pizzu 50cm. Stoji 380kč")
        total_price += 380
    elif char == "4":
        print("Vybral jsi si pizzu s Extra sýrem. Stoji přídavné 20kč")
        total_price += 20
    elif char == "5":
        if not discount_applied:
            print("Vybral jsi si vyzvednuti v pizerii. 10% sleva")
            total_price *= 0.9
            discount_applied = True
    elif char == "6":
        print("Vybral jsi si Dovoz domu. Stojí přídavné 49kč")
        total_price += 49
    elif char == "," or char == " ":
        continue
    else:
        print(f"Neplatná volba: {char}")

if total_price >= 500:
    print("Pro ceny nad 500kč je dovoz zdarma")

print(f"Celková cena je: {total_price:.2f}kč")
