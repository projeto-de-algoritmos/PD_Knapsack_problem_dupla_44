import os
import pygame
import tkinter as tk
from tkinter import Tk, Button, Label, Frame
from PIL import Image, ImageTk

def changeOnHover(button, colorOnHover, colorOnLeave):
 
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
 
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

root = Tk()
root.title('Test buttons')
root.geometry("600x600")

file = "Modded_wagon.png"

# Obtenha as dimensões do frame
frame_width = 600
frame_height = 600

# Carregue a imagem original
original_image = Image.open(file)

# Redimensione a imagem para o tamanho do frame
resized_image = original_image.resize((frame_width, frame_height), Image.ANTIALIAS)

# Crie o objeto ImageTk a partir da imagem redimensionada
bg = ImageTk.PhotoImage(resized_image)

# Crie o label com a imagem redimensionada
label = Label(root, image=bg)
label.place(x=0, y=0)

frame = Frame(root)
frame.pack(pady=20)

# Adicione os botões
button1 = Button(frame, text="Exit", bg="red")
button1.pack(pady=20)
changeOnHover(button1, "red", "red")

button3 = Button(frame, text="Reset", bg="yellow")
button3.pack(pady=20)
changeOnHover(button3, "red", "yellow")

button2 = Button(frame, text="Start", bg="green")
button2.pack(pady=20)
changeOnHover(button2, "red", "green")

root.mainloop()
