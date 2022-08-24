import pyautogui
import pywhatkit
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def validar_opcion():
    ok: bool = False
    while not ok:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if 0 < opcion < 5:
                ok = True
                return opcion
            else:
                raise ValueError
        except ValueError:
            print("Opcion invalida")
            ok = False


def mensaje_custom():
    cls()
    cerrar: bool = False
    while not cerrar:
        mensaje: str = input("Ingrese el mensaje a enviar antes del spam: ")
        mensaje_a_enviar: str = input("Ingrese el mensaje a enviar: ")
        cantidad_de_mensajes: int = int(input("Ingrese la cantidad de mensajes a enviar: "))
        num_de_telefono = int(input("Ingrese el numero de telefono (11...): "))
        cls()
        num_de_telefono = "+54" + str(num_de_telefono)
        pywhatkit.sendwhatmsg_instantly(num_de_telefono, mensaje)
        for i in range(cantidad_de_mensajes):
            pyautogui.write(mensaje_a_enviar)
            pyautogui.press("enter")


def elefantes():
    cls()
    cerrar = False
    while not cerrar:
        mensaje: str = input("Ingrese el mensaje a enviar antes del spam: ")
        cantidad_de_mensajes: int = int(input("Ingrese la cantidad de mensajes a enviar: "))
        num_de_telefono = int(input("Ingrese el numero de telefono (11...): "))
        cls()
        num_de_telefono = "+54" + str(num_de_telefono)
        pywhatkit.sendwhatmsg_instantly(num_de_telefono, mensaje)
        for i in range(cantidad_de_mensajes):
            pyautogui.write(str(i + 1) + " elefantes se balanceaban sobre la tela de una arana")
            pyautogui.press("enter")
            pyautogui.write("como veian que resistian fueron a llamar a otro elefante ")
            pyautogui.press("enter")


def imagen():
    pass


def main():
    cls()
    cerrar: bool = False
    while not cerrar:
        print("""
        #############################################################
        #############################################################
        ############### Whatsapp spam by @_nicoflorio ###############
        #############################################################
        #############################################################
        
        MENU:
        [1] Mensaje custom
        [2] Elefantes
        [3] Imagen
        [4] Salir
        """)
        opcion = validar_opcion()
        if opcion == 1:
            mensaje_custom()
        elif opcion == 2:
            elefantes()
        elif opcion == 3:
            imagen()
        else:
            cerrar = True


main()
