import secrets
import string
import os
import sys
from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox, CTkImage
from PIL import Image
import tkinter as tk

"""" // Colores // """

c_negro = "#010101"
c_amarillo = "#F6BB43"
c_azul = "#427EF6"

""""// Funciones // """


def passwordGenerator(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


def PG_App(length: int, symbols: bool, uppercase: bool, quantity: int):

    ventana = CTk()
    ventana.minsize(480, 500)
    ventana.config(bg=c_negro)
    ventana.resizable(False, False)
    ventana.title("Contraseñas")

    frame2 = CTkFrame(ventana, fg_color=c_negro,
                      border_color="#427EF6", border_width=2)
    frame2.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

    scrollbar = tk.Scrollbar(frame2)
    textarea = tk.Text(frame2, font=('Arial', 12), yscrollcommand=scrollbar.set, fg="white", bg=c_negro,
                       relief="solid", borderwidth=2, highlightthickness=2, padx=4, pady=4)
    textarea.config(highlightbackground="blue")

    # Ubicar el Text widget y scrollbar en la ventana
    textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    for i in range(quantity):
        password = f"🔑 Contraseña número {i+1}  ---->  " + passwordGenerator(
            length=length, symbols=symbols, uppercase=uppercase)
        textarea.insert(tk.END, password + "\n\n")

    # Deshabilitar la escritura en el Text widget
    textarea.configure(state=tk.DISABLED)

    derechos = "©lruizap"
    label_derechos = CTkLabel(
        ventana, bg_color=c_negro, text=derechos, font=("Arial", 12))
    label_derechos.grid(row=2, columnspan=2, padx=0, pady=10)

    # Logo de la ventana
    ventana.iconbitmap(logo_ico)

    # Fin ventana
    ventana.mainloop()


#! Pestaña principal


""" // App // """

root = CTk()
root.geometry('500x600+320+20')
root.minsize(480, 500)
root.config(bg=c_negro)
root.resizable(False, False)
root.title("CryptoPass")

frame = CTkFrame(root, fg_color=c_negro,
                 border_color="#427EF6", border_width=2)
frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

frame.columnconfigure([0, 1], weight=1)
frame.rowconfigure([0, 1, 2, 3, 4], weight=1)

# Dentro de la ventana principal configuramos la posición del frame
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

""" // Imagenes // """

logo = CTkImage(light_image=Image.open("./images/key-fhd.png"),
                dark_image=Image.open("./images/key-fhd.png"), size=(128, 128))
# Redimensionar la imagen a un factor de 0.5 (la mitad del tamaño original)
logo_ico = './images/key-fhd.ico'

""" // Elementos de la app // """

# Crear el label para la imagen
label_imagen = CTkLabel(frame, text='', image=logo)
label_imagen.grid(row=0, column=0, padx=0, pady=5)

# Crear el label para el texto
texto = "CryptoPass"
label_texto = CTkLabel(frame, text=texto, font=("Arial", 25))
label_texto.grid(row=0, column=1, padx=0, pady=5)

longitud = CTkEntry(frame, font=('Arial', 12),
                    placeholder_text='Introduzca la longitud', border_color=c_amarillo, fg_color=c_negro, width=200, height=40)
longitud.grid(columnspan=2, row=1, padx=4, pady=2)

cantidad = CTkEntry(frame, font=('Arial', 12),
                    placeholder_text='Introduzca la cantidad', border_color=c_amarillo, fg_color=c_negro, width=200, height=40)
cantidad.grid(columnspan=2, row=2, padx=4, pady=2)

simbolos = CTkCheckBox(frame, text='Símbolos', hover_color=c_azul,
                       border_color=c_amarillo, fg_color=c_amarillo)
simbolos.grid(column=0, row=3, padx=4, pady=6)

mayusculas = CTkCheckBox(frame, text='Mayúsculas', hover_color=c_azul,
                         border_color=c_amarillo, fg_color=c_amarillo)
mayusculas.grid(column=1, row=3, padx=4, pady=6)

# Botón
bt_gen = CTkButton(frame, font=('Arial', 12), border_color=c_amarillo,
                   fg_color=c_negro, hover_color="#F2A405", corner_radius=12, border_width=2, text='Generar Contraseñas', height=35,
                   command=lambda: PG_App(length=int(longitud.get().strip()),
                                                 symbols=simbolos.get(),
                                                 uppercase=mayusculas.get(),
                                                 quantity=int(cantidad.get().strip())))
bt_gen.grid(columnspan=2, row=4, padx=4, pady=18)

derechos = "©lruizap"
label_derechos = CTkLabel(frame, text=derechos, font=("Arial", 12))
label_derechos.grid(row=5, columnspan=2, padx=0, pady=5)

# Logo de la ventana
root.iconbitmap(logo_ico)

# Fin ventana
root.mainloop()
