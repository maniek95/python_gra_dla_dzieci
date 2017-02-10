from Tkinter import *
from PIL import ImageTk, Image

def funkcja(okno):
    
    okno.title("Do zobaczenia!")
    okno.geometry("800x800")

    Opis=Label(okno,text="\n\nJuz dzisiaj nic nie policzymy :( \n Wroc jeszcze kiedys!\n\n\n", font=("Arial",15,"bold"),bg="grey",fg="white")
    Opis.pack(side="top")
    


okno=Tk()
funkcja(okno)
img2 = ImageTk.PhotoImage(Image.open("cookiemonster4.jpg"))
panel = Label(okno, image = img2)
panel.pack(side = "bottom", fill = "both", expand = "yes")
okno.mainloop()
