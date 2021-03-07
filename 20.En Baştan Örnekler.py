# AAI Company - Python

# En Baştan Geldiğimiz Yere Kadar Örnek Uygulama/Python Kodları

# Arkadaşlar merhaba bir sonraki dersimiz Sözlük Veri Tipi olacağı için bu konuya geçmeden sıfırdan bir tekrar edelim dedim.
# Hem hatırlamış oluruz hem de kafamıza takılan yerleri sindirmiş oluruz.
# İsterseniz başlayalım;


#! Çemberin Çevresi: (2.π.r)

r = float(input("Lütfen Çemberin Yarıçapını Giriniz: "))
π = 3.14
cevre = 2*π*r
print("Çemberin Çevresi: {} ".format(cevre))










#! +18 Mekana Giriş :

ad = input("Lütfen Adınzı Giriniz: ")
dogum_tarihi = int(input("Lütfen Doğdunuz Yılı Giriniz: "))
giris = 2021 - dogum_tarihi

if (giris<18):
    print("Sayın {} \nÜzgünüz, Yaşınız Mekana Girmek İçin Uygun Değil!".format(ad))

elif (giris==18):
    print("Sayın {}  Hoşgeldin \n Yaşınız 18 Mekana Girebilirsiniz.".format(ad))

else:
    print("Sayın {} Hoşgeldin \n Yaşınız {} Mekana Girebilirsiniz".format(ad,giris))










#! Üçgeninin Çeşidini ve Çevresini  Hesaplama

a = float(input("Lütfen a Kenarının Değerini Giriniz: "))
b = float(input("Lütfen b Kenarının Değerini Giriniz: "))
c = float(input("Lütfen c Kenarının Değerini Giriniz: "))

if (a==b==c):
    print("Bu bir eşkenar üçgen")
    print("Çevresi: {} ".format(3*a))

elif (a==b or b==c or a==c):
    print("Bu bir ikizkenar üçgen")
    print("Çevresi: {} ".format(a+b+c))

elif (a!=b and a!=c and b!=c):
    print("Bu bir çeşitkenar üçgen")
    print("Çevresi: {}".format(a+b+c))

else:
    print("Lütfen Sayı Giriniz!")
    









#! Basit LogIn Ekranı:

username  = input("Lütfen Kullanıcı Adı Oluşturunuz: ")
password  = input("Lütfen Şifre Oluşturunuz: ")

while True:
    username2 = input("Kullanıcı Adınızı Giriniz: ")
    password2 = input("Şifrenizi Giriniz: ")
    if ((username==username2) and (password2==password)):
        print("Başarılı Şekilde Giriş Yaptınız Teşekkür Ederiz...")
        print("\n\t AAI Company'e Hoşgeldiniz")
        break

    elif ((username!=username2) and (password2==password)):
        print("Kullanıcı Adınız Hatalı Lütfen Tekrar Deneyiniz")


    elif((username==username2) and (password2 !=password)):
        print("Şifrenizi Mi Unuttunuz?")
        print("Şifrenizi Değiştirmek İster Misiniz?\nLütfen Cevabı Eksiksiz ve Yazıldığı Gibi Giriniz\nEvet/Hayır")
        cevap = input()
        if (cevap == "Evet"):
            new_password = input("Lütfen Yeni Şifreyi Giriniz: ")
            print("Lütfen Bekleyiniz...")
            password=new_password
            print("Şifre Başarıyla Değiştirildi")

    else:
        print("Lütfen Tekrar Deneyiniz")

















#! Vücüt Kitle İndeksi Hesaplama:

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














#! Arabanı Oluşturma Programı:


print("Kendi Arabanı Oluşturmak İster Misin?\nLütfen Belirtildiği Gibi Eksiksiz Giriniz\nEvet/Hayır")
cevap = input()
if (cevap == "Evet"):
    print("AA Auto'ya Hosgeldiniz")
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

    elif (yil >= 2022):
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
    print("Yanlış İşlem Yaptınız ya da Reddediniz!")




















#! Faktoriyel Uygulaması:

faktoriyel = 1

while True:
    sayi = int(input("Lütfen Bir Sayı Giriniz: "))
    if (sayi<0):
        print("Lütfen Negatif Olmayan Bir Sayı Giriniz !")

    elif(sayi==0):
        print("Lütfen Sıfırdan Farklı Bir Sayı Giriniz!")

    else:
        for i in range(1,sayi+1):
            faktoriyel*=i

        print("Faktoriyel: ", faktoriyel)
        break





#! Girilen Harleri Alt Alta Sıralama:

isim=input("Adınızı Girin ")
sayac=0
while sayac < len(isim):
    print(isim[sayac])
    sayac += 1
else:
    print("Adının harflerini listeledim.")



#! Sinema veya Tiyatro Bilet 

secim = input("Sinema için (1), Tiyatro için (2) tuşlayınız : ")
ogrenci = input("Öğrenci Misiniz? (E/H) : ")
ucret = 0
 
if secim == '1':
  ucret = 40  
elif secim == '2':
  ucret = 240 
 

if ogrenci =='E' or ogrenci =='e':
  ucret= ucret - (ucret / 5 )
 
print("Ödemeniz Gereken Ücret :{}".format(ucret))




#! Asal Sayı Hesaplama:

sayac=0
sayi=input('Sayı: ')
for i in range(2,int(sayi)):
      if(int(sayi)%i==0):
            sayac+=1
            break
if(sayac!=0):
      print("Sayı Asal Değil")
else:
      print("Sayı Asal")











