import os
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
            pass
        elif (commando == "time"):
            pass
        elif (commando == "exit"):
            break
        elif (commando == "clear"):
            pass
        elif (commando == "man"):
            pass
        elif (commando == "uname -a"):
            pass
        elif (commando == "cd"):
            ruta = os.chdir(os.getcwd())
        #Este else lo utilizamos para encontrar los comandos variables
        else:
            comSeparado = ConvertirLista(commando)
            print(len(comSeparado))
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
                    #Entra a la carpeta que le especifiquemos
                    ruta = os.path.join(ruta, comSeparado[1])

            elif (comSeparado[0] == "rm"):
                pass
            elif (comSeparado[0] == "mkdir"):
                if ((len(comSeparado)) == 2):
                    os.mkdir(comSeparado[1])
            elif (comSeparado[0] == "rmdir"):
                pass

def ConvertirLista(cadena):
    return cadena.split()

if __name__ == "__main__":
    run()