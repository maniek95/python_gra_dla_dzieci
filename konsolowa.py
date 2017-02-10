# wersja konsolkowa

import random
import math
class Dzialanie:

    licznik=0
    def dod(self,x,y):
        wynik=x+y
        napis= "ile jest: " + str(x) + " + " + str(y) + "???" 
        print napis
        odp=input()
        if wynik==odp:
           self.licznik +=1
           print 'SUPER! POPRAWNA ODPOWIEDZ!' 
           print "Stan twoich punktow :)) : " + str(self.licznik)
        else:
           print "SPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! stan twoich punktow to: "  + str(self.licznik)
           
            
    def od(self,x,y):
        wynik=x-y
        napis= "ile jest: " + str(x) + " - " + str(y) + "???" 
        print napis
        odp=input()
        if wynik==odp:
           self.licznik +=1
           print 'SUPER! POPRAWNA ODPOWIEDZ!' 
           print "Stan twoich punktow :)) : " + str(self.licznik)
        else:
           print "SPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! stan twoich punktow to: "  + str(self.licznik)
        print wynik
    def mnoz(self,x,y):
        wynik=x*y
        napis= "ile jest: " + str(x) + " * " + str(y) + "???" 
        print napis
        odp=input()
        if wynik==odp:
           self.licznik +=1
           print 'SUPER! POPRAWNA ODPOWIEDZ!' 
           print "Stan twoich punktow :)) : " + str(self.licznik)
        else:
           print "SPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! stan twoich punktow to: "  + str(self.licznik)
        print wynik
        
    def dziel(self,x,y):
        wynik=x/y
        napis= "ile jest: " + str(x) + " / " + str(y) + "???" 
        print napis
        odp=input()
        if wynik==odp:
           self.licznik +=1
           print 'SUPER! POPRAWNA ODPOWIEDZ!' 
           print "Stan twoich punktow :)) : " + str(self.licznik)
        else:
           print "SPROBUJ JESZCZE RAZ :) NA PEWNO CI SIE UDA! stan twoich punktow to: "  + str(self.licznik)
        print wynik
    def wybor_operacji(self,x,y):

        print "Wybierz dzialanie \n 1.Dodawanie \n 2. Odejmowanie \n 3. Mnozenie \n 4.Dzielenie \n"
        b=input()
        if  b== 1:
             self.dod(x,y)
             
                 
        elif b== 2:
             self.od(x,y)
             
            
        elif b== 3:
             self.mnoz(x,y)
            
        elif b== 4:
             self.dziel(z)
        else:
            print 'wybierz opcje jeszcze raz'
            self.wybor_operacji(self,x,y)
    def wybor(self):
         print "Wybierz poziom trudnosc \n 1.banalny \n 2. latwy \n 3. sredni \n 4.trudny \n"

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
             crandom.randint(1,10000)  
             self.wybor_operacji(b,c)
         else:
             print 'zla opcja! \n'
             self.wybor()
   
   


dz=Dzialanie()
while(1):
    dz.wybor()

