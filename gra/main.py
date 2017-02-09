
import Tkinter,sys
from PIL import ImageTk, Image
import os

def wyjscie():
    execfile("pa.py")
def rozpocznij:
    execfile("poziomy.py") 
okno=Tkinter.Tk()
okno.title("Nauka matematyki dla uczniow szkol podstawowych")
okno.geometry("800x800")
#okno.configure(background='grey')


button=Tkinter.Button(okno,text="Zakoncz zabawe!",command=wyjscie, bg="red", fg="white",font=("Arial",24,"italic"))
button2=Tkinter.Button(okno,text="Rozpocznij przygode!", command=rozpocznij, bg="green", fg="white",font=("Arial",24,"italic"))

label=Tkinter.Label(okno,text="\n\nWitaj w magicznej krainie matematyki \n \n Aby rozpoczac zabawe nacisnij przycisk ROZPOCZNIJ  PRZYGODE! \n Aby wyjsc z programu wcisnij KONIEC ZABAWY!\n\n\n", font=("Arial",15,"bold"),bg="grey",fg="white")

img = ImageTk.PhotoImage(Image.open("CountCookies.jpg"))
panel = Tkinter.Label(okno, image = img)


#label.pack(fill=X)
#label.pack(fill=Y)
label.pack(side="top")
panel.pack(side = "top", fill = "both", expand = "yes")
button2.pack(side = "left", fill="x", expand="yes")
print "\n"
button.pack(side = "right",fill="x" , expand="yes")

print "\n\n\n\n"
okno.mainloop()
