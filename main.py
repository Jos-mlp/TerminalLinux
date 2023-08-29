import os
import platform
import sys
from datetime import datetime
from warnings import catch_warnings
if (os.name== 'nt'):
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
        if (commando == "pwd"): #imprime la ruta
            print(ruta)

        elif (commando == "date"): #imprime la fecha actual
            print("La fecha actual es:", datetime.now().date())

        elif (commando == "time"): #imprime la hora actual
            print("La hora actual es:", datetime.now().time())

        elif (commando == "exit"): #Cierra la terminal
            break

        elif (commando == "clear"): #Limpia la pantalla
            BorrarPantalla()

        elif (commando == "man"): #Imprime las opciones disponibles
            print("--COMANDOS ACEPTADOS--")
            print("pwd: Muestra el directorio activo")
            print("date: Muestra la fecha")
            print("time: Muestra la hora")
            print("exit: sale del intérprete")
            print("clear: borra pantalla")
            print("cd [..] [Directorio]: Cambia el directorio activo")
            print("uname -a: versión del OS")
            print("ls -[a][l] [Directorio]: Muestra el contenido del directorio especificado o, en caso de no especificar ninguno, el directorio activo")
            print("rm [Archivo]: Borra archivos")
            print("touch [Archivo]: Crea archivos")
            print("mkdir [Directorio]: Crea un directorio")
            print("rmdir [Directorio]: Borra un directorio")

        elif (commando == "uname -a"): #Muestra informacion sobre la plataforma del SO
            print(sys.platform)
            print (platform.platform()) 

        elif (commando == "cd"): 
            ruta = os.getcwd()
            os.chdir(ruta)

        elif(commando == "cd .."): #Retorna una carpeta en la terminal
            ruta = os.path.dirname(os.getcwd())
            os.chdir(ruta)

        elif (commando == "ls"): #imprime los archivos normales en la ruta
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
                        try:
                            path = os.path.join(ruta,comSeparado[2]) #Path se utiliza opara crear una ruta temporal
                            os.chdir(path)
                            for item in os.listdir(path):
                                print(item)
                        except OSError as e:  ## si falla retorna el error
                            print ("ERROR: " + str(e.strerror))
                            os.chdir(ruta)
                    else:
                        print("ERROR: Comando desconocido")


                #Sirve para imprimir en formato largo elementos de los archivos
                elif (comSeparado[1] == "-l"):
                    #Regresa los datos cuando no se envia directorio
                    if ((len(comSeparado)) == 2):
                        list = [f for f in os.listdir(ruta) if (DirOculto(f) == 0)]
                        for item in list:
                            ArcivosConMetadatos(item)
                            

                    elif((len(comSeparado)) == 3):
                        try:
                            #Regresa los datos cuando se envia directorio
                            path = os.path.join(ruta,comSeparado[2]) #Path se utiliza opara crear una ruta temporal
                            os.chdir(path)
                            list = [f for f in os.listdir(path) if (DirOculto(f) == 0)]
                            for item in list:
                                ArcivosConMetadatos(item)
                                
                        except OSError as e:  ## si falla retorna el error
                            print ("ERROR: " + str(e.strerror))
                            os.chdir(ruta)
                    else:
                        print("ERROR: Comando desconocido")
                            

                elif(comSeparado[1] == "-al"):
                    #Regresa los datos cuando no se envia directorio
                    if ((len(comSeparado)) == 2):
                        for item in os.listdir(ruta):
                            ArcivosConMetadatos(item)
                            

                    elif((len(comSeparado)) == 3):
                        try:
                        #Regresa los datos cuando se envia directorio
                            path = os.path.join(ruta,comSeparado[2])
                            os.chdir(path)
                            for item in os.listdir(path):
                                ArcivosConMetadatos(item)
                                
                        except OSError as e:  ## si falla retorna el error
                            print ("ERROR: " + str(e.strerror))
                            os.chdir(ruta)
                    else:
                        print("ERROR: Comando desconocido")

                #Sirve para imprimir cuando se pasa el nombre de un directorio sin banderas
                elif(len(comSeparado) == 2):
                    try:
                        path = os.path.join(ruta,comSeparado[1])
                        os.chdir(path)   
                        list = [f for f in os.listdir(path) if (DirOculto(f) == 0)]
                        for item in list:
                            print(item)
                    except OSError as e:  ## si falla retorna el error
                        print ("ERROR: " + str(e.strerror))
                        os.chdir(ruta)
                else:
                    print("ERROR: Comando desconocido")
                    


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

            #Con este comando creamos un archivo con la extension que querramos
            elif(comSeparado[0] == "touch"):
                path = os.path.join(ruta,comSeparado[1])
                file = open(path, "w")
                file. close()

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