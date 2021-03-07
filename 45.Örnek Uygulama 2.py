# AAI Company - Python 

# Örnek Uygulama - 2

#! Sizler için kodların çoğunu birleştirmek istedim ve bir tekrar ile Yapay Zekasız Site gibi kod yazmak istedim;


print("Hoşgeldiniz\n")


yas=int(input("Lütfen Yaşıınızı Giriniz:"))
if (yas>=15):
    print("Hoşgeldiniz...")
    print("Yönlendiriliyorsunuz Lütfen Bekleyiniz...")

else:
    print("Lütfen Yaşınızı Doğru Girdiğinizden Emin Olunuz!")



print("Sitemizde Şunlar Mevcuttur:\n1)Yazılım\n2)Eğitim\n3)Spor İlgili Herşey\n4)Eğlence")
print("İmkanlarınmızdan Yararlanmak İçin İlk Önce Üye Olmak Zorundasınız")
print("Üye Olmak İster Misiniz?\nZaten Üyeyim/Üye Ol")


cevap = input()
if (cevap == "Üye Ol"):
    print("Bekleyiniz...")
    print("Lütfen Aşağıdaki Boşlukları Doldurunuz...\n")

    ad = input("Lütfen Adınızı Giriniz:")
    soyad = input("Lütfen Soyadınızı Giriniz:")
    
    
    
    
    dogum_ayı=int(input("Doğduğunuz Ayı Giriniz:"))
    dogum_günü=int(input("Doğuğunuz Günü Giriniz:"))
    dogum_yılı=int(input("Doğdunuz Yılı Giriniz:"))
    
    
    
    
    if (dogum_yılı>=2005):
        print("Lütfen Devam Ediniz...")
        
    else:
        print("Lütfen Çıkış Yapınız Çok Küçüksünüz!")
        
    
    
    
    
    
    
    
    
    telefon = input("Lütfen Telefon Numaranızı Giriniz:")
    mail = input("Lütfen Mail Adresinizi Giriniz:")
   
   
   
   
    cinsiyet = input("Lütfen Cinsiyetinizi Seçiniz:\nSeçenek 1:Kadın\nSeçenek 2:Erkek\nSeçenek 3:Belirtmek İstemiyorum")
    while True:
        print("Lütfen Bir Seçenek Seçiniz:")
        cevap = input()
        if (cevap == "Seçenek 1"):
            print("Cinsiyet: Kadın")
            break

        elif (cevap == "Seçenek 2"):
            print("Cinsiyet: Erkek")
            break


        else:
            print("Cinsiyet Belirtmediniz.")
            break

    meslek = input("Lütfen Mesleğinizi Giriniz:")
    kullanıcıadı = input("Lütfen Bir Kullanıcı Adı Oluşturunuz:")

    while (True):
        parola1 = input("Lütfen Parola Giriniz:")
        parola2 = input("Lütfen Girdiğiniz Parolayı Tekrar Giriniz")
        if (parola1 == parola2):
            print("Lütfen Devam Ediniz...")
            break

        else:
            print("Lütfen Paroların Eşleştiğinden Emin Olunuz")




    print("Hoşgeldin=", kullanıcıadı)
    print("Bilgileriniz Gösteriliyor...")
    print("Lütfen Bekleyiniz...")
    print("Ad::", ad)
    print("Soyad:", soyad)
    print("Telefon Numarası:", telefon)
    print("Mail Adresiniz:", mail)
    print("Mesleğiniz:", meslek)
    print("Kullanıcı Adınız:", kullanıcıadı)
    print("Şifreniz:", parola1)
    print("Doğum Tarihiniz:",dogum_günü,dogum_ayı,dogum_yılı)

else:
    print("Lütfen Devam Ediniz...")










print("Sisteme Giriş Yapmak İster Misiniz?\n(Evet/Hayır)")
cevap = input()
if (cevap == "Evet"):
    print("Lütfen Kullanıcı Adınızı ve Parolanızı Giriniz...")

defkullanıcı = "alpablo11"
defparola = "1121"
while (True):
    kullanıcı = input("Kullanıcı Adı:")
    parola = input("Parola Giriniz:")
    if ((kullanıcı == defkullanıcı) and (parola == defparola)):
        print("Hoşgeldiniz", kullanıcı)
        break

    elif ((kullanıcı != defkullanıcı) and (parola == defparola)):
        print("Kullanıcı adınız yanlıs")
    elif ((kullanıcı == defkullanıcı) and (parola != defparola)):
        print("Şifrenizi mi unuttunuz?")
        print("Şifrenizi değiştirmek ister misiniz? (E/H)")
        cevap = input()
        if (cevap == "E"):
            yeniparola = input("Yeni Parola:")
            print("Lütfen bekleyiniz...")
            defparola = yeniparola
            print("Şifre Başarıyla Değiştirildi")
        else:
            print("Tekrar Deneyiniz")
    else:
        print("Sisteme Giriş Yapmadınız!")

else:
    print("Lütfen Sisteme Giriş Yapınız!")











print("Vücut Kitle İndeksinizi Hesaplamak İster Misiniz?\n(Evet/Hayır)")
cevap = input()
if (cevap == "Evet"):
    print("Lütfen Bekleyiniz...")
    agirlik = float(input("Lütfen ağırlığınızı giriniz(kg): "))
    boy = float(input("Lütfen boyunuzu giriniz(cm): "))

    vki = agirlik / ((boy / 100) * (boy / 100))
    print("Vücut Kitle İndeksiniz: ", vki)
    print("Mevcut Durumunuz: ")
    if (vki <= 20):
        print("Zayıf")
    elif (vki <= 24.9):
        print("Normal")
    elif (vki <= 29.9):
        print("Hafif Şişman")
    elif (vki <= 34.9):
        print("Şişman")
    elif (vki <= 44.9):
        print("Sağlık Açısından Önemli")
    elif (vki <= 49.9):
        print("Aşırı Şişman")
    else:
        print("Ölümcül Şişman")

else:
    print("Lütfen Devam Ediniz...")











print("Kendi Arabanı Oluşturmak İster Misin?\n(Evet/Hayır)")
cevap = input()
if (cevap == "Evet"):
    print("AA INDUSTRIES'e Hosgeldiniz")
    print("Size Nasil Yardimci Olabiliriz?")
    print("Lutfen Araba Bilgilerini Girmek Icin Devam Ediniz.")
    print("Bilgiler Yukleniyor Lutfen Bekleyiniz...")

    while (True):
        tekerlek = int(input("Tekerlek Sayisi:"))
        yil = int(input("Yil:"))
        marka = input("Marka:")
        model = input("Model Ismi:")
        motor = float(input("Motor Gücü:"))
        beygir = float(input("Beygiri:"))
        break
    print("Bizi Tercih Ettiginiz Icin Tesekkur Ederiz...\n-AA INDUSTRIES")

    if (tekerlek <= 3):
        print("Yanlıs Giris Yaptiniz!")
        print("Yeniden Denemek Ister Misiniz? (E/H)")
        cevap = input()
        if (cevap == "E"):
            yenitekerlek = int(input("Lutfen Tekrar Giriniz:"))
            print("Lutfen Bekleyiniz...")
            yenitekerlek = tekerlek
            print("Lutfen Devam Ediniz!")
            yil = int(input("Yil:"))
            marka = input("Marka:")
            model = input("Model Ismi:")
            motor = float(input("Motor Gücü:"))
            beygir = float(input("Beygiri:"))
            print("Bizi Tercih Ettiginiz Icin Tesekkur Ederiz...\n-AA INDUSTRIES")

        else:
            print("Sonuc Bulunamadi.")
            print("Bizi Tercih Ettiginiz Icin Tesekkur Ederiz...\n-AA INDUSTRIES")

    elif (tekerlek >= 5):
        print("Yanlıs Giris Yaptınız")
        print("Yeniden Denemek Ister Misiniz? (E/H)")
        cevap = input()
        if (cevap == "E"):
            yenitekerlek = int(input("Lutfen Tekrar Giriniz:"))
            print("Lutfen Bekleyiniz...")
            yenitekerlek = tekerlek
            print("Lutfen Devam Ediniz!")
            yil = int(input("Yil:"))
            marka = input("Marka:")
            model = input("Model Ismi:")
            motor = float(input("Motor Gücü:"))
            beygir = float(input("Beygiri:"))
            print("Bizi Tercih Ettiginiz Icin Tesekkur Ederiz...\n-AA INDUSTRIES")

        else:
            print("Sonuc Bulunamadi.")
            print("Bizi Tercih Ettiginiz Icin Tesekkur Ederiz...\n-AA INDUSTRIES")

    elif (yil >= 2021):
        print("Henuz Sonuclari Gosteremiyoruz!")
        print("Yeniden Denemek Ister Misiniz? (E/H)")
        cevap = input()
        if (cevap == "E"):
            yeniyil = int(input("Lutfen Tekrar Giriniz:"))
            print("Lutfen Bekleyiniz...")
            yeniyil = yil
            print("Lutfen Devam Ediniz!")
            marka = input("Marka:")
            model = input("Model Ismi:")
            motor = float(input("Motor Gücü:"))
            beygir = float(input("Beygiri:"))
            print("Bizi Tercih Ettiginiz Icin Tesekkur Ederiz...\n-AA INDUSTRIES")


        else:
            print("Sonuc Bulunamadi.")
            print("Bizi Tercih Ettiginiz Icin Tesekkur Ederiz...\n-AA INDUSTRIES")

else:
    print("Lütfen Devam Ediniz...")










print("Şirketiniz İle İlgili Veri Tabanı Oluşturmak İster Mİsiniz?\nEvet/Hayır\nLütfen Cevabınızı Giriniz:")
cevap = input()
if (cevap == "Evet"):
    print("Lütfen Bekleyiniz...")
    print("AA INDUSTRIES'e Hoşgeldiniz")


    class Calisan():
        def __init__(self, isim, maas, meslek):
            self.isim = isim
            self.maas = maas
            self.meslek = meslek

        def bilgilerigoster(self):
            print("Çalışan bilgileri Gösteriliyıor....")
            print("İsim:", self.isim, "Maaş:", self.maas, "Meslek:", self.meslek)

        def maasazamyap(self, zam_miktari):
            print("Maaşa Zam Yapıldı.")
            self.maas += zam_miktari

        def pozisyondegistir(self, yeni_pozisyon):
            print("Meslek Değiştiriliyor....")
            self.meslek = yeni_pozisyon


    class Yonetici(Calisan):
        def __init__(self, isim, maas, meslek, kisi_sayisi):
            print("Yönetici Sınıfının Bilgileri!")
            super().__init__(isim, maas, meslek)
            self.kisi_sayisi = kisi_sayisi

        def bilgilerigoster(self):
            print("Bilgiler Göstyeriliyor...")
            print("İsim:", self.isim, "Maaş:", self.maas, "Meslek:", self.meslek, "Kişi Sayısı:",
                  self.kisi_sayisi)

        def kisisayisiartir(self, artir):
            print("Kişi Sayısı Artırılıyor...")
            self.kisi_sayisi += artir


    yonetici = Yonetici("Alper Aybak", 100000, "Elektrik-Elektronik ve Yazılım Mühendisi", 10000)
    yonetici.bilgilerigoster()
    yonetici.kisisayisiartir(1000)
    yonetici.bilgilerigoster()

    yonetici = Yonetici("Hüseyincan Bağcı", 80000, "Avukat ve Finans Uzmanı", 1000)
    yonetici.bilgilerigoster()

else:
    print("Lütfen Devam Ediniz...")



print("Bundan Sonraki İşlemler Çoğunlukla İnteraktif Olacaktır")
print("Web Tarayıcıları Gösteriliyor...")



print("İndirebileceğiniz İçerikler\n\n1)Google Chrome\n2)Mozilla\n3)Microsoft Edge\n4)Safari(IOS)")





print("Google Chrome İndirmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Veriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")

    import urllib.request
    url="https://www.google.com/intl/tr_tr/chrome/"
    urlistesi=[url]
    for url in urlistesi:
        urllib.request.urlretrieve(url,"Google Chrome İndirin"+".html")

else:
    print("Lütfen Devam Ediniz...")









print("Mozilla İndirmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Veriniz:")
cevap = input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")

    import urllib.request

    url = "https://www.mozilla.org/tr/firefox/new/"
    urlistesi = [url]
    for url in urlistesi:
        urllib.request.urlretrieve(url, "Mozilla İndirin" + ".html")

else:
    print("Lütfen Devam Ediniz...")










print("Microsoft Edge İndirmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Veriniz:")
cevap = input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")

    import urllib.request

    url = "https://www.microsoft.com/tr-tr/edge"
    urlistesi = [url]
    for url in urlistesi:
        urllib.request.urlretrieve(url, "Microsoft Edge İndirin" + ".html")

else:
    print("Lütfen Devam Ediniz...")









print("Safari İndirmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Veriniz:")
cevap = input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")

    import urllib.request

    url = "https://www.apple.com/tr/safari/"
    urlistesi = [url]
    for url in urlistesi:
        urllib.request.urlretrieve(url, "Safari İndirin" + ".html")

else:
    print("Lütfen Devam Ediniz...")










print("Spor Hakkında Bilgi Almak İster Misiniz?\nEvet/Hayır\nLütfen Cevabınızı Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request
    url="https://www.alperaybakindustries.com/product-page/e-book"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Eklenti"+".html")

else:
    print("Lütfen Devam Ediniz...")











print("Fizik 1 ve Fizik 2 Ders Notlarını Görmek İster Mİsiniz?\nEvet/Hayır\nLütfen Cevabınızı Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...\n")
    import urllib.request
    url1="https://www.alperaybakindustries.com/product-page/fizik-1"
    url2="https://www.alperaybakindustries.com/product-page/fizik-2"
    say=1
    urllistesi=[url1,url2]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Ders Notları"+str(say)+".html")
        say+=1
else:
    print("Lütfen Devam Ediniz...")












print("Python Hakkıda Bilgi İster Misiniz?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request
    url="https://www.alperaybakindustries.com/product-page/python3-a%C3%A7%C4%B1klamal%C4%B1"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Python"+".html")

else:
    print("Lütfen Devam Ediniz...")











print("LINUX Hakkıda Bilgi İster Misiniz?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request
    url="https://www.alperaybakindustries.com/product-page/gnu-linux"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"LINUX"+".html")

else:
    print("Lütfen Devam Ediniz...")









print("C'ye Dair Her Şeyi Öğrenmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request
    url="https://www.alperaybakindustries.com/product-page/c-programlama-dili-c-c-c"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"C'ye Dair Herşey"+".html")

else:
    print("Lütfen Devam Ediniz...")








print("PCB Hakkında Bir Şeyler Öğrenmek İster Misiniz?\nEvet/Hayır\nLütfen Cevabınızı Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request
    url="https://www.alperaybakindustries.com/product-page/pcb-tasar%C4%B1m-kurallar%C4%B1-ve-uygulama"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"PCB"+".html")

else:
    print("Lütfen Devam Ediniz....")









print("İnstagram Sayfamızı Görmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request
    url = "https://www.instagram.com/alperaybakindustries/"
    urllistesi = [url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"İnstagram" + ".html")

else:
    print("Lütfen Devam Ediniz...")









print("Kişisel Sayfamızı Görmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request
    url = "https://www.alperaybakindustries.com/"
    urllistesi = [url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"AA INDUSTRIES" + ".html")

else:
    print("Lütfen Devam Ediniz...")









sozluk={"AA INDUSTRIES":"Dünyanın Ötesinde","no excuses":"bahane yok!","grind":"it gibi çalışmak","%1 club":"%1'lik çete","stronger":"güçlü"}

print(sozluk["AA INDUSTRIES"])
print(sozluk["no excuses"])
print(sozluk["grind"])
print(sozluk["%1 club"])
print(sozluk["stronger"])










print("Motivasyon İster Misiniz?\nEvet/Hayır\nLütfen Cevabınızı Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Hayallerinin Peşinden Giderek Sen de Bize Katıl!\n")
    print("Bu Yola Ayağını Sevenler Çıkamaz!\n")
    print("Başarı,hayatınızda kimse yokken inşa ettiğiniz o heykeli sergileme anıdır.\n")
    print("Yorulduğunda dinlenmeyi öğren, bırakmayı değil.\n")
    print("yıl içinde olacağın kişi çoğunlukla bugün okuduğun kitaplara, birlikte olduğun insanlara, yediğin yemeklere, sürdürdüğün alışkanlıklarına ve girdiğin konuşmalara göre şekillenecek.\n")
    print("Senin de Bir Kazanan Olduğunun Göstergesi Kazanmayı En Az Senin Kadar Kafasına Koymuş İnsanlarla İlerlemendir!")

else:
    print("Lütfen Devam Ediniz....")








print("Sitemizin Logolarını Görmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request

    url1 = "https://scontent-iad3-1.cdninstagram.com/v/t51.29350-15/121629517_383651569335902_8854650872178666659_n.jpg?_nc_cat=107&_nc_sid=8ae9d6&_nc_ohc=iQiNivGyAuMAX9JZyqq&_nc_ht=scontent-iad3-1.cdninstagram.com&oh=7959a50f049be4151f39a8a97d41af4f&oe=5FAF9B1D"
    url2 = "https://scontent-iad3-1.cdninstagram.com/v/t51.29350-15/121336081_705155453767787_6778032169912422714_n.jpg?_nc_cat=110&_nc_sid=8ae9d6&_nc_ohc=FDyXs-wmMBgAX9_6dfA&_nc_ht=scontent-iad3-1.cdninstagram.com&oh=70f6239c1af2606abc382b161c4c63ad&oe=5FB06ACA"

    urllistesi = [url1, url2]
    say = 1
    for url in urllistesi:
        urllib.request.urlretrieve(url, "Logo" + str(say) + ".jpg")
        say += 1

else:
    print("Lütfen Devam Ediniz...")


print("Blog Yazılarımıza Bakmaya Ne Dersiniz? \nEvet/Hayır\nLütfen Cevap Veriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    import urllib.request
    url="https://www.alperaybakindustries.com/blog"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Blog Yazılarımız"+".html")


else:
    print("Lütfen Devam Ediniz...")






print("Biraz Oyun Oynamaya Ne Dersin?\nEvet/Hayır\nLütfen Cevabınızı Giriniz:")
cevap=input()

if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    print("Yeniden AA INDUSTRIES Oyunlarına Hoşgeldiniz...")

    ad = input("Adınız:")
    soyad = input("Soyadınız:")
    yas = int(input("Yaş:"))

    if (yas >= 18):
        print("Mekana Girebilirsiniz!")
        print("İyi Eğlenceler...")

    else:
        print("Mekana Giremezsiniz!")
        print("Burası İçin Küçüksünüz")


    class Dusman():
        kalan_can = 10

        def saldir(self):
            print("HÜCUUUUUUUUUUUM")
            self.kalan_can -= 1

        def hayatta_mi(self):
            if (self.kalan_can <= 0):
                print("Öldünüzz! :(")

            else:
                print(str(self.kalan_can) + "Canım Kaldı! Yaşasınnnnn....")


    dusman1 = Dusman()
    dusman2 = Dusman()

    dusman1.saldir()
    dusman1.saldir()
    dusman1.saldir()
    dusman1.hayatta_mi()

    dusman2.saldir()
    dusman2.saldir()
    dusman2.saldir()
    dusman2.saldir()
    dusman2.saldir()
    dusman2.saldir()
    dusman2.saldir()
    dusman2.saldir()
    dusman2.saldir()
    dusman2.saldir()
    dusman2.hayatta_mi()







print("İnstagramda Gezmek İster Misini?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...\n")
    import  urllib.request
    url="https://www.instagram.com/accounts/emailsignup/?hl=tr"
    urllistesi=[url]
    for  url in urllistesi:
        urllib.request.urlretrieve(url,"İnstagram'da Gezinti"+".html")

else:
    print("Lütfen Devam Ediniz...")







print("Facebbok'ta Gezinmek İster Misiniz?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...\n")
    import urllib.request
    url="https://tr-tr.facebook.com/"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Facebook'ta Gezinti"+".html")

else:
    print("Lütfen Devam Ediniz...")









print("Whatsapp'a Geçiş Yapmak İster Misiniz?\nEvet/Hayır\nLütfen Cevabınızı Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...\n")
    import urllib.request
    url="https://www.whatsapp.com/?lang=tr"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Whatsapp'Git"+".html")


else:
    print("Lütfen Devam Ediniz....")










print("Bizi Değerlendirmek İster Misiniz?")
print("Evet/Hayır")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz....\n\n")
    print("Lütfen Yönlendirileceğiniz Adreste En Alta İnerek Formu Doldurunuz...\n")
    import urllib.request
    url="https://www.alperaybakindustries.com/"
    urllistesi=[url]
    for url in urllistesi:
        urllib.request.urlretrieve(url,"Bizi Değerlendirin"+".html")

else:
    print("Yönlendiriliyorsunuz....")








print("Gitmeden Son Kez Oyun Oynamak İster Misin?\nEvet/Hayır\nLütfen Cevap Giriniz:")
cevap=input()
if (cevap=="Evet"):
    print("Lütfen Bekleyiniz...")
    print("\nVe işte karşındaaaa.....")
    print("AA INDUSTRIES Oyun Salonuna Hoşgeldiniz")
    print("Lütfen Bilgilerinizi Giriniz...")
    isim = input("İsim:")
    soyisim = input("Soyisim:")
    yas = int(input("Yaş:"))

    if (yas < 18):
        print("Mekana Girmek İçin Küçüksünüz")
    else:
        print("Mekana Girebilirsiniz.")

    print("Dikkat! Mekan:18+")

    print("Lütfen Karakter Seçiniz? (Iron-MAN/Thor)")
    print("Eğer Thor ise Kazandınız!\nİzleyelim...")
    print("Eğer Iron-MAN ise Kaybettiniz!\nİzleyelim...")


    class Dovus():

        def __init__(self, isim, saldiri_gucu, kalan_can, mermi_sayisi):
            self.isim = isim
            self.saldiri_gucu = saldiri_gucu
            self.kalan_can = kalan_can
            self.mermi_sayisi = mermi_sayisi

        def print(self):
            print("Basılıyor....")
            print("İsim:", self.isim, "Saldırı Gücü:", self.saldiri_gucu, "Kalan Can:", self.kalan_can, "Mermi Sayısı:",
                  self.mermi_sayisi)


    dovuscu1 = Dovus("Iron-MAN", 100000, 10, 10000)
    dovuscu2 = Dovus("Thor", 400000, 100, 90)

    print("Dövüşçü1*******************************")
    dovuscu1.print()
    print("Dövüşçü2*******************************")
    dovuscu2.print()

    print("Thor Kazandı")
    print("Iron-MAN Kaybetti")





print("It's a dog eat dark world and here.")







print("Ekibimiz Karşınızda...\n")
print("Yükleniyor...\n")

print("Lütfen Sol Tarafa Bakınız!")


import urllib.request
url="https://www.alperaybakindustries.com/ekip"
urllistesi=[url]
for url in urllistesi:
    urllib.request.urlretrieve(url,"Ekibimiz"+".html")






print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz...\n")
print("Lütfen En Güncel Bilgiler İçin Takipte Kalın!\n")
print("-Alper Aybak\n-AA INDUSTRIES|alperaybakindustries\n")
print("Yine Bekleriz...")



