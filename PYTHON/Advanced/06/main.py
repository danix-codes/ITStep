from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk

HEIGHT = 600
WIDTH = 600

ukoly = []


def update_listbox():
    listbox.delete(0, END)
    for ukol in ukoly:
        listbox.insert(END, ukol)


def add_task():
    ukol = text_input.get()
    if ukol != '':
        ukoly.append(ukol)
        update_listbox()
    else:
        messagebox.showwarning('Varování', "Nebyl zadán žádný ukol!!!")
    text_input.delete(0, END)

    pass


def del_one():
    ukolsmazat = listbox.get('active')
    if ukolsmazat in ukoly:
        ukoly.remove(ukolsmazat)
    update_listbox()

    pass


def del_all():
    opravdu = messagebox.askyesno('Opravdu smazat?', 'Chcete opravdu smazat všechny ukoly?')
    if opravdu:
        global ukoly
        ukoly = []
        update_listbox()
    pass


def sort_asc():
    ukoly.sort(reverse=False)
    update_listbox()

def sort_desc():
    ukoly.sort(reverse=True)
    update_listbox()

def choose_random():
    ukol = random.choice(ukoly)
    label_display['text'] = ukol

def show_number_of_tasks():
    delka = len(ukoly)
    label_display['text'] = delka

def generuj():
    ukoly_texty = [
        "Dokonči domácí úkol z matematiky",
        "Přečti kapitolu z knihy",
        "Procvič psaní na klávesnici",
        "Vypracuj referát do školy",
        "Procvič si slovní zásobu v angličtině",
        "Namaluj obrázek",
        "Vyřeš logickou hádanku",
        "Zahraj si vzdělávací hru",
        "Připrav si oblečení na zítra",
        "Udělej si pořádek v pokoji",
        "Umyj nádobí",
        "Pohraj si venku",
        "Nakrm domácího mazlíčka",
        "Procvič si násobilku",
        "Naplánuj si den",
        "Vytvoř si seznam úkolů",
        "Zalij květiny",
        "Pomoz rodičům s nákupem",
        "Podívej se na vzdělávací video",
        "Napiš dopis kamarádovi",
        "Procvič si hru na hudební nástroj",
        "Nauč se něco nového o přírodě",
        "Naplánuj si výlet",
        "Připrav jednoduché jídlo",
        "Udělej si pořádek v počítači",
        "Vytvoř si deník",
        "Zaznamenej si svoje nápady",
        "Udělej si cvičení nebo jógu",
        "Přečti si článek o vědě",
        "Nauč se nový tanec"
    ]
        

root = Tk()
root.geometry("%dx%d" % (WIDTH, HEIGHT))
root.title("Můj TO DO list")

image = Image.open("background.jpg")
resized_image = image.resize((WIDTH, HEIGHT))
photo = ImageTk.PhotoImage(resized_image)

background_label = Label(root, image=photo)
background_label.place(relwidth=1, relheight=1)

root.option_add('*Font', '{Comic Sans MS} 10')
root.option_add('*Background', 'white')

frame = Frame(root, bd=10)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

title_label = Label(frame, text="Můj užasný TO DO list", fg='magenta', font='{Comic Sans MS} 16')
title_label.place(relx=0.3, rely=0)

button_generate = Button(frame,text="Generuj",command=generuj)
button_generate.place(rely=0.7,relwidth=0.25)

label_display = Label(frame, text='')
label_display.place(relx=0.3, rely=0.1)

text_input = Entry(frame, width=15)
text_input.place(relx=0.3, rely=0.15, relwidth=0.6)

# Buttons
button_add_task = Button(frame, text='Add task', command=add_task)
button_add_task.place(rely=0.15, relwidth=0.25)

button_del = Button(frame, text='Delete', command=del_one)
button_del.place(rely=0.25, relwidth=0.25)

button_del_all = Button(frame, text='Delete All', command=del_all)
button_del_all.place(rely=0.35, relwidth=0.25)

button_sort_asc = Button(frame, text='Sort (A-Z)', command=sort_asc)
button_sort_asc.place(rely=0.45, relwidth=0.25)

button_sort_desc = Button(frame, text='Sort (Z-A)', command=sort_desc)
button_sort_desc.place(rely=0.55, relwidth=0.25)

button_random = Button(frame, text='Choose Random', command=choose_random)
button_random.place(rely=0.65, relwidth=0.25)

button_number_of_tasks = Button(frame, text='Number of Tasks', command=show_number_of_tasks)
button_number_of_tasks.place(rely=0.75, relwidth=0.25)

button_exit = Button(frame, text='Exit', command=exit)
button_exit.place(rely=0.85, relwidth=0.25)

listbox = Listbox(frame)
listbox.place(relx=0.3, rely=0.24, relwidth=0.6, relheight=0.6)

root.mainloop()