import Tkinter
import sys
import random
from PIL import ImageTk, Image
import os
class Poziom:

    poziomy_trudnosci=['banalny', 'latwy', 'sredni', 'trudny']
    
okno=Tkinter.Tk()
okno.title("Nauka matematyki dla uczniow szkol podstawowych")
okno.geometry("900x800")
Opis=Tkinter.Label(okno,text="\n\nWYBIERZ POZIOM TRUDNOSCI\n\n\n", font=("Arial",15,"bold"),bg="grey",fg="white")

dod=Tkinter.Button(okno,text="BANALNY", command=Poziom.poziomy_trudnosci[0], bg="green", fg="white",font=("Arial",24,"italic"))
odej=Tkinter.Button(okno,text="LATWY", command=Poziom.poziomy_trudnosci[1], bg="green", fg="white",font=("Arial",24,"italic"))
mnoz=Tkinter.Button(okno,text="SREDNI", command=Poziom.poziomy_trudnosci[2], bg="green", fg="white",font=("Arial",24,"italic"))
dziel=Tkinter.Button(okno,text="TRUDNY", command=Poziom.poziomy_trudnosci[3], bg="green", fg="white",font=("Arial",24,"italic"))

img = ImageTk.PhotoImage(Image.open("cookie.gif"))
panel = Tkinter.Label(okno, image = img)


Opis.pack(side="top",expand="yes")
panel.pack(side = "top", fill = "both", expand = "yes")
dod.pack(side="left",expand="yes")
odej.pack(side="left",expand="yes")
mnoz.pack(side="right",expand="yes")
dziel.pack(side="right",expand="yes")

okno.mainloop()
