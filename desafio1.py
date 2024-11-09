import tkinter as tk
import csv
import tkinter.messagebox
import os

def initialize_csv():
    if not os.path.isfile('notas.csv'):
        with open('notas.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre', 'Nota'])

def save_data():
    name = entry_name.get()
    grade = entry_grade.get()
    
    if name == "" or grade == "":
        tkinter.messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
        return

    try:
        grade = int(grade)
    except ValueError:
        tkinter.messagebox.showerror("Error", "La nota debe ser un número.")
        return
    
    with open('notas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, grade])
    
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    tkinter.messagebox.showinfo("Éxito", "Datos guardados correctamente.")

root = tk.Tk()
root.title("Gestor de Notas")

initialize_csv()

label_name = tk.Label(root, text="Nombre:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_grade = tk.Label(root, text="Nota:")
label_grade.pack()

entry_grade = tk.Entry(root)
entry_grade.pack()

button_save = tk.Button(root, text="Guardar", command=save_data)
button_save.pack()

root.mainloop()
