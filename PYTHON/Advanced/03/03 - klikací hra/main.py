from tkinter import *

bomb = 100
score = 0

enter_press = True


def start(event):
    global bomb
    global score
    global enter_press
    if not enter_press:
        pass
    else:
        bomb = 100
        score = 0
        title.config(text='')
        update_bomb()
        update_point()
        update_display()
        enter_press = False


def update_display():
    global bomb
    global score
    if bomb > 50:
        obr_label.config(image=obr1)
    elif 0 < bomb <= 50:
        obr_label.config(image=obr2)
    else:
        obr_label.config(image=obr3)
    score_label.config(text="Score: " + str(score))
    fuse_label.config(text="Fuse: " + str(bomb))
    fuse_label.after(100, update_display)


def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)


def update_point():
    global score
    score += 1
    if is_alive():
        fuse_label.after(3000, update_point)


def click():
    global bomb
    if is_alive():
        bomb += 1


def is_alive():
    global bomb
    global enter_press
    if bomb <= 0:
        title.config(text="Bum prásk")
        enter_press = True
        return False
    else:
        return True


okno = Tk()
okno.title("Tic Tac Booom")
okno.geometry("500x700")

title = Label(okno, text="Pro start hry zmáčkni [Enter]", font=('Comic Sans MS', 12))
title.pack()

fuse_label = Label(okno, text="Fuse: " + str(bomb), font=('Comic Sans MS', 12))
fuse_label.pack()

score_label = Label(okno, text="Score: " + str(score), font=('Comic Sans MS', 12))
score_label.pack()

obr1 = PhotoImage(file="1.gif").subsample(2)
obr2 = PhotoImage(file="2.gif").subsample(2)
obr3 = PhotoImage(file="3.gif").subsample(2)

obr_label = Label(okno, image=obr1)
obr_label.pack()

click_tlacitko = Button(okno, text="Klikni", bg="black", fg="white", font=('Comic Sans MS', 14), command=click)
click_tlacitko.pack()

okno.bind('<Return>', start)

okno.mainloop()