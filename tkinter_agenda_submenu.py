#!/usr/bin/env python3

import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from json import dump
from json import loads

def agregar():
	datos = {}
	
	datos["nombre"] = sd.askstring("Datos Personales", "Ingrese su nombre")
	
	datos["apellido"] = sd.askstring("Datos Personales", "Ingrese su apellido")
	
	datos["telefono"] = sd.askstring("Datos Personales", "Ingrese su telefono")
	
	with open("datos.json", "w") as barby:
		dump(datos, barby)

def mostrar():
	vertical = 10
	
	datos = loads(open("datos.json").read())
	
	for key, value in datos.items():
		dataLabel = tk.Label(mainForm, text = key + ": " + value)
		dataLabel.place(x = 10, y = vertical)
		vertical += 20

mainForm = tk.Tk()
mainForm.title("Agenda")
mainForm.geometry("400x200")

mainMenu = tk.Menu(mainForm)

fileMenu = tk.Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Salir", command = quit)

mainMenu.add_cascade(label = "Archivo", menu = fileMenu)

personMenu = tk.Menu(mainMenu, tearoff = 0)
personMenu.add_command(label = "Agregar datos", command = agregar)
personMenu.add_separator()
personMenu.add_command(label = "Mostrar datos", command = mostrar)

mainMenu.add_cascade(label = "Persona", menu = personMenu)

mainForm.config(menu = mainMenu)

mainForm.mainloop()
