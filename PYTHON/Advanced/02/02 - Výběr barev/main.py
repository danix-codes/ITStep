from tkinter import *

# Proměnné, funkce a parametry
entryHistorie = []
entryHistorieTemp = ""
entryHistorieTemp_list = ""
entryHistorie_string = ""
def cervenaClicked():
    entryBarva.delete(0, END)
    entryBarva.insert(0, "Červená")
    entryBarva.config(background="Red")

def oranzovaClicked():
    entryBarva.delete(0, END)
    entryBarva.insert(0, "Oranžová")
    entryBarva.config(background="Orange", fg='Black')

def zlutaClicked():
    entryBarva.delete(0, END)
    entryBarva.insert(0, "Žlutá")
    entryBarva.config(background="Yellow", fg='Black')

def zelenaClicked():
    entryBarva.delete(0, END)
    entryBarva.insert(0, "Zelená")
    entryBarva.config(background="Green", fg='White')

def modraClicked():
    entryBarva.delete(0, END)
    entryBarva.insert(0, "Modrá")
    entryBarva.config(background="Blue", fg='White')

def tmaveModraClicked():
    entryBarva.delete(0, END)
    entryBarva.insert(0, "Tmavě modrá")
    entryBarva.config(background="Dark Blue", fg='White')

def fialovaClicked():
    entryBarva.delete(0, END)
    entryBarva.insert(0, "Fialová")
    entryBarva.config(background="Purple", fg='White')

def onEnter(event):
    entryPrompt = entryHledani.get()
    global entryHistorie, entryHistorieTemp,entryHistorieTemp_list, entryHistorie_string
    entryHistorieTemp = entryHledani.get()
    entryHistorieTemp_list = list(entryHistorieTemp)
    entryHistorieTemp_list = entryPrompt.split()
    entryHistorie += entryHistorieTemp_list
    entryHistorie_string = ", ".join(entryHistorie)
    entryHistorieTemp = ""
    entryHistorieTemp_list = ""
    if entryPrompt.lower() in ["červená", "cervena"]:
        cervenaClicked()
    elif entryPrompt.lower() in ["oranžová", "oranzova"]:
        oranzovaClicked()
    elif entryPrompt.lower() == "žlutá":
        zlutaClicked()
    elif entryPrompt.lower() == "zelená":
        zelenaClicked()
    elif entryPrompt.lower() == "modrá":
        modraClicked()
    elif entryPrompt.lower() in ["tmavě modrá", "tmavě modra", "tmave modrá", "tmave modra"]:
        tmaveModraClicked()
    elif entryPrompt.lower() in ["fialová", "fialova"]:
        fialovaClicked()
    update_text()

def update_text():
    textHistorie.config(text="Historie: " + entryHistorie_string)
    formatted_text = entryHistorie_string.replace(", ", "\n")
    textHistorie.config(text="Historie:\n" + formatted_text)

okno1 = Tk()
okno1.title("Výběr barev")
okno1.geometry("400x700")

nadpisOkna = Label(text="Výběr barev", font=('Corbel', 24, 'bold'))
nadpisOkna.config(bd=5)
nadpisOkna.pack()

jmenoBarvy = Label(text="Jméno/kód barvy: ", font=('Corbel', 8), width=20)
jmenoBarvy.config(bd=5)
jmenoBarvy.pack()

entryBarva = Entry(width=25)
entryBarva.pack()

text3 = Label(text="Vyhledávání: ", font=('Corbel', 8), width=20)
text3.config(bd=5)
text3.pack()

entryHledani = Entry(width=25)
entryHledani.pack()
entryHledani.bind('<Return>', onEnter)

spacer = Label(text="", font=('Corbel', 8), width=20, height=1)
spacer.config(bd=5)
spacer.pack()

cervena = Button(text="", bg='Red', width=30, height=3, command=cervenaClicked)
cervena.pack()

oranzova = Button(text="", bg='Orange', width=30, height=3, command=oranzovaClicked)
oranzova.pack()

zluta = Button(text="", bg='Yellow', width=30, height=3, command=zlutaClicked)
zluta.pack()

zelena = Button(text="", bg='Green', width=30, height=3, command=zelenaClicked)
zelena.pack()

modra = Button(text="", bg='Blue', width=30, height=3, command=modraClicked)
modra.pack()

tmaveModra = Button(text="", bg='Dark Blue', width=30, height=3, command=tmaveModraClicked)
tmaveModra.pack()

fialova = Button(text="", bg='Purple', width=30, height=3, command=fialovaClicked)
fialova.pack()


textHistorie = Label(text="", font=('Corbel', 8), width=20, height=50)
textHistorie.config(bd=5)
textHistorie.pack()

# Spouštění
okno1.mainloop()
print("Aplikace skončila úspěšně.")