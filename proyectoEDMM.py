import tkinter as tk
import serial
import threading

# Inicializar la comunicación serial con Arduino
arduino = serial.Serial('COM4', 9600)

# Función para enviar comandos a Arduino
def enviar_comando(comando):
    arduino.write(comando.encode())

# Función para procesar los datos recibidos de Arduino
def procesar_datos(datos):
    if datos.startswith('BotonAEncendido'):
        # Actualizar el estado del botón A en la interfaz
        label_estado.config(text="Botón A: Presionado (físico)")
    elif datos.startswith('BotonAApagado'):
        # Actualizar el estado del botón A en la interfaz
        label_estado.config(text="Botón A: No presionado")
    elif datos.startswith('BotonBEncendido'):
        # Actualizar el estado del botón B en la interfaz
        label_estado.config(text="Botón B: Presionado (físico)")
    elif datos.startswith('BotonBApagado'):
        # Actualizar el estado del botón B en la interfaz
        label_estado.config(text="Botón B: No presionado")
    elif datos.startswith('BotonCEncendido'):
        # Actualizar el estado del botón C en la interfaz
        label_estado.config(text="Botón C: Presionado (físico)")
    elif datos.startswith('BotonCApagado'):
        # Actualizar el estado del botón C en la interfaz
        label_estado.config(text="Botón C: No presionado")
    elif datos.startswith('BotonDEncendido'):
        # Actualizar el estado del botón D en la interfaz
        label_estado.config(text="Botón D: Presionado (físico)")
    elif datos.startswith('BotonDApagado'):
        # Actualizar el estado del botón D en la interfaz
        label_estado.config(text="Botón D: No presionado")
    elif datos.startswith('Boton'):
        # Mensaje recibido al presionar un botón físico
        print(datos)

# Función para apagar todas las LEDs
def apagar_leds():
    enviar_comando('E')

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Dashboard")

# Crear etiqueta para mostrar el estado de los botones físicos
label_estado = tk.Label(ventana, text="Estado de los botones físicos")
label_estado.pack()

# Función para procesar el clic de los botones virtuales
def boton_virtual_presionado(comando):
    enviar_comando(comando)

# Crear botones virtuales en la interfaz
boton_A = tk.Button(ventana, text="Botón A", command=lambda: boton_virtual_presionado('A'))
boton_A.pack()

boton_B = tk.Button(ventana, text="Botón B", command=lambda: boton_virtual_presionado('B'))
boton_B.pack()

boton_C = tk.Button(ventana, text="Botón C", command=lambda: boton_virtual_presionado('C'))
boton_C.pack()

boton_D = tk.Button(ventana, text="Botón D", command=lambda: boton_virtual_presionado('D'))
boton_D.pack()

# Botón para apagar todas las LEDs
boton_apagar = tk.Button(ventana, text="Apagar LEDs", command=apagar_leds)
boton_apagar.pack()

# Bucle principal para recibir y procesar datos de Arduino
def leer_datos_desde_arduino():
    while True:
        datos = arduino.readline().decode().strip()
        if datos:
            procesar_datos(datos)
            print(datos)  # Imprimir los datos recibidos en la consola de Visual Studio Code

# Crear un hilo para leer datos de Arduino en segundo plano
thread_arduino = threading.Thread(target=leer_datos_desde_arduino)
thread_arduino.start()

# Iniciar el bucle de la interfaz de usuario
ventana.mainloop()

