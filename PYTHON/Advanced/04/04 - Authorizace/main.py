import pickle
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def prihlaseni():
    frame = Frame(okno, bd=10)
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
            messagebox.showinfo('Vitej', 'Jsi příhlášen')
        else:
            messagebox.showerror('Error', 'Ups něco se pokazilo')
        pass


def registrace():
    label_error = None

    frameReg = Frame(okno, background="#8BA4A8", bd=10)
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


okno = Tk()
okno.geometry("700x500")
okno.resizable(False, False)
okno.option_add("*Font", 'Corbel')

photo_bg = Image.open("background.jpg")
resized_image= photo_bg.resize((700,500))
photo = ImageTk.PhotoImage(resized_image)

background_image = Label(okno, image=photo)
background_image.place(relwidth=1, relheight=1)

Prihlaseni = Button(okno, text="Přihlásit se", command=prihlaseni)
Prihlaseni.place(relx=0.2, rely=0.2, relwidth=0.3)

Registrace = Button(okno, text="Registrovat se", command=registrace)
Registrace.place(relx=0.5, rely=0.2, relwidth=0.3)

okno.mainloop()