import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
import wave
import os

def convert_mp4_to_wav(input_file, output_file):
    # Cargar el archivo del video
    video = VideoFileClip(input_file)

    # Extraer el audio del video
    audio = video.audio

    # Guardar el audio en formato wav
    audio.write_audiofile(output_file)  # salida

    # Cerrar los archivos
    audio.close()
    video.close()

def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Seleccionar archivo",
                                          filetypes=(("Archivos de video", "*.mp4"),
                                                     ("Todos los archivos", "*.*")))
    if filename:
        print("Archivo seleccionado:", filename)
        output_file = 'audio.wav'
        convert_mp4_to_wav(filename, output_file)
        print("Archivo de audio guardado como:", output_file)

# Crear una instancia de la VENTANA PRINCIPAL
root = tk.Tk()
root.title('Aplicacion para convertir video a wav')

# Crear boton para seleccionar archivos
buttonFile = tk.Button(root,
                       text="Seleccionar video .mp4",
                       command=browse_files)
buttonFile.pack()

# Agregar widgets a la ventana
label = tk.Label(root,
                 text="Bienvenido")
label.pack()

root.mainloop()  # mostrar la ventana
