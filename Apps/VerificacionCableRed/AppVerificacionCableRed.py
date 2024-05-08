import tkinter as tk
from tkinter import ttk
import psutil
import customtkinter

def verificar_estado():
    interfaces = psutil.net_if_stats()
    if 'Ethernet' in interfaces:
        estado = interfaces['Ethernet'].isup
        if estado:
            estado_label.config(text="El cable de red Ethernet está conectado.", foreground="green")
        else:
            estado_label.config(text="El cable de red Ethernet está desconectado.", foreground="red")
    else:
        estado_label.config(text="No se encontró una interfaz de red Ethernet. Tu computadora no acepta cables ethernet.", foreground="orange")

# Crear una ventana
root = customtkinter.CTk()
root.title("Verificador de Cable Ethernet")


# Ajustando el alto y el ancho de la ventana
root.geometry("400x500")

# Crear un estilo para los botones
style = ttk.Style()
style.configure('TButton', foreground='black', background='lightgray', font=('Helvetica', 22))

# Crear un botón para verificar el estado
verificar_button = customtkinter.CTkButton(master=root, text="Verificar estado", command=verificar_estado)
verificar_button.pack(pady=20)

# Crear una etiqueta para mostrar el estado
estado_label = ttk.Label(root, text="")
estado_label.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
