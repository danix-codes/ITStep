import random
import time
import threading


def program():
    seznam = []
    pokracuj = True

    # while(pokracuj):
    #     cislo = input("Zadej cislo: ")
    #     if cislo.isnumeric():
    #         seznam.append(int(cislo))
    #     else:
    #         pokracuj = False

    n = int(input("Zadej počet čísel na vygen.: "))
    for i in range(n):
        nahodneCislo = random.randint(0, 32000)
        seznam.append(nahodneCislo)

    # print("Seznam Pred: ", seznam)

    temp = None
    start = time.time()
    for i in range(len(seznam) - 1):
        for j in range(0, len(seznam) - i - 1):
            if (seznam[j] > seznam[j + 1]):
                temp = seznam[j]
                seznam[j] = seznam[j + 1]
                seznam[j + 1] = temp

    end = time.time()

    b = temp
    a = b
    temp = a
    print("Trvalo to: ", end - start, "sekund")
    print("seznam Po: ", seznam)

t1 = threading.Thread(program())
t2 = threading.Thread(program())
t3 = threading.Thread(program())
t4 = threading.Thread(program())
t5 = threading.Thread(program())
t6 = threading.Thread(program())
t7 = threading.Thread(program())
t8 = threading.Thread(program())

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()