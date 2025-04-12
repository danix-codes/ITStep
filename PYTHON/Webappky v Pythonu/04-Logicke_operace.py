rychly = True
chytry = True
print(rychly and chytry)    # True, pokud jsou oba True, jinak False

pomaly = True
hloupy = False
print(pomaly or hloupy)     # True, pokud je alespon jeden True, jinak False

borec = False
print(not borec)            # Vrati opacnou hodnotu

print(chytry and not pomaly or hloupy)    # False, pokud je alespon jeden False, jinak True


