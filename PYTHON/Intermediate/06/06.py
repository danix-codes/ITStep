# from turtle import *
#
# a = Turtle()
# a.speed(200)
#
# turtle_soubor = open("kroky.turtlemap", "r")
# turtle_data = turtle_soubor.read()
# turtle_soubor.close()
# print(turtle_data)
# instrukce = turtle_data.split("|")
# print(instrukce)
#
# for i in instrukce:
#     print(i[0], "-", i[1:])
#     smer = i[0]
#     vzdalenost = i[1:]
#     vzdalenost = int(vzdalenost)
#
#     if smer == "F":
#         a.forward(vzdalenost)
#     elif smer == "B":
#         a.back(vzdalenost)
#     elif smer == "R":
#         a.left(vzdalenost)
#     elif smer == "L":
#         a.right(vzdalenost)
#
# done()

import turtle

turtle_soubor = open("kroky.turtlemap", mode="r", encoding="UTF-8")
turtle_data = turtle_soubor.read()
turtle_soubor.close()
print(turtle_data)
instrukce = turtle_data.split("|")
print(instrukce)

my_screen = turtle.Screen()
my_screen.setup(600, 600)
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
#
for i in instrukce:
    krok = i[0]
    if krok == "F":
        vzdalenost = int(i[1:])
        my_turtle.forward(vzdalenost)
    elif krok == "B":
        vzdalenost = int(i[1:])
        my_turtle.back(vzdalenost)
    elif krok == "L":
        stupne = int(i[1:])
        my_turtle.left(stupne)
    elif krok == "R":
        stupne = int(i[1:])
        my_turtle.right(stupne)

#
my_screen.exitonclick()