sort = []
temp = None
while(temp != "-"):
    temp = input("Zadej temp: ")
    temp = temp.lower()
    if temp != "-":
        sort.append(temp)

print("Seznam před: ", sort)
sort.sort()
print("Seznam po: ", sort)
