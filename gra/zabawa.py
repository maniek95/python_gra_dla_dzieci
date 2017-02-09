import Tkinter
import sys
import random
from PIL import ImageTk, Image
import os
class Dzialania:

    poziomy_trudnosci=['banalny', 'latwy', 'sredni', 'trudny']
    def Add():
        sum=2
    def Sub():
        sum=2
    def Mul():
        sum=2
    def Div():
        sum=2
        L



def wybor(a):
    
    if   a== 1:
         Add()
    elif a== 2:
         Sub()
    elif a== 3:
         Mul()
    elif a== 4:
         Div()
    else :
        print ":) Zastanow sie jeszcze raz! \n Przeciez nic nie wybrales z listy!"
        a=input()
class Wybor:
    
    def dodaj(self):
        2
    def odejmij(self):
        2
    def mnoz(self):
        2
    def dziel(self):
        2
        
okno=Tkinter.Tk()
okno.title("Nauka matematyki dla uczniow szkol podstawowych")
okno.geometry("900x800")
Opis=Tkinter.Label(okno,text="\n\nWYBIERZ JAKI TYP DZIALAN CHCESZ DZIS POCWICZYC?\n\n\n", font=("Arial",15,"bold"),bg="grey",fg="white")

dod=Tkinter.Button(okno,text="DODAWANIE", command=Wybor.dodaj, bg="green", fg="white",font=("Arial",24,"italic"))
odej=Tkinter.Button(okno,text="ODEJMOWANIE", command=Wybor.odejmij, bg="green", fg="white",font=("Arial",24,"italic"))
mnoz=Tkinter.Button(okno,text="MNOZENIE", command=Wybor.mnoz, bg="green", fg="white",font=("Arial",24,"italic"))
dziel=Tkinter.Button(okno,text="DZIELENIE", command=Wybor.dziel, bg="green", fg="white",font=("Arial",24,"italic"))

img = ImageTk.PhotoImage(Image.open("CookieAndKermit.jpg"))
panel = Tkinter.Label(okno, image = img)


Opis.pack(side="top",expand="yes")
panel.pack(side = "top", fill = "both", expand = "yes")
dod.pack(side="left",expand="yes")
odej.pack(side="left",expand="yes")
mnoz.pack(side="right",expand="yes")
dziel.pack(side="right",expand="yes")

okno.mainloop()
