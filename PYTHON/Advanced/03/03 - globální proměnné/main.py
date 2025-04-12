def vypis_her():
    global popis
    popis = "Nový výpis her"
    print(popis, "\n", id(popis))
    hra1, hra2, hra3 = "Farcry", "GTA", "My Summer Car"
    print(hra1, vyv1,"\n", hra2, vyv2,"\n", hra3, vyv3)

popis = "Můj výpis her"
vyv1, vyv2, vyv3 = "Ubisoft", "Rockstar", "Amistech"

vypis_her()
print(popis, "\n", id(popis))