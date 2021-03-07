# AAI Company - Python 

#! sociALmediA 

# sociAlmediA aslında A'lardan anlayacağınız gibi (Aper Aybak) bizim tarafımızdan geliştirilen bir uygulama TKinter örneğinde de görülmüştür.
# Ufak bir sosyal medyamızda neler olacak kodlarla görelim :)

print("\nAA INDUSTRIES|alperaybakindustries\n")

aaliste=["Yazılım","Oyun Programlama","Web Geliştrime","Mühendislik","Eğitim (matematik,fizik ve gündem)","Teknoloji","Hologram Teknolojisi","Ekonomi ve Finans","Yabancı Dil","Spor","Motivasyon"]
a=0
for A in aaliste:
    a=a+1
    print("{}){}".format(a,A))

print("sociAlmediA'ya Üyel Olmak İster Misiniz?\nEvet/Hayır (Lütfen Cevaıbızı Yanda belirtiği Gibi Yazınız!)\n")
cevap=input()
if (cevap=="Evet"):
    print("=================sociAlmediA=================")
    while True:

        ad=input("Adınızı Giriniz:")
        soyad=input("Soyadınızı Giriniz:")
        kullanıcıadı=input("Kullanıcı Adınızı Giriniz:")

        while True:
            parola=input("Şifrenizi Giriniz:")
            parola1=input("Şifrenizi Tekrar Giriniz:")
            if (parola!=parola1):
                print("Lütfen Tekrar Deneyiniz Şifreler Eşleşmiyor!")

            else:
                print("Şifreniz Başarıyla Doğrulandı")
                break

        email=input("E-Mail Adresiniz:")
        telefon=input("Telefon Numaranız:")
        print("Bilgileriniz Kaydediliyor Lütfen Bekleyiniz...")
        print("\n\n\n=================Bilgileriniz=================")
        print("Ad:",ad,"\nSoyad:",soyad,"\nKullanıcı Adı:",kullanıcıadı,"\nŞifre:",parola,"\nE-Mail:",email,"\nTelefon:",telefon)
        while True:
            print("\n\n\nBilgilerinizi Onaylıyor Musunuz?\n\nEvet/Hayır (Lütfen Cevaıbızı Yanda belirtiği Gibi Yazınız!)")
            cevap=input()
            if (cevap=="Evet"):
                print("Kayıt İşleminiz Başarıyla Gerçekleştirilmiştir")
                print("Giriş Ekranına Yönlendiriliyorsunuz")
                break
            else:
                print("Lütfen Bilgilerinizi Kontrol Ediniz")
                print("Ad:", ad, "\nSoyad:", soyad, "\nKullanıcı Adı:", kullanıcıadı, "\nŞifre:", parola, "\nE-Mail:",email, "\nTelefon:", telefon)


else:
    print("Giriş Ekranına Yönlendiriliyorsunuz...")


print("\n=================sociAlmediA Giriş Ekranı=================\n")


kullanıcıadı=input("Kullanıcı Adınızı Giriniz:")
parola=input("Şifrenizi Giriniz:")

while True:
    kullanıcıadı1=input("Kullanıcı Adı:")
    parola2=input("Şifre:")
    if((parola==parola2)and(kullanıcıadı1==kullanıcıadı)):
        print("Giriş Başarılı")
        break

    elif((parola==parola2)and(kullanıcıadı1!=kullanıcıadı)):
        print("Kullanıcı Adınız Hatalı!")
        print("Lütfen Tekrar Deneyiniz")

    elif((parola!=parola2)and(kullanıcıadı1==kullanıcıadı)):
        print("Şifreniz Yanlış Lütfen Tekrar Deneyiniz")
        print("Şifrenizi Mi Unuttunuz? (E/H)")
        cevap=input()
        if (cevap=="E"):
            print("Lütfen Bekleyiniz...")
            while True:
                yeniparola=input("Lütfen Yeni Şifrenizi Giriniz:")
                yeniparola1=input("Lütfen Yeni Şifrenizi Tekrar Giriniz:")
                if (yeniparola==yeniparola1):
                    print("Şifreniz Onaylandı")
                    break

                else:
                    print("Şifreler Eşleşmiyor, Lütfen Tekrar Deneyiniz!")

        else:
            print("Lütfen Tekrar Deneyiniz")

print("\n-Sitemizin Ana Tasarımı Aşağıdaki Gibidir-\n")


industries=print(""""

[AA]==============sociAlmediA======[-] [O] [X]
|                                            |
| Your Story ||| STORY (yapay zeka kısmı)    |
|--------------------------------------------|
|   İSTEĞE GÖRE OLAN GÜNLÜK BÖLÜM            |
|                                            |
|   (yazılım,eğlence,dil,teknoloji...vs.)    |
|                                            |  
|  Yapay Zekaya Kalan Kaydırmalı Kısım       |
|                                            |
|   SOSYAL MEDYA  KISMI                      |
|                                            |
| AA INDUSTRIES|alperaybakindustries         |
|                                            |
|ana syf.| + |arama| |hesap||istek listesi[AA]    
|============================================|

""")

print("\n\n\n\n")
print("İstek ve Görüşlerinizi Bildirmek İster Misiniz?\nEvet/Hayır (Lütfen Belirtidiği Gibi Yazınız)")
cevap=input()
if (cevap=="Evet"):
    print("=================İstek ve Görüşlerinizi Bize Bildiriniz=================")
    input("Adınız:")
    input("Soyadınız:")
    input("E-mail:")
    input("Görüşleriniz:")
    print("Bizimle İletişime Geçtiğiniz İçin Teşekkür Ederiz...")

else:
    print("sociAlmediA Teşekkürlerini Sunar...")

print("\n\n\n\n")

print("========================Hakkımızda========================\n\n")
print("==Alper Aybak==\n-Elektrik-Elektronik ve Yazılım Mühendisliği\n-40+ Sertifika\n-AA INDUSTRIES|alperaybakindustries'in Sahibi ve Kurucusudur.\n-Gerçek Dünya'nın Tony Stark'ı Olarak Biliniyor.\n\n")
print("==Hüseyincan Bağcı==\n-Hukuk ve Fİnans\n-Alanında 10+ Sertifika\n-HCB Finance and Law'ın Kurucusu ve Sahibidir.\n-Ülkenin Sayılı Ekonomist ve Avukatlarından Olarak Biliniyor.")

print("\n\nSitemizi Ziyaret Etmek İster Misiniz?\nEvet/Hayır (Lütfen Belirtilen Şekilde Cevap Veriniz!")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyin, Yönlendiriliyorsunuz...")

    import urllib.request
    url="https://www.alperaybakindustries.com/"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Sitemiz"+".html") #! .html uzantısı ile de html linki verebilirsiniz

else:
    print("Teşekkür Ederiz.")


print("Sağlıklı Günler Dileriz,Yine Bekleriz...")