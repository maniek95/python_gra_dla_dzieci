# wersja konsolkowa

import random
import math
import sys

class Dzialanie:

    licznik=0
    def komunikat(self,licznik):
        if dz.licznik==2:
           print "\n\n\nOby tak dalej!\n\n\n"
        elif dz.licznik==10:
            print "\n\n\nPedzisz jak burza! Wow! Super Ci idzie!\n\n\n"
        elif dz.licznik==20:
            print "\n\n\nSUPER! Jestes prawdziwym mistrzem!\n\n\n"
        elif dz.licznik==100:
            print "\n\n\nNIE WIERZE! JESTEM KROLEM MATEMATYKI!\n\n\n"
        elif dz.licznik==1000:
            print "\n\n\nTo nie mozliwe ale jednak. Nie ma lepszych od Ciebie :)\n\n\n "

    def dod(self,x,y):
        wynik=x+y
        napis= "ile jest: " + str(x) + " + " + str(y) + "???" 
        print napis
        odp=input()
        if wynik==odp:
           self.licznik +=1
           print '\nSUPER! POPRAWNA ODPOWIEDZ!\n' 
           print "\nStan twoich punktow :)) : " + str(self.licznik)
        else:
           print "\nSPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! stan twoich punktow to: "  + str(self.licznik)
           self.dod(x,y)
            
    def od(self,x,y):
        wynik=x-y
        napis= "ile jest: " + str(x) + " - " + str(y) + "???" 
        print napis
        odp=input()
        if wynik==odp:
           self.licznik +=1
           print '\nSUPER! POPRAWNA ODPOWIEDZ!\n' 
           print "\nStan twoich punktow :)) : " + str(self.licznik)
        else:
           print "\nSPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA!\n stan twoich punktow to: "  + str(self.licznik)
           self.od(x,y)
    def mnoz(self,x,y):
        wynik=x*y
        napis= "ile jest: " + str(x) + " * " + str(y) + "???" 
        print napis
        odp=input()
        if wynik==odp:
           self.licznik +=1
           print '\nSUPER! POPRAWNA ODPOWIEDZ!\n' 
           print "\nStan twoich punktow :))  : " + str(self.licznik)
        else:
           print "\n\nSPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! \nstan twoich punktow to: "  + str(self.licznik)
           self.mnoz(x,y)
        
    def dziel(self,x,y):
        if(x%y!=0):
            reszta=x%y
            x+=reszta
        wynik=x/y
        napis= "ile jest: " + str(x) + " : " + str(y) + "???" 
        print napis
        odp=input()
        if wynik==odp:
           self.licznik +=1
           print '\n\nSUPER! POPRAWNA ODPOWIEDZ!\n\n' 
           print "\nStan twoich punktow :)  : " + str(self.licznik)
        else:
           print "\n\nSPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! \nstan twoich punktow to: "  + str(self.licznik)
           self.dziel(x,y)
    def wybor_operacji(self,x,y):

        print "\nWybierz dzialanie \n 1.\tDodawanie \n 2.\tOdejmowanie \n 3.\tMnozenie \n 4.\tDzielenie \n"
        b=input()
        if  b== 1:
             self.dod(x,y)
             
                 
        elif b== 2:
            tmp=0
            if (x-y)<0:
              x=tmp
              x=y
              tmp=y 
            self.od(x,y)
             
            
        elif b== 3:
             self.mnoz(x,y)
            
        elif b== 4:
             self.dziel(x,y)
             #if(x % 
        else:
            print '\n\nwybierz opcje jeszcze raz\n\n'
            self.wybor_operacji(self,x,y)
    def wybor(self):
         print "\nWybierz poziom trudnosci \n 1.\tbanalny \n 2.\tlatwy \n 3.\tsredni \n 4.\ttrudny \n\n\n5.\tKONIEC ZABAWY :) \n"

         a=input()
      
         if a== 1:
            b=random.randint(1,10)
            c=random.randint(1,10)
            self.wybor_operacji(b,c)
                   

         elif a== 2:
             b=random.randint(1,20)
             c=random.randint(1,20)
             self.wybor_operacji(b,c)
         elif a== 3:
             b=random.randint(1,100)
             c=random.randint(1,100)  
             self.wybor_operacji(b,c)  
         elif a== 4:
             b=random.randint(1,10000)
             c=random.randint(1,10000)  
             self.wybor_operacji(b,c)
         elif a==5:
             execfile("pa.py")
             sys.exit()
         else:
             print '\n\nzla opcja! \n\n'
             self.wybor()
   

dz=Dzialanie()

while(1):
    dz.wybor()
    dz.komunikat(dz.licznik)

