# AAI Company - Python 

#! Python Tkinter (GUI Programlama)

# Tkinter, Python için standart GUI kütüphanesidir. Python, Tkinter ile kullanıldığında GUI uygulamaları yapılabilmektedir.
# Tkinter kullanarak bir GUI uygulaması oluşturmak için tek yapmanız gereken aşağıdaki adımları uygulamak.
# Tkinter modülünü içe aktarın.
# GUI uygulaması ana penceresini oluşturun.
# GUI uygulamasına buton ve daha fazlasını ekleyin.
# Kullanıcı tarafından tetiklenen her bir olay için ana döngüyü yazın;

from tkinter import *
window = Tk()
window.title("Test")
window.geometry("400x200")
window.mainloop()


#* Hata alırsanız tkinter yüklemeliyiz ==> sudo apt-get install python-tk


#! Tkinter Buton Ekleme

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("alperaybakindustries.com")
window.geometry("400x200")
def ButtonFunc():
 messagebox.showinfo( "alperaybakindustries.com", "AAI Company")
B = Button(window, text ="Hello", command = ButtonFunc)
B.pack()
window.mainloop()



#! Tkinter Canvas Ekleme
# Canvas, resim veya diğer karmaşık düzenleri çizmek için tasarlanmış dikdörtgen bir alandır. Tuval üzerine grafik, metin, widget veya çerçeve yerleştirebilirsiniz.

from tkinter import *
window = Tk()
window.title("alperaybakindustries.com")
window.geometry("400x200")
C = Canvas(window, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()
window.mainloop()


#! Tkinter Checkbutton Ekleme

from tkinter import *
window = Tk()
window.title("alperaybakindustries.com")
window.geometry("400x200")
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(window, text = "Alper Aybak", variable = CheckVar1, \
onvalue = 1, offvalue = 0, height=5, \
width = 20)
C2 = Checkbutton(window, text = "Hüseyincan Bağcı", variable = CheckVar2, \
onvalue = 1, offvalue = 0, height=5, \
width = 20)
C1.pack()
C2.pack()
window.mainloop()



#! Tkinter Entry Ekleme

from tkinter import *
window = Tk()
window.title("alperaybakindustries.com")
window.geometry("400x200")
L1 = Label(window, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(window, bd =5)
E1.pack(side = RIGHT)
window.mainloop()



#! Tkinter Listbox Ekleme

from tkinter import *
window = Tk()
window.title("alperaybakindustries.com")
window.geometry("400x200")
Lb1 = Listbox(window)
Lb1.insert(1, "C")
Lb1.insert(2, "C++")
Lb1.insert(3, "C#")
Lb1.insert(4, "JAVA")
Lb1.insert(5, "Python")
Lb1.insert(6, "Web Development")
Lb1.insert(7, "from Alper Aybak")
Lb1.pack()
window.mainloop()



#! Tkinter Menubuton Ekleme

from tkinter import *
window = Tk()
window.title("alperaybakindustries.com")
window.geometry("400x200")
mb=  Menubutton ( window, text="AAI Company", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu
var1 = IntVar()
var2 = IntVar()
mb.menu.add_checkbutton ( label="Alper",variable=var1 )
mb.menu.add_checkbutton ( label="Aybak",variable=var2 )
mb.pack()
window.mainloop()