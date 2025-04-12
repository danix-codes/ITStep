from tkinter import *

# Proměnné, funkce a parametry
def vlozit():
    entry.insert(0, "Ahoj")

def smazat():
    entry.delete(0, END)

okno1 = Tk()
okno1.title("Moje první okno")
okno1.geometry("800x600")

text1 = Label(text="Ahoj světe!", font=('Arial', 16, 'bold'))
text1.config(bd=50, background='yellow')
text1.pack()

entry = Entry(width=60)
entry.pack()

tlacitkoVloz = Button(text="Uložit", bg='Green', width=10, height=1)
tlacitkoVloz.config(command=vlozit)
tlacitkoVloz.pack()

tlacitkoSmazat = Button(text="Smazat", bg='Red', width=10, height=1)
tlacitkoSmazat.config(command=smazat)
tlacitkoSmazat.pack()

# Spouštění
okno1.mainloop()
print("Aplikace skončila úspěšně.")
