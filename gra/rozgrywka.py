import random
import math
try:
    import Tkinter as tk # Python 2.x
except:
    import tkinter as tk # Python 3.x



class Dzialanie:

    def Wybor(opcja):
         
        if   a== 1:
             Add()
        elif a== 2:
             Sub()
        elif a== 3:
             Mul()
        elif a== 4:
             Div()
    liczba_pierwsza=random.randint(45, 55)
    liczba_druga=random.randint(45, 55)
    operator='+'
   
    wynik=1
    #konstruktor
    def __init__(self,master):
      master.title("Nauka matematyki dla uczniow szkol podstawowych")
      master.geometry("800x800")
      label=tk.Label(master,self.liczba_pierwsza)
      label2=tk.Label(master,self.liczba_druga)
      odpowiedz = tk.Entry(master)
      label.pack()
      label2.pack()
      odpowiedz.pack(side = "right", fill="x", expand="no")
      
okno=tk.Tk()

dz=Dzialanie(okno)


okno.mainloop()



