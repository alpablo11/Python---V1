# AAI Company - Python 

#! sociAlmediA  V2(Basit Sürüm)

# Python ile bilgi verelim biraz, olur da böyle şeyler yapmak isterseniz diye :)



#! Giriş


print("Hoşgeldiniz...\nŞuanda sociAlmediA Uygulamasına Giriş Yapmış Bulunuyorsunuz.")
print("\nBu Bir Bilgilendirmedir...")
print("\nSizinle daha samimi olabilmek için lütfen öncelikle isminizi giriniz:")
isim=input()
print("\n Tekrardan Hoşgeldin",isim)

print(isim,",öncelikle şunu belirmek isterim ki bu uygulama AA INDUSTRIES | alperaybakindustries tarafından kurulmuştur!\n")

print(isim," alperaybakindustries dediğimize göre,Alper Aybak kimdir? sorusunu merak ediyor olabilirsin...")
print("\n== Alper Aybak ==\nElektrik-Elektronik ve Yazılım Mühendisidir.\nYazılım,Web Tasarımı,Siber Güvenlik (Etik Hacker'lık),Sosyal Medya Uzmanlığı başta olmak üzere 40+ sertifikası bulunmaktadır.")
print("\n İşin en güzel yanı ise Alper Aybak, Türk'tür!")

print(isim,",neler yapıyoruz diye merak etmiş olabilirsin...\nAA INDUSTRIES | alperaybakindustries kar amacı gütmeden insanların her türlü bilgiye ulaşması için plana geçmiştir. ")
print("İki arkadaş tarafından 2020 yılının Ekim ayında hayata geçen bu proje insan ayırt etmeden herkesin ön plana çıkabileceği ve gelişebileceği kuruluştur.")
print(isim,",daha fazlasını görmek ister misin?(Evet/Hayır)")
cevap=input()
if (cevap=="Evet"):
    print("1)Yazılım ve Mühendislik\n2)Hukuk ve Finans\n3)Bilgisayar Programlama ve Bilgisayar Dilleri\n4)Yabancı Dil Öğrenebilme\n5)Spor ile İstediğin Fiziğe Ulaşabilme\n6)Motivasyon\n7)Eğitim ve Materyaller\8)Web Tasarımı\n")
    print("Bunlar ön plana çıkan desteklerimiz.\nHepsini Alper Aybak özel olarak hazırlamıştır ve son derece güvenilirdir.")

else:
    print("O zaman devam edelim ama görmeni isterdik...")



print("İstersen daha fazla uzatmadan Sosyal Medya'nın en güvenli uygulaması olan sociAlmediA'ya seni de kaydetmek için talimatları uygulayarak başlayalım")

print("Sevgili,",isim,"Lütfen Bilgileri Eksiksiz Bir Şekilde Doldurlım. (isim de dahil olmak üzere merak etme ismini unutmadık bizim için çok değerlisin...)")
print("\nBaşlayalımmmm...\n\n")

while True:
    ad=input("Lütfen Adınızı Giriniz:")
    soyad=input("Lütfen Soyadınızı Giriniz:")
    email=input("Lütfen E-Mailinizi Giriniz:")
    telefon=input("Lütfen Telefon Numaranızı Giriniz:")

    print("Lütfen Bekleyiniz...\n")
    print("\nBigileriniz Gösteriliyor...\n")

    print("İsminiz:",ad)
    print("Soyisminiz:",soyad)
    print("E-Mail Adresiniz:",email)
    print("Telefon Numaranız:",telefon)


    print("\nBilgilerini Onaylıyor Musun? (Evet/Hayır)")
    cevap=input()
    if (cevap=="Evet"):
        print("Teşekkür Ederiz Detaylı Olarak Tekrar Gösterilecektir.")
        break

    else:
        print("Lütfen Bilgilerinizi Kontrol Ediniz!")


while True:
    sifre = input("Lütfen Şifre Giriniz:")
    sifre1 = input("Lütfen Şifrenizi Tekrar Giriniz:")
    if (sifre != sifre1):
        print("Şifreniz Eşleşmiyor Lütfen Tekrar Deneyiniz!")



    else:
        print("Şifreniz Eşleşiyor Lütfen Devam Ediniz")
        break




print("İsminiz:",ad)
print("Soyisminiz:",soyad)
print("E-Mail Adresiniz:",email)
print("Telefon Numaranız:",telefon)
print("Şifreniz:",sifre)

print("\nsociAlmediA'ya Hoşgeldiniz...\Başarılı Şekilde Kaydınız Tamamlanmıştır.\nİyi Eğlenceler Dileriz...")


#! Hakkımızda 

print("\n== Hakkımızda ==\n")

print("sociAlmediA Türk Girişimci Gençlerin Şirketleri:\n AA INDUSTRIES | alperaybakindustries ve HCB Finance and Law\n ortaklığında kurulmuştur. ")
print("Alper Aybak:\n*AA INDUSTRIES | alperaybakindustries'in sahibi ve kurucusu.\n*11 Haziran 2002 Doğumludur.\nElektrik-Elektronik ve Yazılım Mühendisliği\n*40+ Sertifikası Bulunmaktadır.")
print("Hüseyincan Bağcı:\n*HCB Finance and Law'ın sahibi ve kurucusu.\n*23 Nisan 2001 Doğumludur.\n Hukuk ve Ekonomi\n*Alanında Uzmandır ve Yurt Dışı Yayın ve Makaleleri Mevcuttur.")
print("sociAlmediA .... senesinde kurulmuştur ve tüm hakları saklıdır.")
print("Alper Bey ve Hüseyin Bey'e sevgilerimizi iletiyor ve başarılarının devamını diliyoruz.")


#! Basit Tkinter 

from tkinter import *

pencere = Tk()

pencere.title("www.sociAlmediA.com")
pencere.geometry("400x300")


uygulama = Frame(pencere)
uygulama.grid()



L1 = Label(uygulama, text="Kullanıcı Adı")
L1.grid(padx=110, pady=10)

E1 = Entry(uygulama, bd=2)
E1.grid(padx=110, pady=3)

L2 = Label(uygulama, text="Şifre")
L2.grid(padx=110, pady=10)


E2 = Entry(uygulama, bd=2)
E2.grid(padx=110, pady=3)

L4=Label(uygulama,text="\n\nAA INDUSTRIES| alperaybakindustries\n=sociAlmediA=")
L4.grid(padx=110,pady=10)

pencere.mainloop()


#! Site Yönlendirmesi (alperaybakindustries.com)

print("AA INDUSTRIES | alperaybakindustries Sitemizi Görmek İster Misiniz? (Evet/Hayır)")
cevap=input()

if (cevap=="Evet"):
    print("Lütfen Bekleyiniz Yönlendiriliyorsunuz...")
    import urllib.request
    url="https://www.alperaybakindustries.com/"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Sitemiz:AA INDUSTRIES | alperaybakindustries"+".html")

else:
    print("Lütfen Devam Ediniz...")



#! print() Fonksiyonu ile Şema

print("""
... [AA]========AA INDUSTRIES |alperaybakindustries========[-][o][x]
... |                                                              |
... | AA INDUSTRIES'e Hoşgeldiniz!                                 |
... |          |alperaybakindustries                               |
... |                                                              |
    |  Devam etmek için herhangi                                   |
... | bir düğmeye basın.                                           |
... |                                                              |
... |==============================================================|                           
... """)



# Biraz olaya eğlence katmak istedim ufak bir tekrar olmuş oldu hem de print ile başka şeyler de yapılacağını da gördük.
