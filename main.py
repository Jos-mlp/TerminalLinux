import os
from datetime import datetime
from warnings import catch_warnings
#from pathlib import Path
def run():
    ruta = (os.getcwd())
    #Este while se utiliza para que siem
    while True:
        #Obtenemos el comando del usuario
        commando = input(ruta + "> ")
        
        #Con condicionales obtenemos el comando que quiere ejecutar el usuario
        if (commando == "pwd"):
            print(ruta)
        elif (commando == "date"):
            print("La fecha actual es:", datetime.now().date())
        elif (commando == "time"):
            print("La hora actual es:", datetime.now().time())
        elif (commando == "exit"):
            break
        elif (commando == "clear"):
            BorrarPantalla()
        elif (commando == "man"):
            pass
        elif (commando == "uname -a"):
            print ("El sistema operativo de mi ordenador es: "+ os.name) 
        elif (commando == "cd"):
            ruta = os.chdir(os.getcwd())
        elif (commando == "ls"):
            for item in os.listdir():
                print(item)
        #Este else lo utilizamos para encontrar los comandos variables
        else:
            #Con la funcion ConvertirLista separamos la cadena en palabras
            comSeparado = ConvertirLista(commando)
            #Con este bloque ejecutamos el comando ls y todas sus variaciones
            if (comSeparado[0] == "ls"):
                if (comSeparado[1] == "-a"):
                    if ((len(comSeparado)) == 2):
                        pass
                    elif((len(comSeparado)) == 3):
                        pass

                elif (comSeparado[1] == "-l"):
                    if ((len(comSeparado)) == 2):
                        pass
                    elif((len(comSeparado)) == 3):
                        pass


            #Con este comando ejecutamos el comando cd y todas sus variaciones
            elif (comSeparado[0] == "cd"):
                if ((len(comSeparado)) == 2):
                    #Comprueba que el directorio exista antes de cambiar la ruta
                    if (os.path.exists(os.path.join(ruta, comSeparado[1])) == True):
                        #Entra a la carpeta que le especifiquemos
                        ruta = os.path.join(ruta, comSeparado[1])
                    else: print("ERROR: Este directorio NO existe")
                else:
                    print("ERROR: Comando desconocido")


            #Con este comando ejecutamos el comando rm y todas sus variaciones
            elif (comSeparado[0] == "rm"):
                if ((len(comSeparado)) == 2):
                    #Utilizamos un try para capturar algun error
                    try:
                        #Borramos el directorio
                        os.remove(comSeparado[1])
                    except OSError as e:  ## si falla retorna el error
                        print ("ERROR: %s - %s." % (e.filename, e.strerror))
                else:
                    print("ERROR: Comando desconocido")


            #Con este comando ejecutamos el comando mkdir y todas sus variaciones
            elif (comSeparado[0] == "mkdir"):
                if ((len(comSeparado)) == 2):
                    #Utilizamos un try para capturar algun error
                    try:
                        #Creamos un nuevo directorio con el nombre que el usuario ingreso
                        os.mkdir(comSeparado[1])
                    except OSError as e:  ## si falla retorna el error
                        print ("ERROR: %s - %s." % (e.filename, e.strerror))
                else:
                    print("ERROR: Comando desconocido")
            

            #Con este comando ejecutamos el comando rmdir y todas sus variaciones
            elif (comSeparado[0] == "rmdir"):
                if ((len(comSeparado)) == 2):
                    #Utilizamos un try para capturar algun error
                    try:
                        #Borramos el directorio
                        os.rmdir(comSeparado[1])
                    except OSError as e:  ## si falla retorna el error
                        print ("ERROR: %s - %s." % (e.filename, e.strerror))
                else:
                    print("ERROR: Comando desconocido")


def ConvertirLista(cadena): #Crea tokens de una cadena de texto
    return cadena.split()

def BorrarPantalla(): #Detecta que sistema operativo usamos para limpiar la pantalla
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


if __name__ == "__main__":
    run()