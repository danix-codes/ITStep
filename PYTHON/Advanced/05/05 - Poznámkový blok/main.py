import pickle
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# Funkce
def save_file():
    file_name = filedialog.asksaveasfilename(initialdir='/',
                                             title='Vyberte umístění',
                                             filetypes=(('Textové dokumenty', '*.txt'),
                                                        ('Bez přípony', '*.*')))

    if file_name:
        f = open(file_name, 'w')
        textToSave = str(text.get(1.0, END))
        f.write(textToSave + '\n')

def open_file():
    file_name = filedialog.askopenfilename(initialdir='/',
                                           title='Vyberte soubor',
                                           filetypes=(('Textové dokumenty', '*.txt'),
                                                        ('Bez přípony', '*.*')))
    if file_name:
        f = open(file_name, "r")
        text_open = f.read()
        if text_open:
            text.delete(1.0, END)
            text.insert(END, text_open)


def new_file():
    text.delete(1.0, END)

# Hlavní okno
def main_note_window():
    main = Tk()
    main.title("Poznámkový blok")
    main.geometry("400x500")
    main.resizable(False, False)
    main.option_add("*Font", 'Corbel')

    label_welcome = Label(text="Vítejte v poznámkovém bloku!")
    label_welcome.config(bd=30)
    label_welcome.pack()

    menu = Menu(main)
    main.config(menu=menu)

    file_menu = Menu(menu, tearoff=0)
    file_menu.add_command(label='Nová poznámka', command=new_file)
    file_menu.add_command(label='Otevřít poznámku', command=open_file)
    file_menu.add_command(label='Uložit poznámku', command=save_file)

    help_menu = Menu(menu, tearoff=0)
    help_menu.add_command(label="Vytvoření poznámky")
    help_menu.add_command(label="Uložení poznámky")
    help_menu.add_command(label="Otevírání poznámky")

    menu.add_cascade(label='Soubor', menu=file_menu)
    menu.add_cascade(label='Nápověda', menu=help_menu)

    text = Text(main)
    text.pack(expand=YES, fill=BOTH)

    main.mainloop()

def prihlaseni():
    frame = Frame(login_window, background="#8BA4A8", bd=10)
    frame.place(relx=0.5, rely=0.3,
                relwidth=0.7, relheight=0.6,
                anchor='n')
    label = Label(frame, text="Přihlášení", bg="#8BA4A8")
    label.pack()

    login_label = Label(frame, text="Login: ", bg="#8BA4A8")
    login_label.place(rely=0.2, relx=0.2, relwidth=0.25)

    login_prihlaseni = Entry(frame)
    login_prihlaseni.place(rely=0.2, relx=0.5, relwidth=0.3)

    password_label = Label(frame, text="Heslo: ", bg="#8BA4A8")
    password_label.place(rely=0.4, relx=0.2, relwidth=0.25)

    password_prihlaseni = Entry(frame)
    password_prihlaseni.place(rely=0.4, relx=0.5, relwidth=0.3)

    button_prihlaseni = Button(frame, text="Příhlásit se", command=lambda: odeslat())
    button_prihlaseni.place(relx=0.25, rely=0.8, relheight=0.15, relwidth=0.5)

    def odeslat():
        soubor = open("login.txt", "rb")
        data = pickle.load(soubor)
        soubor.close()
        if login_prihlaseni.get() in data and password_prihlaseni.get() == data[login_prihlaseni.get()]:
            login_window.destroy()
            main_note_window()
        else:
            messagebox.showerror('Error', 'Ups něco se pokazilo')
        pass


def registrace():
    label_error = None

    frameReg = Frame(login_window, background="#8BA4A8", bd=10)
    frameReg.place(relx=0.5, rely=0.3,
                   relwidth=0.7, relheight=0.6,
                   anchor='n')
    labelReg = Label(frameReg, text="Registrace", bg="#8BA4A8")
    labelReg.pack()

    login_label = Label(frameReg, text="Login: ", bg="#8BA4A8")
    login_label.place(rely=0.2, relx=0.2, relwidth=0.25)

    login_register = Entry(frameReg)
    login_register.place(rely=0.2, relx=0.5, relwidth=0.3)

    password_label = Label(frameReg, text="Heslo: ", bg="#8BA4A8")
    password_label.place(rely=0.4, relx=0.2, relwidth=0.25)

    password_register = Entry(frameReg)
    password_register.place(rely=0.4, relx=0.5, relwidth=0.3)

    password1_label = Label(frameReg, text="Heslo znovu: ", bg="#8BA4A8")
    password1_label.place(rely=0.6, relx=0.15, relwidth=0.3)

    password1_register = Entry(frameReg)
    password1_register.place(rely=0.6, relx=0.5, relwidth=0.3)

    button_register = Button(frameReg, text="Registrovat", command=lambda: odeslat())
    button_register.place(relx=0.25, rely=0.8, relheight=0.15, relwidth=0.5)

    def odeslat():
        nonlocal label_error
        error = ''

        if label_error:
            label_error.destroy()

        if password1_register.get() != password_register.get():
            error = "Hesla se neshodují"
        elif len(password_register.get()) < 6:
            error = "Heslo je příliš krátké"
        elif len(login_register.get()) < 1:
            error = "Chybí uživatelské jméno"
        else:
            save()

        label_error = Label(frameReg, text=error, fg='red')
        label_error.place(rely=0.6)

    def save():
        data = dict()
        data[login_register.get()] = password1_register.get()
        soubor = open("login.txt", "wb")
        pickle.dump(data, soubor)
        soubor.close()
        prihlaseni()
        pass


login_window = Tk()
login_window.geometry("700x500")
login_window.resizable(False, False)
login_window.option_add("*Font", 'Corbel')


Prihlaseni = Button(login_window, text="Přihlásit se", command=prihlaseni)
Prihlaseni.place(relx=0.2, rely=0.2, relwidth=0.3)

Registrace = Button(login_window, text="Registrovat se", command=registrace)
Registrace.place(relx=0.5, rely=0.2, relwidth=0.3)

# Spouštění
login_window.mainloop()
