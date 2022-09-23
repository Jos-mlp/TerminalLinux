import os
from datetime import datetime
from warnings import catch_warnings
import win32api
import win32con
#from pathlib import Path
def run():
    ruta = (os.getcwd())
    #Este while se utiliza para que siem
    while True:
        print("")
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
            ruta = os.getcwd()
            os.chdir(ruta)
        elif(commando == "cd .."):
            ruta = os.path.dirname(os.getcwd())
            os.chdir(ruta)
        elif (commando == "ls"):
            list = [f for f in os.listdir(ruta) if (DirOculto(f) == 0)]
            for item in list:
                print(item)

        #Este else lo utilizamos para encontrar los comandos variables
        else:
            #Con la funcion ConvertirLista separamos la cadena en palabras
            comSeparado = ConvertirLista(commando)
            #Con este bloque ejecutamos el comando ls y todas sus variaciones
            if (comSeparado[0] == "ls"):
                #Sirve para imprimir todos los archivos ocultos
                if (comSeparado[1] == "-a"):
                    #Regresa los datos cuando no se envia directorio
                    if ((len(comSeparado)) == 2):
                        for item in os.listdir(ruta):
                            print(item)
                    #Regresa los datos cuando se envia directorio
                    elif((len(comSeparado)) == 3):
                        path = os.path.join(ruta,comSeparado[2]) #Path se utiliza opara crear una ruta temporal
                        os.chdir(path)
                        for item in os.listdir(path):
                            print(item)
                        os.chdir(ruta)


                #Sirve para imprimir en formato largo elementos de los archivos
                elif (comSeparado[1] == "-l"):
                    #Regresa los datos cuando no se envia directorio
                    if ((len(comSeparado)) == 2):
                        list = [f for f in os.listdir(ruta) if (DirOculto(f) == 0)]
                        for item in list:
                            ArcivosConMetadatos(item)
                            print()

                    elif((len(comSeparado)) == 3):
                        #Regresa los datos cuando se envia directorio
                        path = os.path.join(ruta,comSeparado[2]) #Path se utiliza opara crear una ruta temporal
                        os.chdir(path)
                        list = [f for f in os.listdir(path) if (DirOculto(f) == 0)]
                        for item in list:
                            ArcivosConMetadatos(item)
                            print()
                        os.chdir(ruta)
                            

                elif(comSeparado[1] == "-al"):
                    #Regresa los datos cuando no se envia directorio
                    if ((len(comSeparado)) == 2):
                        for item in os.listdir(ruta):
                            ArcivosConMetadatos(item)
                            print()

                    elif((len(comSeparado)) == 3):
                        #Regresa los datos cuando se envia directorio
                        path = os.path.join(ruta,comSeparado[2])
                        os.chdir(path)
                        for item in os.listdir(path):
                            ArcivosConMetadatos(item)
                            print()
                        os.chdir(ruta)

                #Sirve para imprimir cuando se pasa el nombre de un directorio sin banderas
                elif(len(comSeparado) == 2):
                    path = os.path.join(ruta,comSeparado[1])
                    os.chdir(path)
                    list = [f for f in os.listdir(path) if (DirOculto(f) == 0)]
                    for item in list:
                        print(item)
                    os.chdir(ruta)


            #Con este comando ejecutamos el comando cd y todas sus variaciones
            elif (comSeparado[0] == "cd"):
                if ((len(comSeparado)) == 2):
                    #Comprueba que el directorio exista antes de cambiar la ruta
                    if (os.path.exists(os.path.join(ruta, comSeparado[1])) == True):
                        #Entra a la carpeta que le especifiquemos
                        ruta = os.path.join(ruta, comSeparado[1])
                        os.chdir(ruta)
                    else: print("ERROR: Este directorio NO existe")
                else:
                    print("ERROR: Comando desconocido")


            #Con este comando ejecutamos el comando rm y todas sus variaciones
            elif (comSeparado[0] == "rm"):
                if ((len(comSeparado)) == 2):
                    #Utilizamos un try para capturar algun error
                    try:
                        path = os.path.join(ruta,comSeparado[1])
                        #Borramos el directorio
                        os.remove(path)
                    except OSError as e:  ## si falla retorna el error
                        print ("ERROR: %s - %s." % (e.filename, e.strerror))
                else:
                    print("ERROR: Comando desconocido")


            #Con este comando ejecutamos el comando mkdir y todas sus variaciones
            elif (comSeparado[0] == "mkdir"):
                if ((len(comSeparado)) == 2):
                    #Utilizamos un try para capturar algun error
                    try:
                        path = os.path.join(ruta,comSeparado[1])
                        #Creamos un nuevo directorio en ruta con el nombre que el usuario ingreso
                        os.mkdir(path)
                    except OSError as e:  ## si falla retorna el error
                        print ("ERROR: %s - %s." % (e.filename, e.strerror))
                else:
                    print("ERROR: Comando desconocido")
            

            #Con este comando ejecutamos el comando rmdir y todas sus variaciones
            elif (comSeparado[0] == "rmdir"):
                if ((len(comSeparado)) == 2):
                    #Utilizamos un try para capturar algun error
                    try:
                        path = os.path.join(ruta,comSeparado[1])
                        #Borramos el directorio
                        os.rmdir(path)
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

def ArcivosConMetadatos(ruta):
    metadata = os.stat(ruta)
    ultima_mod = datetime.utcfromtimestamp(metadata.st_mtime).strftime('%Y/%m/%d')
    print("Ultima modificacion: "+ str(ultima_mod) +"  "+ str(metadata.st_size) + " byte" + "  " + ruta) 

def DirOculto(p):
    if os.name== 'nt':
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx


if __name__ == "__main__":
    run()