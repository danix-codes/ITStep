from tkinter import *
from tkinter import colorchooser


class KresliciAplikace:
    def __init__(self, okno) -> None:
        self.okno = okno
        self.okno.title("Kreslici aplikace")

        self.canvas = Canvas(okno, bg='white', width=800, height=600)
        self.canvas.pack()

        self.color_button = Button(okno, text="Vyber barvu", command=self.vyber_barvu)
        self.color_button.pack()

        self.vymaz_button = Button(okno, text="Vymazat", command=self.vymazat)
        self.vymaz_button.pack()

        self.barva = 'black'
        self.canvas.bind('<B1-Motion>', self.kresli)

    def vyber_barvu(self):
        self.barva = colorchooser.askcolor(color=self.barva)[1]

    def vymazat(self):
        self.canvas.delete('all')

    def kresli(self, event):
        x = event.x
        y = event.y
        r = 3
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.barva, outline=self.barva)


okno = Tk()
aplikce = KresliciAplikace(okno)
okno.mainloop()
