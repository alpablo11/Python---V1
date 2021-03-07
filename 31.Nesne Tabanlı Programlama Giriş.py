# AAI Company - Python

# Nesne Tabanlı Programlamaya Giriş (NTP)

#! Sınıf Nedir? 
# Sınıflar nesne üretebilmemizin sağlayan araçlardır kısaca.
# Yani bizim NTP için ihtiyacımız olan şey sınıflardır.
# Fonksiyonlarda "def" şeklinde fonksiyon oluşturabildiğimiz gibi, sınıflarda da "class" şeklinde oluşturuyoruz.
# Sınıf nasıl tanımlanır görelim o zaman;

class Yeni_Sinif:
    pass

#! class'tan sonra büyük harfle başlamak bir kültür gibidir. Küçük harf ile de başlayabilirsiniz.
# Daha net bir tanım kafamızda oluşturmak için şu örneğe bakalım;

class AAI_Company:
    isim = "Alper Aybak"
    araba = "Audi R8"
    meslek = "Software"

print(AAI_Company.isim)
print(AAI_Company.araba)
print(AAI_Company.meslek)

# Çıktılar: 
# Alper Aybak
# Audi R8
# Software

# Görüldüğü gibi sınıfımızdan çağırmak istediğimiz nesneyi sınıf adı daha sonra nokta ve hangi veriyi istediğimizi yazıyoruz ve bu şekilde çıktısını alabiliyoruz.

# Sınıf çok uzun diyelim araba ve mesleği değiştirmek istiyorum, nasıl yaparım? Görelim;

class AAI_Company:
    isim = "Alper Aybak"
    araba = "Audi R8"
    meslek = "Software"

print(AAI_Company.isim)
AAI_Company.araba = "Audi A5 Coupe"
print(AAI_Company.araba)
AAI_Company.meslek = "Engineer"
print(AAI_Company.meslek)

# Çıktımız =>
# Alper Aybak
# Audi A5 Coupe
# Engineer

# Gördüğümüz gibi başka bir değer atamak istiyorsak veya değiştirmek bu işlemi yapıyoruz.



#! Sınıf Nitelikleri
# Niteliğin Python'da da karşılığı normal sözlükte niteliğin karşılığı ile aynıdır.
# Yani herhangi bir objenin özelliklerini temsil ediyor.
# Örneğin bir köpeğe isim verirsek bu köpeğin niteliği olmuş oluyor
# Sınıflarımızın niteliklerini kodlayıp onlarla işlem yapacağız, görelim;

class Kutuphane:
    kitaplar = list()
    # Şimdi birkaç kitap ekleyelim;
Kutuphane.kitaplar.append("Kitap 1")
Kutuphane.kitaplar.append("Kitap 2")
Kutuphane.kitaplar.append("Kitap 3")

for i in Kutuphane.kitaplar:
    print(i)

# Çıktımız => 
# Kitap 1
# Kitap 2
# Kitap 3


#! Sınıfın Örneklemesi 
# AAI Company için çalışanları eklemek istiyorum diyelim ki 30 tane bunları tek tek eklemek yerine kolayca eklemek istiyorum nasıl yaparım?
# İsterseniz önce bir tane üretelim sonra diğerlerine bakarız;

class AAI_Company:
    maas = 30000
    bolum = "yazilim"

alper = AAI_Company
# Böylece alper ve AAI Company aynı id değerine sahip oldu görelim isterseniz;

print(id(AAI_Company)) == id(alper)

# Çıktımız ==> True

# Eğer sınıftan yeni örnek elde edeceksek parantez koyuyoruz;

class AAI_Company:
    maas = 30000
    bolum = "yazilim"

alper = AAI_Company()


# Detayları gördüğümüze göre kodumuza gelelim;

class AAI_Company:
    maas = 30000
    bolum = "yazilim"

calisanlar = list()

for i in range(30):
    calisanlar.append(AAI_Company())

for i in calisanlar:
    print(i)


# Çıktımız :
# <__main__.AAI_Company object at 0x0177E4F0>
# <__main__.AAI_Company object at 0x0177EC10>
# <__main__.AAI_Company object at 0x0190C1A8>
# <__main__.AAI_Company object at 0x0190C220>
# <__main__.AAI_Company object at 0x0190C1D8>
# <__main__.AAI_Company object at 0x0190C1C0>
# <__main__.AAI_Company object at 0x0190C208>
# <__main__.AAI_Company object at 0x0190C238>
# <__main__.AAI_Company object at 0x0190C250>
# <__main__.AAI_Company object at 0x0190C268>
# <__main__.AAI_Company object at 0x0190C3B8>
# <__main__.AAI_Company object at 0x0190C3D0>
# <__main__.AAI_Company object at 0x0190C340>
# <__main__.AAI_Company object at 0x0190C298>
# <__main__.AAI_Company object at 0x0190C2B0>
# <__main__.AAI_Company object at 0x0190C358>
# <__main__.AAI_Company object at 0x0190C2F8>
# <__main__.AAI_Company object at 0x0190C388>
# <__main__.AAI_Company object at 0x0190C2E0>
# <__main__.AAI_Company object at 0x0190C3E8>
# <__main__.AAI_Company object at 0x0190C400>
# <__main__.AAI_Company object at 0x0190C418>
# <__main__.AAI_Company object at 0x0190C430>
# <__main__.AAI_Company object at 0x0190C448>
# <__main__.AAI_Company object at 0x0190C460>
# <__main__.AAI_Company object at 0x0190C478>
# <__main__.AAI_Company object at 0x0190C490>
# <__main__.AAI_Company object at 0x0190C4A8>
# <__main__.AAI_Company object at 0x0190C4C0>
# <__main__.AAI_Company object at 0x0190C4D8>

# Bu 30 satırın hepsi Çalışanları tmsil ediyor.
# Peki bunlara nasıl ulaşabiliriz? GÖrelim;

print("Çalışılan Bölüm: ",calisanlar[0].bolum)
print("Çalılanların Maaşlar: ",calisanlar[0].maas)

# Çıktılarımız :
# Çalışılan Bölüm:  yazilim
# Çalılanların Maaşlar:  30000


#! Nesne Nitelikleri 
# Nesne niteliği nasıl oluşur öncelikle onu görelim;

class alperaybakindustries:
    def __init__(self):
        self.ad  = " "
        self.soyad  = " "
        self.araba = " "
        self.cinsiyet  = " "

# Daha önce görmediğimiz bir veriyle karşılaştık veya kod.
# __init__ fonksiyonu özel bir fonksiyondur.
# Özelliği ise örnekleme aldığı an çalışır.
# Self anahtar sözcüğümüz de var tabiki.
# Self, __init__() fonksiyonu da içinde olmak üzere nesneye ait fonksiyonların olmazsa olmazıdır.
# İsterseniz bu kadar açıklamanın üzerine ne olduğunu görelim;

class alperaybakindustries:
    def __init__(self):
        self.ad  = "Alper"
        self.soyad  = "Aybak"
        self.araba = "Audi R8"
        self.cinsiyet  = "Erkek"


# Şu şekilde de tanımlayabiliriz;

class alperaybakindustries:
    def __init__(self,ad="Alper",soyad="Aybak",araba="Audi R8",cinsiyet="Erkek"):
        self.ad  = ad
        self.soyad  = soyad
        self.araba = araba
        self.cinsiyet  = cinsiyet


# Şimdi ise sınıfımızla 11 yeni örnek oluşturalım;

aai = list()

for i in range(11):
    ad = input("İsim: ")
    soyad = input("Soyisim: ")
    araba = input("Araba: ")
    cinsiyet = input("Cinsiyet: ")

    aai.append(alperaybakindustries(ad,soyad,araba,cinsiyet)) 


# Kodu çalıştırıp 11 istediğiniz şekilde yazabilirsiniz
# Veya sadece ad yazmak istiyorsanız şöyle yapabiliriz;

for i in aai:
    print(i.ad)

# soyad,araba,cinsiyet de aynı şekilde yazılabilir.







#! Şimdi Kütüphane Otomasyonumuza bir kez daha bakalım umarım daha net anlaşılacaktır;


class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi, yayinevi, basim_yili, id_no):
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.basim_yili = basim_yili
        self.yayinevi = yayinevi
        self.id_no = id_no

    def __str__(self):
        return "Kitap: {} -- Yazar: {} -- Sayfa Sayısı: {} -- Basım Yılı: {} -- Yayınevi: {} -- ID: {}".format(self.ad, self.yazar, self.sayfa_sayisi, self.basim_yili, self.yayinevi, self.id_no)


class Uye:
    def __init__(self, isim, soyisim, dogum_tarihi):
        self.ad = isim
        self.soyad = soyisim
        self.dogum_tarihi = dogum_tarihi
        self.alinan_kitaplar = list()
        self.son_alinan_kitap = None # Kitap alındığında değişecek.
        self.favoriler = list()
        self.alinan_etkin_kiap_sayisi = 0 # En fazla 3 kitaba aynı anda sahip olunabilir
        self.etkin_kitaplar = list()

    def favori_ekle(self, kitap):
        if kitap not in self.favoriler:
            self.favoriler.append(kitap)

        else:
            print("Bu kitap zaten favorilerde ekli!")


    def favori_sil(self, kitap):
        if kitap in self.favoriler:
            self.favoriler.remove(kitap)

        else:
            print("Bu kitap favorilerinizde bulunmuyor!")


    def kitap_al(self, kitap):
        if self.alinan_etkin_kiap_sayisi < 3:
            if kitap not in self.alinan_kitaplar:
                self.alinan_kitaplar.append(kitap)
            
            self.etkin_kitaplar.append(kitap)
            self.alinan_etkin_kiap_sayisi += 1
            self.son_alinan_kitap = kitap

        else:
            print("Daha fazla kitap alamazsınız!")

    def kitap_teslim_et(self, kitap):
        if kitap in self.etkin_kitaplar:
            self.etkin_kitaplar.remove(kitap)
            self.alinan_etkin_kiap_sayisi -= 1


        else:
            print("Kitap bu üyede mevcut değil!")

    def __str__(self):
        return "Ad: {} -- Soyad: {} -- Son Alınan Kitap: {}".format(self.ad, self.soyad, self.son_alinan_kitap)


class Kutuphane:
    def __init__(self):
        self.kitaplar = list()
        self.uyeler = list()
        self.yazarlar = set()



    def uye_ekle(self, uye):
        if uye not in self.uyeler:
            self.uyeler.append(uye)

        else:
            print("Üye zaten mevcut!")
    

    def uye_sil(self, uye):
        if uye in self.uyeler:
            self.uyeler.remove(uye)
        
        else:
            print("Bu üyenin zaten kaydı yok!")


    def yazar_kume_yenile(self):
        self.yazarlar = set()
        
        for i in self.kitaplar:
            self.yazarlar.add(i.yazar)


    def kitap_ekle(self, kitap):
        if kitap not in self.kitaplar:
            self.kitaplar.append(kitap)
            self.yazar_kume_yenile()

        else:
            print("Bu kitap zaten kütüphanede!")


    def kitap_cikar(self, kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
            self.yazar_kume_yenile()

        else:
            print("Kütüphanede mevcut olmayan bir kitabı çıkarmaya çalışıyorsunuz!")


    def yazarlar_bilgi(self):
        return self.yazarlar





# Evet arkadaşlar bu dersimizin de sonuna gelmiş bulunuyoruz.
# NTP ile ilgili 2 örnek kod vereceğim pekişeceğine eminim.
# Görüşmek üzere....