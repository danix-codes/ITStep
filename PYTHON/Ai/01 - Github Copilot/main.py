import tkinter as tk
from tkinter import messagebox
import datetime
import tkinter.ttk as ttk

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Základní okno TKInteru")
root.geometry("600x400")

# Spuštění hlavní smyčky
# Proměnné pro ukládání událostí
events = {}

# Funkce pro přidání události
def add_event():
    def save_event():
        day = day_var.get()
        time = time_var.get()
        event = event_var.get()
        description = description_var.get()
        if day and time and event:
            if day not in events:
                events[day] = {}
            events[day][time] = (event, description, datetime.datetime.now())
            update_table()
            add_event_window.destroy()

    add_event_window = tk.Toplevel(root)
    add_event_window.title("Přidat událost")

    tk.Label(add_event_window, text="Den v týdnu:").grid(row=0, column=0)
    day_var = tk.StringVar()
    day_options = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
    day_menu = ttk.Combobox(add_event_window, textvariable=day_var, values=day_options)
    day_menu.grid(row=0, column=1)

    tk.Label(add_event_window, text="Čas:").grid(row=1, column=0)
    time_var = tk.StringVar()
    tk.Entry(add_event_window, textvariable=time_var).grid(row=1, column=1)

    tk.Label(add_event_window, text="Událost:").grid(row=2, column=0)
    event_var = tk.StringVar()
    tk.Entry(add_event_window, textvariable=event_var).grid(row=2, column=1)

    tk.Label(add_event_window, text="Popis:").grid(row=3, column=0)
    description_var = tk.StringVar()
    tk.Entry(add_event_window, textvariable=description_var).grid(row=3, column=1)

    tk.Button(add_event_window, text="Uložit", command=save_event).grid(row=4, column=0, columnspan=2)

# Funkce pro aktualizaci tabulky
def update_table():
    for row in tree.get_children():
        tree.delete(row)
    for day, times in events.items():
        for time, (event, description, created_at) in times.items():
            tree.insert("", "end", values=(day, time, event, description))

# Funkce pro smazání události
def delete_event():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        day, time, event, description = item['values']
        del events[day][time]
        if not events[day]:
            del events[day]
        update_table()

# Funkce pro otevření události
def open_event():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        day, time, event, description = item['values']
        created_at = events[day][time][2]
        messagebox.showinfo("Detail události", f"Den: {day}\nČas: {time}\nUdálost: {event}\nPopis: {description}\nDatum vytvoření: {created_at}")

# Vytvoření rámce pro tabulku
table_frame = tk.Frame(root)
table_frame.pack()

# Přidání tabulky
columns = ("Den", "Čas", "Událost", "Popis")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.column(col, width=150)
    tree.heading(col, text=col)
tree.pack()

# Vytvoření rámce pro tlačítka
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Tlačítka pro přidání, smazání a otevření události
tk.Button(button_frame, text="Přidat událost", command=add_event, width=20, height=2).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(button_frame, text="Smazat událost", command=delete_event, width=20, height=2).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(button_frame, text="Otevřít událost", command=open_event, width=20, height=2).pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()