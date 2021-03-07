# AAI Company - Python 

# Ekstralar - 5 

# Başka bir tkinter örneğimizi görelim

#! Python Tkinter V2;

from tkinter import *
import time


pencere= Tk()
pencere.title("Dijital Saatim V0.1")
zaman1=''
tiktak=Label(pencere, font=('times',111,'bold'), bg='yellow')

tiktak.grid()

def saat():
    global zaman1
    zaman2=time.strftime('%H:%M:%S')


    if zaman2 != zaman1:
        zaman1=zaman2
        tiktak.config(text=zaman2)
        tiktak.after(50,saat)
       

saat()
pencere.mainloop( )



# Dijital Saattir.