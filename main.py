import tkinter
import pywhatkit
import pyautogui
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def accion_boton1(entrada1, entrada2, entrada3, ventana):
    mensaje = entrada1.get()
    veces = int(entrada2.get())
    numero = entrada3.get()
    ventana.destroy()

    cls()
    numero = "+54" + str(numero)
    pywhatkit.sendwhatmsg_instantly(numero, mensaje)
    for i in range(veces):
        pyautogui.write(mensaje)
        pyautogui.press("enter")

    exit()


def boton1(ventanaa):
    ventanaa.destroy()
    ventana = tkinter.Tk()
    ventana.title("Mensaje random")
    ventana.geometry("400x350")
    ventana.config(bg="grey")
    #poner 3 entradas de texto
    texto = tkinter.Label(ventana, text="Spam a contacto", font=("Arial", 15), bg="grey")
    texto.pack()
    #poner un texto
    texto = tkinter.Label(ventana, text="Ingrese el mensaje a spamear", font=("Arial", 10), bg="grey")
    texto.pack()

    entrada1 = tkinter.Entry(ventana, width=30, font=("Arial", 10), bg="white")
    entrada1.pack()
    #poner un texto
    texto = tkinter.Label(ventana, text="Ingrese el numero de veces a spamear", font=("Arial", 10), bg="grey")
    texto.pack()
    entrada2 = tkinter.Entry(ventana, width=30, font=("Arial", 10), bg="white")
    entrada2.pack()
    #poner un texto
    texto = tkinter.Label(ventana, text="Ingrese el numero de telefono (formato 11...)", font=("Arial", 10), bg="grey")
    texto.pack()
    entrada3 = tkinter.Entry(ventana, width=30, font=("Arial", 10), bg="white")
    entrada3.pack()
    #poner un boton
    texto = tkinter.Label(ventana, text="", font=("Arial", 10), bg="grey")
    texto.pack()
    boton = tkinter.Button(ventana, text="Enviar", font=("Arial", 20), bg="white", command=lambda: accion_boton1
    (entrada1, entrada2, entrada3, ventana))
    boton.pack()
    ventana.mainloop()


def menu():
    ventana = tkinter.Tk()
    ventana.title("Whatsapp bot by @_nicoflorio")
    ventana.geometry("500x380")
    ventana.config(bg="grey")
    #poner un texto
    texto = tkinter.Label(ventana, text="Whatsapp bot by @_nicoflorio", font=("Arial", 20), bg="grey")
    texto.pack()
    texto = tkinter.Label(ventana, text="", font=("Arial", 10), bg="grey")
    texto.pack()
    #poner un boton
    boton_1 = tkinter.Button(ventana, text="Spam a contacto", font=("Arial", 18), bg="white",
                             command=lambda: boton1(ventana))
    boton_1.pack()
    texto = tkinter.Label(ventana, text="", font=("Arial", 10), bg="grey")
    texto.pack()
    boton_2 = tkinter.Button(ventana, text="Spam a grupo", font=("Arial", 18), bg="white",
                             command=lambda: boton1(ventana))
    boton_2.pack()
    texto = tkinter.Label(ventana, text="(proximamente)", font=("Arial", 8), bg="grey")
    texto.pack()
    boton_3 = tkinter.Button(ventana, text="Spam de fotos", font=("Arial", 18), bg="white",
                             command=lambda: boton1(ventana))
    boton_3.pack()
    texto = tkinter.Label(ventana, text="(proximamente)", font=("Arial", 8), bg="grey")
    texto.pack()

    ventana.mainloop()

menu()
