import Tkinter
from PIL import ImageTk, Image

okno=Tkinter.Tk()
okno.title("Do zobaczenia!")
okno.geometry("800x800")


img = ImageTk.PhotoImage(Image.open("cookiemonster4.jpg"))
panel = Tkinter.Label(okno, image = img)
Opis=Tkinter.Label(okno,text="\n\nJuz dzisiaj nic nie policzymy :( \n Wroc jeszcze kiedys!\n\n\n", font=("Arial",15,"bold"),bg="grey",fg="white")
Opis.pack(side="top")
panel.pack(side = "bottom", fill = "both", expand = "yes")
okno.mainloop()
