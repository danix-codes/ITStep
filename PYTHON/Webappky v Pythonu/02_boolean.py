rychly = True
chytry = True

print(rychly and chytry) # True pokud jsou oba True, jinak False
print(rychly or chytry) # True pokud je alespon jeden True, jinak False

borec = False
print(not borec) # True pokud je borec False, jinak False

print(rychly and not borec) # True pokud je rychly True a borec False, jinak False