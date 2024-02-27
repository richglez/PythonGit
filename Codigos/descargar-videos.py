
from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox



def accion():
    enlace = txtUrl.get()
    video = Youtube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.downlad()
    
    
    
    


root = Tk()
root.config(bd=15)
root.title("Script para descargar video de youtube")


imagen = PhotoImage(file="E:\\Imagenes\\youtube-logo-icone.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

lblIntrucciones = Label(root, text="Inserte la url del video\n")
lblIntrucciones.grid(row=0, column=1)

txtUrl = Entry(root)
txtUrl.grid(row=1, column=1)

btnEnviar = Button(root, text="Descargar: ", command=accion)
btnEnviar.grid(row=2, column=1)


root.mainloop()