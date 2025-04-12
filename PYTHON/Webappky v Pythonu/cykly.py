from random import randint


ADMIN_PASSWORD = "tajne123"

"""
while True:
    user_pass = input("zadej heslo: ")

    if user_pass == ADMIN_PASSWORD:
        break

print("si prihlasen")"""

def play_game():
    pc_number = randint(1, 10)
    counter = 0
    while True:
        n = int(input("hadaj cislo: "))
        counter += 1

        if n < pc_number:
            print("zadal si mensie cislo")

        elif n > pc_number:
            print("zadal si vecsie cislo")

        else:
            break

    print(f"uhadol si na {counter} pokus")

#play_game()

def say_hello(name):
    # kod
    return f"Hello, {name}"


text1 = say_hello("Adam")
text2 = say_hello("Eva")

print(text1) 