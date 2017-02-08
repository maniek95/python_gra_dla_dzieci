
import Tkinter,sys
from PIL import ImageTk, Image
import os

def wyjscie():
    sys.exit()
def rozpocznij():
    exec(zabawa.py)
okno=Tkinter.Tk()
okno.title("Nauka matematyki dla uczniow szkol podstawowych")
okno.geometry("800x800")
#okno.configure(background='grey')


button=Tkinter.Button(okno,text="Zakoncz zabawe!",command=wyjscie, bg="red", fg="white")
button2=Tkinter.Button(okno,text="Rozpocznij przygode!", command=rozpocznij, bg="green", fg="white")

label=Tkinter.Label(okno,text="\n\nWitaj w magicznej krainie dodawania i odejmowania! \n \n Aby rozpoczac zabawe nacisnij przycisk START! \n Aby wyjsc z programu wcisnij KONIEC ZABAWY\n\n\n", bg="orange",fg="white")
label2=Tkinter.Label(okno,text="Wybierz interesujaca Cie opcje!" , bg="orange",fg="white")


img = ImageTk.PhotoImage(Image.open("CountCookies.jpg"))
panel = Tkinter.Label(okno, image = img)


#label.pack(fill=X)
#label.pack(fill=Y)
label.pack(side="top")
label2.pack(side="top")
panel.pack(side = "left", fill = "both", expand = "yes")
button2.pack(side = "right", fill="x", expand="yes")
button.pack(side = "right",fill="x")

print "\n\n\n\n"
okno.mainloop()
