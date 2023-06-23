from script.passwordGenerator import passwordGenerator
import tkinter as tk

def PG_App(length: int, symbols: bool, uppercase: bool, quantity: int):

    # Borrar el widget Label existente, si hay alguno
    for widget in result.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    for _, index in enumerate(range(quantity)):

        password = tk.Label(result, background="#404040", fg="white")
        password.pack()

        password['text'] = f"{index+1}  -->  " + passwordGenerator(
            length=length, symbols=symbols, uppercase=uppercase)


ventana = tk.Tk()
ventana.geometry("700x600")
ventana.title("Generador de contraseñas")
ventana.configure(background="#404040")

# Establecer el icono de la aplicación
# Reemplaza "ruta_del_archivo.ico" con la ruta de tu archivo de icono
ventana.iconbitmap("./images/key-fhd.ico")

# Crear las casillas de verificación
checkbox1 = tk.BooleanVar()
checkbox2 = tk.BooleanVar()

# Crear el frame principal
frame = tk.Frame(ventana, background='#212121')
frame.pack(fill=tk.NONE)

# Cargar la imagen
# Reemplaza "ruta_de_la_imagen.png" con la ruta de tu imagen
imagen = tk.PhotoImage(file="./images/key-fhd.png")

# Redimensionar la imagen a 64x64 píxeles
# Cambia el valor 4 según sea necesario
imagen_redimensionada = imagen.subsample(30)

# Crear el label para la imagen
label_imagen = tk.Label(
    frame, image=imagen_redimensionada, background='#212121')
label_imagen.pack(side="left")

# Crear el label para el título
label_titulo = tk.Label(
    frame, text="Generador de contraseñas", background='#212121', fg="white", font=max)
label_titulo.pack(fill=tk.X, side="left")

###
# Para crear separaciones entre elementos
frame_separacion = tk.Frame(ventana, bg="#404040", height=20)
frame_separacion.pack()
###

length = tk.Label(ventana, text="Longitud:", background="#404040", fg="white")
length.pack()

###
frame_separacion = tk.Frame(ventana, bg="#404040", height=20)
frame_separacion.pack()
###

length_input = tk.Entry(ventana)
length_input.pack()

###
frame_separacion = tk.Frame(ventana, bg="#404040", height=20)
frame_separacion.pack()
###

etiqueta_checkbox1 = tk.Checkbutton(
    ventana, text="Símbolos", variable=checkbox1, background="#404040")
etiqueta_checkbox1.pack()

###
frame_separacion = tk.Frame(ventana, bg="#404040", height=20)
frame_separacion.pack()
###

etiqueta_checkbox2 = tk.Checkbutton(
    ventana, text="Mayúsculas", variable=checkbox2, background="#404040")
etiqueta_checkbox2.pack()

###
frame_separacion = tk.Frame(ventana, bg="#404040", height=20)
frame_separacion.pack()
###

quantity = tk.Label(ventana, text="Cantidad:",
                    background="#404040", fg="white")
quantity.pack()

###
frame_separacion = tk.Frame(ventana, bg="#404040", height=20)
frame_separacion.pack()
###

quantity_input = tk.Entry(ventana)
quantity_input.pack()

###
frame_separacion = tk.Frame(ventana, bg="#404040", height=20)
frame_separacion.pack()
###

# Crear el botón
boton = tk.Button(ventana, text="Genera tus contraseñas",
                  background="#6F0A0A", fg="white", padx=10, pady=5, borderwidth=2, relief="solid",
                  command=lambda: PG_App(length=int(length_input.get()),
                                         symbols=checkbox1.get(),
                                         uppercase=checkbox2.get(),
                                         quantity=int(quantity_input.get())))
boton.pack()

###
frame_separacion = tk.Frame(ventana, bg="#404040", height=20)
frame_separacion.pack()
###

# Parte para los resultados
result = tk.Frame(ventana, background='#404040')
result.pack(fill=tk.NONE)

# Este mainloop es el que lleva todo el registro de lo que está sucediendo en la app.
ventana.mainloop()
