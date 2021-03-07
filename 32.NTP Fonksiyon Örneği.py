# AAI Company - Python

# NTP Fonksiyonlarla ilgili örnek kodumuz;



class Dusman:
    

    def __init__(self,isim,kalan_can,saldiri_gucu,mermi_sayisi):
        self.isim= isim
        self.kalan_can= kalan_can
        self.saldiri_gucu= saldiri_gucu
        self.mermi_sayisi= mermi_sayisi


    def print(self):
        print("Basılıyor.....")
        print("İsim:",self.isim,"Kalan can:",self.kalan_can,"Saldırı Gücü:",self.saldiri_gucu,"Mermi Sayısı:",self.mermi_sayisi)

dusman1=Dusman("Hüseyincan Bağcı",2322,23,232)
dusman2=Dusman("Alper Aybak",11111,1111,1111)
print("Dusman1--------------------")
dusman1.print()
print("Dusman2--------------------")
dusman2.print()



# Öğretici aynı zamanda da eğlenceli bir kod oldu diğer örneğimizde görüşelim.