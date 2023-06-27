# CryptoPass - Generador de contraseñas

Este código nos mostrará como crear un generador de contraseñas seguras con python y para comprobar las contraseñas usaremos la siguiente página.

[How Secure Is My Password? | Password Strength Checker](https://www.security.org/how-secure-is-my-password/)

---

## Índice

- [1. Primeros Pasos](https://www.notion.so/1-Primeros-Pasos-fb4a5d3be5f84866b601c4bb0493ff46?pvs=21)
- [2. Codificación](https://www.notion.so/2-Codificaci-n-d72df0c55c324efcbb0d084d61b5522f?pvs=21)
- [3. Aplicación de escritorio](https://www.notion.so/3-Aplicaci-n-de-escritorio-270353728231448eaa333bae4fb8e00d?pvs=21)
- [4. De `.py` a `.exe`](https://www.notion.so/4-De-py-a-exe-93fb8416c623414d8b8a535eb5807629?pvs=21)

---

## 1. Primeros Pasos

Lo primero que voy a hacer será crear un espacio de trabajo y también un entorno virtual por si tenemos que instalar alguna librería.

Para el entorno virtual, usaré `venv` 

```bash
python -m venv venv-CryptoPassEnv
```

Una vez creado el entorno virtual, tendremos que cambiar de intérprete de python al del entorno virtual.

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled.png)

Al seleccionar el intérprete lo tendríamos todo listo para comenzar a trabajar. 

---

## 2. Codificación

Vamos a empezar importando dos librerías, 

```python
import string
import secrets
```

Esto lo hacemos debido a que la librería `random` no es tan aleatoria como la librería `secrets`

Ahora vamos a inicializar nuestra función:

```python
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
```

La función **`passwordGenerator`** genera una contraseña aleatoria según los parámetros proporcionados. El bucle for en esta función se encarga de construir la contraseña carácter por carácter. Veamos cómo funciona:

1. **`for _ in range(length):`** : Esta línea establece un bucle for que se ejecutará **`length`** veces. El valor de **`_`** se ignora en cada iteración, lo que significa que no se utiliza en el cuerpo del bucle. Solo se utiliza para indicar que el bucle se ejecutará la cantidad de veces especificada por **`length`**.
2. **`new_password += combination[secrets.randbelow(combination_length)]`** : En cada iteración del bucle, se agrega un carácter aleatorio de la variable **`combination`** a la variable **`new_password`**. La función **`secrets.randbelow(combination_length)`** genera un número aleatorio entre 0 y **`combination_length - 1`**, que se utiliza como índice para seleccionar un carácter de la cadena **`combination`**.
3. Después de que el bucle se complete, se devuelve la contraseña generada almacenada en la variable **`new_password`**.

La función en su conjunto construye una cadena de caracteres aleatorios seleccionados de una combinación de caracteres. La combinación de caracteres inicial contiene letras minúsculas y dígitos. Si se especifica el parámetro **`symbols`** como **`True`**, se añaden también los símbolos de puntuación a la combinación. Si se especifica el parámetro **`uppercase`** como **`True`**, se añaden también las letras mayúsculas a la combinación. La longitud de la contraseña generada está determinada por el parámetro **`length`**.

Ahora lo que vamos a hacer será un bucle que llame a la función tantas veces como le indiquemos para que nos genere el número de contraseñas que queremos.

```python
for _, index in enumerate(range(5)):
    print(index + 1, " --> ",
          passwordGenerator(length=20, symbols=True, uppercase=True))
```

El bucle utiliza la función **`enumerate()`** y la función **`range()`** para generar una secuencia de números del 0 al 4.

1. **`for _, index in enumerate(range(5)):`**: Esta línea establece el bucle for. **`enumerate()`** se utiliza para obtener tanto el índice como el valor de cada elemento en la secuencia generada por **`range(5)`**. El uso de **`_`** como nombre de variable indica que no nos interesa almacenar el valor de cada elemento, solo el índice.

Y con esto estaría nuestro generador de contraseñas listo, vamos a comprobar su funcionamiento

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled%201.png)

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled%202.png)

---

## 3. Aplicación de escritorio

Tras tener la función lista y comprobar que funciona, vamos a hacerla aplicación de escritorio.

Para ello, tendremos que usar la librería `tkinter` y lo primero que tendremos que hacer será crear el contenedor / ventana para llenarlo de elementos gráficos.

Lo que estamos buscando con la aplicación es que el usuario pueda introducir de forma manual la:

- Cantidad de contraseñas para generar
- Longitud de las contraseñas
- Si quiere Símbolos
- Si quiere Mayúsculas

Por tanto, la función de la aplicación debe ser algo así

```python
def PG_App(length: int, symbols: bool, uppercase: bool, quantity: int):
    for _, index in enumerate(range(quantity)):
        print(index + 1, " --> ",
              passwordGenerator(length=length, symbols=symbols, uppercase=uppercase))
```

Ahora, vamos a crear la aplicación, para ello, vamos a necesitar dos librerías de python

```python
pip install customtkinter, Pillow
```

Una vez instaladas las librerías, vamos a crear la aplicación. Para ello vamos a crear una ventana principal, que será el formulario de inicio y que cuando le demos a un botón, nos envíe a otra página para ver las contraseñas.

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled%203.png)

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled%204.png)

Para hacer la primera ventana se ha introducido el siguiente código:

```python
from passwordGenerator import passwordGenerator
from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox, CTkImage
from PIL import Image
import tkinter as tk

"""" // Colores // """

c_negro = "#010101"
c_amarillo = "#F6BB43"
c_azul = "#427EF6"

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
                   command=lambda: PG_App(length=int(longitud.get()),
                                                 symbols=simbolos.get(),
                                                 uppercase=mayusculas.get(),
                                                 quantity=int(cantidad.get())))
bt_gen.grid(columnspan=2, row=4, padx=4, pady=18)

derechos = "©lruizap"
label_derechos = CTkLabel(frame, text=derechos, font=("Arial", 12))
label_derechos.grid(row=5, columnspan=2, padx=0, pady=5)

# Logo de la ventana
root.iconbitmap(logo_ico)

# Fin ventana
root.mainloop()
```

Y para la segunda, el siguiente 

```python
""""// Funciones // """

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
```

---

## 4. De `.py` a `.exe`

Para hacerlo ejecutable, tendremos que instalar la librería de `auto-py-to-exe`

```python
pip install auto-py-to-exe
```

Una vez descargada, ejecutamos su interfaz gráfica para usarla

```python
auto-py-to-exe
```

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled%205.png)

Una vez hecho eso, introducimos los datos de la aplicación.

- El script de la app
- Si queremos la aplicación en una carpeta o en un solo fichero
- El icono de la app
- Los ficheros adicionales (Algunas dependencias deben ser añadidas)

Y listo, con esto tendríamos nuestra app lista

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled%206.png)

---

Si queremos que nuestro programa se quede como un solo ejecutable, debemos tener mucho cuidado con las rutas de las imágenes, puesto que si las rutas son relativas y con `.` para indicar las carpetas, esta puede fallar.

[https://www.youtube.com/watch?v=xJAM8_Lx5mY](https://www.youtube.com/watch?v=xJAM8_Lx5mY)

Este tutorial explica muy bien el uso de la librería

Las rutas de las imágenes o archivos externos debe quedar de la siguiente forma:

```python
logo = CTkImage(light_image=Image.open("CryptoPass-App\images\key-fhd.png"),
                dark_image=Image.open("CryptoPass-App\images\key-fhd.png"), size=(128, 128))
# Redimensionar la imagen a un factor de 0.5 (la mitad del tamaño original)
logo_ico = 'CryptoPass-App\images\key-fhd.ico'
```

Y con esto, introducimos las siguientes opciones en el software de la librería:

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled%207.png)

Y ya tendríamos nuestro `.exe` generado.

![Untitled](CryptoPass%20-%20Generador%20de%20contrasen%CC%83as%2013720167bfd348a6b049845f95d0b967/Untitled%208.png)