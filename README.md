# Intérprete de Línea de Comandos

Este es un proyecto de un intérprete de línea de comandos básico en Python que simula algunas funcionalidades de un terminal. El intérprete permite realizar operaciones como navegar por el sistema de archivos, listar archivos y directorios, crear y eliminar archivos y directorios, mostrar información del sistema y más.

## Uso

1. Clona el repositorio 
	```bash
    git clone https://github.com/Jos-mlp/TerminalLinux.git
2. Abre una terminal o línea de comandos en la ubicación donde se encuentran los archivos.
	```bash
    cd TerminalLinux
3. Instala todas las dependecias necesarias.
	```bash
    pip install -r requirements.txt
4. Ejecuta el script Python:

    ```bash
    python main.py
    ```

5. Aparecerá un prompt en la terminal. Puedes ingresar los comandos disponibles para interactuar con el intérprete.

## Comandos Disponibles

- `pwd`: Muestra la ruta actual del intérprete.
- `date`: Muestra la fecha actual.
- `time`: Muestra la hora actual.
- `exit`: Cierra el intérprete de línea de comandos.
- `clear`: Limpia la pantalla.
- `man`: Muestra la lista de comandos disponibles y sus descripciones.
- `cd [..] [Directorio]`: Cambia el directorio actual.
- `uname -a`: Muestra información sobre la plataforma del sistema operativo.
- `ls -[a][l] [Directorio]`: Lista archivos y directorios con opciones para mostrar archivos ocultos y detalles extendidos.
- `rm [Archivo]`: Elimina un archivo.
- `touch [Archivo]`: Crea un nuevo archivo.
- `mkdir [Directorio]`: Crea un nuevo directorio.
- `rmdir [Directorio]`: Elimina un directorio vacío.

## Notas

- El script ha sido desarrollado para funcionar en sistemas Windows, sistemas Linux y macOS.
- Ten en cuenta que este proyecto es un ejercicio básico y puede no ser adecuado para entornos de producción o uso extenso.

## Contribuciones

Si deseas contribuir a este proyecto, ¡estás más que bienvenido! Siéntete libre de hacer fork del repositorio, implementar mejoras y enviar pull requests.

## Licencia

Este proyecto está bajo la Licencia MIT. 
