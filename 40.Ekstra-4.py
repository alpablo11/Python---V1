# AAI Company - Python 

# Ekstra - 4 

# Aslında çok fazla öğretilmeyen bir sistemdir. Fakat bunu vermek istedim örnek ile de açıkladım.


#! Python Tkinter

from tkinter import *

def fonksiyon():
    print("Giriş Yapıldı. \nGiriş Bilgileri:",kutu.get(),kutu2.get())  #"get" fonksiyonu yazılanları gösterir

pencere= Tk()
pencere.title("www.sociAlmediA.com")
pencere.geometry("500x400")


yazi=Label(pencere)   #Pencere üzerine yazılacak yazı
yazi.config(text=u"AA INDUSTRIES|alperaybakindustries\n",font="calibri 12 bold ")    #yazılacak yazıyı ' .config(text="" ' şeklinde yazıyoruz.
yazi.pack()   #yazıyı bastırmak için pack komutu kullanılır.

yazi0=Label(pencere)
yazi0.config(text="from Alper Aybak\n Tüm Hakları Saklıdır ©",font="caliibri 5")   #' font="yazı türü büyüklük " ' bold=kalın yazar
yazi0.pack()



yazi2=Label(pencere)
yazi2.config(text="\n\nsociAlmediA\n",font= "courier 25 bold",bg="light blue",fg="yellow")  #bg=background dan  arka plan rengi
yazi2.pack()                                                                                #fg=fount ground dan yazı rengi


kutu=Entry(pencere)    #kutu ekleme (metin girilebilir)
yazi3=Label(pencere)
yazi3.config(text=u"Kullanıcı Adı")
yazi3.pack()
kutu.pack()

kutu2=Entry(pencere)
yazi4=Label(pencere)
yazi4.config(text=u"\nŞifre")
yazi4.pack()
kutu2.pack()



buton=Button(pencere)       #buton eklemek için kullanılır
buton.config(text=u"Giriş Yap",command=fonksiyon)
buton.pack()

mainloop()