from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import random

global Bodovi1
global Bodovi2
global Rndm
global RandomBoja

Bodovi1=0
Bodovi2=0


Rndm = random.randint(0,16777215)
RandomBoja = str(hex(Rndm))
RandomBoja ='#'+ RandomBoja[2:]

def Krizic():

    def Potez(row, column):
    
        global Igrac
        global Ime_1
        global Ime_2
        global Boja_1
        global Boja_2
        global Bodovi1
        global Bodovi2
        global Rndm
        global RandomBoja
        
        
        Ime_1 = Ime1Igraca.get()
        Ime_2 = Ime2Igraca.get()
        Imena = [Ime_1, Ime_2]
        
        Boja_1 = Boja1[1]
        Boja_2 = Boja2[1]
        Boje = [Boja_1, Boja_2]
        
        if RandomBoja == Boja_1[1]:
            Rndm = random.randint(0,16777215)
            RandomBoja = str(hex(Rndm))
            RandomBoja ='#'+ RandomBoja[2:]
        elif RandomBoja == Boja_2[1]:
            RandomBoja = str(hex(Rndm))
            RandomBoja ='#'+ RandomBoja[2:]
        else:
            if Gumbic[row][column]['text'] == "" and Win() is False:

                if Igrac == Imena[0]:

                    Gumbic[row][column]['text'] = KrizicKruzic[0]

                    if Win() is False:
                        Igrac = Imena[1]
                        Ispis.config(text=(Imena[1]+" je na redu!!"))
                        Gumbic[row][column].config(text=KrizicKruzic[0],bg=Boja_1, height=2, width=5)

                    elif Win() is True:
                        Ispis.config(text=(Imena[0]+" je pobijedio/la!!"))
                        Bodovi1 += 1
                        Igrac1Ispis = Label(Polje, text = Imena[0]+" Bodovi --> "+str(Bodovi1), bg=Boja_1, font=('Righteous',20)).place(x=120, y=80)  
                        Igrac2Ispis = Label(Polje, text = Imena[1]+" Bodovi --> "+str(Bodovi2), bg=Boja_2, font=('Righteous',20)).place(x=670, y=80) 

                    elif Win() == "Nerijeseno":
                        Ispis.config(text="Nerijeseno!!")
                        Bodovi1 += 0
                        Bodovi2 += 0
                        Igrac1Ispis1 = Label(Polje, text = Imena[0]+" Bodovi --> "+str(Bodovi1), bg=Boja_1, font=('Righteous',20)).place(x=120, y=80)  
                        Igrac2Ispis2 = Label(Polje, text = Imena[1]+" Bodovi --> "+str(Bodovi2), bg=Boja_2, font=('Righteous',20)).place(x=670, y=80)

                else:

                    Gumbic[row][column]['text'] = KrizicKruzic[1]

                    if Win() is False:
                        Igrac = Imena[0]
                        Ispis.config(text=(Imena[0]+" je na redu!!"))
                        Gumbic[row][column].config(text=KrizicKruzic[1],bg=Boja_2, height=2, width=5)

                    elif Win() is True:
                        Ispis.config(text=(Imena[1]+" je pobijedio/la!!"))
                        Bodovi2 += 1
                        Igrac1Ispis = Label(Polje, text = Imena[0]+" Bodovi --> "+str(Bodovi1), bg=Boja_1, font=('Righteous',20)).place(x=120, y=80)  
                        Igrac2Ispis = Label(Polje, text = Imena[1]+" Bodovi --> "+str(Bodovi2), bg=Boja_2, font=('Righteous',20)).place(x=670, y=80)  

                    elif Win() == "Nerijeseno":
                        Ispis.config(text="Nerijeseno!!!")
                        Bodovi1 += 0
                        Bodovi2 += 0
                        Igrac1Ispis1 = Label(Polje, text = Imena[0]+" Bodovi --> "+str(Bodovi1), bg=Boja_1, font=('Righteous',20)).place(x=120, y=80)  
                        Igrac2Ispis2 = Label(Polje, text = Imena[1]+" Bodovi --> "+str(Bodovi2), bg=Boja_2, font=('Righteous',20)).place(x=670, y=80)

    def Win():

        for row in range(3):
            if Gumbic[row][0]['text'] == Gumbic[row][1]['text'] == Gumbic[row][2]['text'] != "":
                Gumbic[row][0].config(text="──", bg="#66ff99", height=2, width=5)
                Gumbic[row][1].config(text="──", bg="#66ff99", height=2, width=5)
                Gumbic[row][2].config(text="──", bg="#66ff99", height=2, width=5)
                return True

        for column in range(3):
            if Gumbic[0][column]['text'] == Gumbic[1][column]['text'] == Gumbic[2][column]['text'] != "":
                Gumbic[0][column].config(text="│", bg="#66ff99", height=2, width=5)
                Gumbic[1][column].config(text="│", bg="#66ff99", height=2, width=5)
                Gumbic[2][column].config(text="│", bg="#66ff99", height=2, width=5)
                return True

        if Gumbic[0][0]['text'] == Gumbic[1][1]['text'] == Gumbic[2][2]['text'] != "":
            Gumbic[0][0].config(text="\\", bg="#66ff99", height=2, width=5)
            Gumbic[1][1].config(text="\\", bg="#66ff99", height=2, width=5)
            Gumbic[2][2].config(text="\\", bg="#66ff99", height=2, width=5)
            return True

        elif Gumbic[0][2]['text'] == Gumbic[1][1]['text'] == Gumbic[2][0]['text'] != "":
            Gumbic[0][2].config(text="/", bg="#66ff99", height=2, width=5)
            Gumbic[1][1].config(text="/", bg="#66ff99", height=2, width=5)
            Gumbic[2][0].config(text="/", bg="#66ff99", height=2, width=5)
            return True


        elif Provjera() is False:
        
            for row in range(3):
                for column in range(3):
                    Gumbic[0][column].config(text="",bg='#ff4d4d', height=2, width=5)
                    Gumbic[1][column].config(text="",bg='#ffffff', height=2, width=5)
                    Gumbic[2][column].config(text="",bg='#6666ff', height=2, width=5) 
                    
                    Gumbic[row][column]['state']='disabled'
                    Gumbic[row][column]['state']='disabled'
                    Gumbic[row][column]['state']='disabled'
                    
            return Ispis.config(text="Nerijeseno!!") 
        else:
            return False


    def Provjera():

        PraznaPolja = 9

        for row in range(3):
            for column in range(3):
                if Gumbic[row][column]['text'] != "":
                    PraznaPolja -= 1

        if PraznaPolja == 0:
            return False
        else:
            return True

    def NovaIgra():

        global Igrac
        
        Ime_1 = Ime1Igraca.get()
        Ime_2 = Ime2Igraca.get()
        Imena = [Ime_1, Ime_2]
        
        Igrac = random.choice(Imena)

        Ispis.config(text=Igrac+" je na redu!!")
        
        Rndm1 = random.randint(0,16777215)
        RandomBoja1 = str(hex(Rndm1))
        RandomBoja1 ='#'+ RandomBoja1[2:]
      
        for row in range(3):
            for column in range(3):
                Gumbic[row][column].config(text="",bg=RandomBoja1)
                
                Gumbic[row][column]['state']='normal'
                Gumbic[row][column]['state']='normal'
                Gumbic[row][column]['state']='normal'
                

    Polje = Tk() 
    Polje.title("Krizic_Kruzic")   
    Polje.geometry("1024x854")      
    KrizicKruzic = ["x","o"]     
    
    global Igrac                 
    
    Ime_1 = Ime1Igraca.get()      
    Ime_2 = Ime2Igraca.get()    
    Imena = [Ime_1, Ime_2]        
    
    Igrac = random.choice(Imena)   
    Gumbic = [[0,0,0], 
              [0,0,0],
              [0,0,0]]           

    Ispis = Label(text=Igrac + " je na redu!!", font=('Righteous',45))      
    Ispis.pack(side="top")                                                

    Reset = Button(text="Reset", font=('Righteous',25), command=NovaIgra)   
    Reset.pack(side="top")                                                

    Prikaz = Frame(Polje)                                                
    Prikaz.pack()                                               

    for row in range(3):
        for column in range(3):
            Gumbic[row][column] = Button(Prikaz, text="", font=('Righteous',45), bg=RandomBoja, width=5, height=2, command=lambda row=row, column=column: Potez(row,column))     
            Gumbic[row][column].grid(row=row,column=column)         
            
            
    Polje.mainloop()





def Login():
    
    
    global Bojica1
    global Bojica2
    
    Boja_1 = Boja1[1]      
    Boja_2 = Boja2[1]
    Ime1 = Ime1Igraca.get()    
    Ime2 = Ime2Igraca.get()      
    
    
    if Ime1 == '' and Ime2 == '':      
        Poruka.set("Niste upisali imena!!")  
    elif isinstance(Boja_1, int):
        Poruka.set("Promjeni boju!!")
    elif isinstance(Boja_2, int):
        Poruka.set("Promjeni boju!!")
    elif Boja_1 == Boja_2:
        Poruka.set("Ne mozete imati iste boje!!")
    elif Ime1 == Ime2:
        Poruka.set("Ne mogu biti dva ista imena!!")  
    elif len(Ime1)>10 or len(Ime2)>10:    
        Poruka.set("Predugacko ime (do 10 slova)")
    elif Ime1 == '':
           Poruka.set("Upisi prvo ime")
    elif Ime2 == '':
           Poruka.set("Upisi drugo ime")
    else:
        Poruka.set("Upali ste u igru!!")
        Upad.destroy()           
        Krizic()                    
        
        




def IzaberiBoju1():
    global Boja1     
    
    Boja1 = colorchooser.askcolor(title="Izaberi boju")        
    Entry(Upad, font=('Righteous', 15), textvariable = Ime1Igraca, bg=Boja1[1]).place(x=250, y=42)   

def IzaberiBoju2(): 
    global Boja2

    Boja2 = colorchooser.askcolor(title="Izaberi boju")
    Entry(Upad, font=('Righteous',15), textvariable = Ime2Igraca, bg=Boja2[1]).place(x=250, y=82)
    
    
    
    
def Sucelje(): 

    global Upad      

    Upad = Tk()         
    Upad.title("Prijeva za Krizic Kruzic")              
    Upad.geometry("649x510")   

    global Poruka                   
    global Ime1Igraca             
    global Ime2Igraca
    
    Rndm1 = random.randint(0,16777215)       
    RandomBoja1 = str(hex(Rndm1))             
    RandomBoja1 ='#'+ RandomBoja1[2:]         
   
    
    Ime1Igraca = StringVar()           
    Ime2Igraca = StringVar()
    Poruka = StringVar()
    
    Poruka.set("Prvo odaberite boju!!")  

    Label(Upad,width = "300", text = "Upisite imena igraca!!", bg="#8000ff", fg="#ffff00", font=('Righteous',20)).pack()        

    Label(Upad, font=('Righteous',14), text = "Ime prvog igraca  x  ").place(x=20, y=40)  



    Label(Upad, font=('Righteous',14), text = "Ime drugog igraca  o  ").place(x=20, y=80)  
    
    Label(Upad, text="", font=('Righteous',14), textvariable = Poruka).place(x=95, y=150)           
    
    Button(Upad, text="Upad u igru", width=10, height=2, bg="#8000ff", fg="#ffffff", font=('Righteous', 18), command=Login).place(x=190, y=240)                                                                      
    
    Igrac1B = Button(Upad, text="Boja", bg="white", font=('Righteous', 7), command=IzaberiBoju1).place(x=205, y=46)                                                                                                                  
    Igrac2B = Button(Upad, text="Boja", bg="white", font=('Righteous', 7), command=IzaberiBoju2).place(x=205, y=86)                                                                                                        

    Upad.mainloop()  

Sucelje()            


