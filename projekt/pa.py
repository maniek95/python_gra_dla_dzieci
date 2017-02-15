import Tkinter
from PIL import ImageTk, Image

okno2=Tkinter.Tk()
okno2.title("Do zobaczenia!")
okno2.geometry("800x800")


img = ImageTk.PhotoImage(Image.open("cookiemonster4.jpg"))
panel2 = Tkinter.Label(image = img)
panel2.image=img  #rozwiazanie problemu
Opis=Tkinter.Label(text="\n\nJuz dzisiaj nic nie policzymy :( \n Wroc jeszcze kiedys!\n\n\n", font=("Arial",15,"bold"),bg="grey",fg="white")
Opis.pack(side="top")
panel2.pack(side = "bottom", fill = "x", expand = "yes")
panel.destroy()
okno2.mainloop()
