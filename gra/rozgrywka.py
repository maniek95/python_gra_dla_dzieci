import random

import Tkinter


okno=Tkinter.Tk()
okno.title("Nauka matematyki dla uczniow szkol podstawowych")
okno.geometry("800x800")
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
    odpowiedz = Tkinter.Entry(okno)
    wynik=1

                   
dz=Dzialanie()
l = Tkinter.Label(okno, textvariable = dz.liczba_pierwsza)
l.pack()
okno.mainloop()
print dz.liczba_pierwsza
print dz.liczba_druga


