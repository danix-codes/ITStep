import tkinter as tk

def vypis(slovo, pocet):
    for i in range(pocet):
        print(slovo)

def zobraz_hry():
    label.config(text=f"Je zde {len(hry)} her\n{hry}")

def pridej_hru():
    jmeno = entry.get()
    hry.append(jmeno.lower())
    entry.delete(0, 'end')

def odeber_hru():
    jmeno = entry.get()
    if jmeno.lower() in hry:
        hry.remove(jmeno.lower())
    entry.delete(0, 'end')

def vyber_možnost():
    vyber = vyber_var.get()
    if vyber == 1:
        zobraz_hry()
    elif vyber == 2:
        pridej_hru()
    elif vyber == 3:
        odeber_hru()
    elif vyber == 0:
        root.quit()
    else:
        print("Zadej správnou volbu!")

hry = []

root = tk.Tk()
root.title("Herní menu")

label = tk.Label(root, text="!##############! Vítám tě hráči! !##############!")
label.pack()

label2 = tk.Label(root, text="Vítej v menu")
label2.pack()

vyber_var = tk.IntVar()
vyber_var.set(-1)

options_frame = tk.Frame(root)
options_frame.pack()

moznost1 = tk.Radiobutton(options_frame, text="Zobraz hry", variable=vyber_var, value=1)
moznost2 = tk.Radiobutton(options_frame, text="Přidej hry", variable=vyber_var, value=2)
moznost3 = tk.Radiobutton(options_frame, text="Odeber hry", variable=vyber_var, value=3)
moznost4 = tk.Radiobutton(options_frame, text="Ukonči program", variable=vyber_var, value=0)

moznost1.grid(row=0, column=0)
moznost2.grid(row=0, column=1)
moznost3.grid(row=0, column=2)
moznost4.grid(row=0, column=3)

label_jmeno = tk.Label(root, text="Zadej jméno hry:")
label_jmeno.pack()
entry = tk.Entry(root)
entry.pack()

tlacitko_potvrdit = tk.Button(root, text="Potvrdit", command=vyber_možnost)
tlacitko_potvrdit.pack()

root.mainloop()
