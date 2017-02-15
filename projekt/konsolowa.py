# wersja konsolkowa

import random
import math
import sys
from itertools import count
import Tkinter 
  
class Dzialanie:
    
    operacja = {
    "dodawanie": lambda x,y: x+y,
    "odejmowanie": lambda x,y: x-y,
    "mnozenie": lambda x,y: x*y,
    "dzielenie": lambda x,y: x/y
    }
    
    licznik=0
    def komunikat(self,licznik):
        lista=["\n\n\nOby tak dalej!\n\n\n","\n\n\nPedzisz jak burza! Wow! Super Ci idzie!\n\n\n","\n\n\nSUPER! Jestes prawdziwym mistrzem!\n\n\n", "\n\n\nNIE WIERZE! JESTEM KROLEM MATEMATYKI!\n\n\n","\n\n\nTo nie mozliwe ale jednak. Nie ma lepszych od Ciebie :)\n\n\n "]
        if dz.licznik==2:
           print lista[0]
        elif dz.licznik==10:
            print lista[1]
        elif dz.licznik==20:
            print lista[2]
        elif dz.licznik==100:
            print lista[3]
        elif dz.licznik==1000:
            print lista[4]
            

		    
    def dod(self,x,y):
        wynik=self.operacja["dodawanie"](x,y)
        napis= "ile jest: " + str(x) + " + " + str(y) + "???"
        print napis
        for c in count():

            try:
                odp=int(input('Wpisz swoja odpowiedz!'))
                break
            except:
                print ("error", c)
                pass
        if wynik==odp:
           self.licznik +=1
           print '\nSUPER! POPRAWNA ODPOWIEDZ!\n' 
           print "\nStan twoich punktow :)) : " + str(self.licznik)
        else:
           print "\nSPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! stan twoich punktow to: "  + str(self.licznik)
           self.dod(x,y)
            
    def od(self,x,y):
        wynik=self.operacja["odejmowanie"](x,y)
        napis= "ile jest: " + str(x) + " - " + str(y) + "???" 
        print napis
        for c in count():
            try:
                odp=int(input('Wpisz swoja odpowiedz!'))
                break
            except ValueError:
                print ("error", c)
                pass
        if wynik==odp:
           self.licznik +=1
           print 
           print "\nStan twoich punktow :)) : " + str(self.licznik)
        else:
           print "\nSPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA!\n stan twoich punktow to: "  + str(self.licznik)
           self.od(x,y)
    def mnoz(self,x,y):
        wynik=self.operacja["mnozenie"](x,y)
        napis= "ile jest: " + str(x) + " * " + str(y) + "???" 
        print napis
        for c in count():
            try:
                odp=int(input('Wpisz swoja odpowiedz!'))
                break
            except:
                print ("error", c)
                pass
        if wynik==odp:
           self.licznik +=1
           print '\nSUPER! POPRAWNA ODPOWIEDZ!\n' 
           print "\nStan twoich punktow :))  : " + str(self.licznik)
        else:
           print "\n\nSPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! \nstan twoich punktow to: "  + str(self.licznik)
           self.mnoz(x,y)
        
    def dziel(self,x,y):
        
        wynik=self.operacja["dzielenie"](x,y)
        napis= "ile jest: " + str(x) + " : " + str(y) + "???" 
        print napis
        for c in count():
            try:
                odp=int(input('Wpisz swoja odpowiedz!'))
                break
            except :
                print ("error", c)
                pass
        if wynik==odp:
           self.licznik +=1
           print '\n\nSUPER! POPRAWNA ODPOWIEDZ!\n\n' 
           print "\nStan twoich punktow :)  : " + str(self.licznik)
        else:
           print "\n\nSPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! \nstan twoich punktow to: "  + str(self.licznik)
           self.dziel(x,y)
    def wybor_operacji(self,x,y):

        print "\nWybierz dzialanie \n 1.\tDodawanie \n 2.\tOdejmowanie \n 3.\tMnozenie \n 4.\tDzielenie \n"


        #try:
        
        b = input()
        #except:
          #   print 'Wpisz jeszcze raz'
        #pass
    
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
             tmp=0
             if y>x:
               x=tmp
               x=y
               tmp=y 
             x=x+x%y
             self.dziel(x,y)
        else:
            print '\n\nwybierz opcje jeszcze raz\n\n'
            self.wybor_operacji(self,x,y)
    def wybor(self,us):
         
         print "\nWybierz poziom trudnosci \n 1.\tbanalny \n 2.\tlatwy \n 3.\tsredni \n 4.\ttrudny \n\n\n5.\tKONIEC ZABAWY :) \n"

       #  try:
         a = input()
     #    except:
        #   print 'Wpisz jeszcze raz'
       #  pass
         
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
             
             b=random.randint(1,1000)
             c=random.randint(1,1000)  
             self.wybor_operacji(b,c)
             
         elif a==5:
             file=open("wyniki.txt","ar+")

             file.write(str(us) + "  uzyskal/a : " + str(self.licznik) + "\n")

             file.close()
             execfile("pa.py")
             sys.exit()
             
            
       
             
         else:
             print '\n\nzla opcja! \n\n'
             self.wybor()
   

def Napis(a):
    b="Hej"
    def zagniezdzona():
        global c
        c= "Super swiat matematyki czeka na Ciebie"
    
    zagniezdzona()
    print b
    print a
    print globals()["c"]
   
    
    
    
dz=Dzialanie()

user=raw_input("CZESC! WPISZ SWOJE IMIE: \n ")
Napis(user) 
while(1):
    dz.wybor(user)
    dz.komunikat(dz.licznik)

