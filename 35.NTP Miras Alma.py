# AAI Company - Python 

#! Nesne Tabanlı Programlama - Miras Alma


# Arkadaşlar aslında biraz bildiğimiz bir bölüm hatırlarsanız NTP'da self ve daha bir çok birimle kullanılan __init__ fonksiyonunu görmüştük
# Evet ama bunun mitas almayla ne alakası var diyebilirsiniz.
# Aslında biz miras almada bu NTP'yi geliştireceğiz.
# Oluşturdğumuz sınıfı farklı bir sınıf oluşturduğumuzda geri çağırabilmeyi verileri tekrardan yazmadan yeni sınıfa aktarabileceğiz.
# Aslında miras alma terimi de buradan geliyor.
# Bu bölümü örnekle anlatacağım bir iki öğreneceğimiz terimler/fonksiyonlar olacak onları da örnek içerisinde açıklayacağım.
# Fazla uzatmadan başlayalım isterseniz;



class AAI_Company():
    def __init__(self, ad, soyad, meslek, bildigi_yabanci_diller, bildigi_yazilim_dilleri):
        self.ad = ad
        self.soyad = soyad
        self.meslek = meslek
        self.bildigi_yabanci_diller = bildigi_yabanci_diller
        self.bildigi_yazilim_dilleri = bildigi_yazilim_dilleri


# Buralar zaten bildiğimiz kısımlar. Fonksiyonlarımızı çağırabilmek için self  ile eşitledik.


    def BilgileriGoster(self):
        print("AAI Company Çalışan Bilgileri Gösteriliyor")
        print("Ad:", self.ad, "Soyad:", self.soyad, "Meslek:", self.meslek, "Bilinen Yabancı Diller:",
              self.bildigi_yabanci_diller, "Bildiği Yazılım Dilleri:", self.bildigi_yazilim_dilleri)

    def YazilimDiliEkle(self, yeni_yazilim_bilgisi):
        print("Yeni Sertifika Ekleniyor...")
        self.bildigi_yazilim_dilleri += yeni_yazilim_bilgisi (# Yeni yazılım bilgisi ekliyoruz azaltmak isterseniz de -= şeklinde olabilir)

    def YeniYabanciDil(self, yeni_dil_bilgisi):
        print("Yeni Yabancı Dil Ekleniyor...")
        self.bildigi_yabanci_diller += yeni_dil_bilgisi

    def MeslekDegistir(self, yeni_meslek):
        print("Çalıştığı Bölüm Değiştiriliyor...")
        self.meslek = yeni_meslek



calisan = AAI_Company("Alper","Aybak","Elektrik-Elektronik Mühendisi","İngilizce ve Almanca","Python,C ve C++,Php,Java,Web Development,Kotlin") # Değerleri "calisan" verisine atadık.
calisan.BilgileriGoster()
calisan.YazilimDiliEkle(",Arduino Kodlama") # Virgül koyma sebebim yapışık bir şekilde eklenmesin diye 
calisan.BilgileriGoster()

# Bu kısım anlaşıldı diye düşünüyorum daha önce de yaptığımız uygulamalar. 


class YoneticiSinifi(AAI_Company): # Miras alma işlemi burada başlıyor miras alacağımız sınıfın ismini yeni sınıfımızın parantez içine yazıyoruz.
    def __init__(self, ad, soyad, meslek, bildigi_yabanci_diller, bildigi_yazilim_dilleri, maas,
                 ilgilendigi_kisi_sayisi):
        print("Yönetici Sınıfının Yapıcı Fonksiyonu")
        super().__init__(ad, soyad, meslek, bildigi_yabanci_diller, bildigi_yazilim_dilleri) 
        # super() fonksiyonu daha önce gördüğümüz bir fonksiyon değil. Yukarıda atadığımız verileri tekrardan yazmayalım kolay çağırabilelim diye kullanılan fonksiyondur.
        self.ilgilendigi_kisi_sayisi = ilgilendigi_kisi_sayisi 
        self.maas = maas
        # Bu sınıfa özel olarak da maas ve ilgilenilen kişi sayısını ekledim (diğer sınıftan farkımız bu)

    def BilgileriGoster(self):
        print("Yönetici Sınıfının Bilgileri GÖsteriliyor...")
        print("Ad:", self.ad, "Soyad:", self.soyad, "Meslek:", self.meslek, "Bilinen Yabancı Diller:",
              self.bildigi_yabanci_diller, "Bildiği Yazılım Dilleri:", self.bildigi_yazilim_dilleri, "Maaşı:",
              self.maas, "İlgilendiği Kişi Sayısı:", self.ilgilendigi_kisi_sayisi)

        # Bilgileri görmek için kullanacğımız def fonksiyonumuz.

    def MaasaZamYap(self, zam_miktari):
        print("Maaşa Zam Yapıldı")
        self.maas += zam_miktari

    def KisiSayisiArtir(self, artir):
        print("İlgilendiği Kişi Sayısı Artırılıyor...")
        self.ilgilendigi_kisi_sayisi += artir


yonetici = YoneticiSinifi("Alper", "Aybak", "Elektrik-Elektronik Mühendisi", "İngilizce ve Almanca","Python,C ve C++,Php,Java,Web Development,Kotlin", 100000, 100)
yonetici.BilgileriGoster()
yonetici.KisiSayisiArtir(100) #Kişi sayısının üzerine 100 kişi daha ekleniyor
yonetici.BilgileriGoster()

# Atadğımız değerden sonra nokta koyarak istediğimiz def fonksiyonunu çağırabiliyoruz ve değerleri değiştirebiliyoruz.
# Elimden geldiğince açıklamaya çalıştım umarım anlaşılmıştır ve bir de calisan ve yonetici verilerimizin çıktısına bakalım isterseniz;

# #! Çıktımız :
# AAI Company Çalışan Bilgileri Gösteriliyor
# Ad: Alper Soyad: Aybak Meslek: Elektrik-Elektronik Mühendisi Bilinen Yabancı Diller: İngilizce ve Almanca Bildiği Yazılım Dilleri: Python,C ve C++,Php,Java,Web Development,Kotlin
# Yeni Sertifika Ekleniyor...
# AAI Company Çalışan Bilgileri Gösteriliyor
# Ad: Alper Soyad: Aybak Meslek: Elektrik-Elektronik Mühendisi Bilinen Yabancı Diller: İngilizce ve Almanca Bildiği Yazılım Dilleri: Python,C ve C++,Php,Java,Web Development,Kotlin,Arduino Kodlama
# Yönetici Sınıfının Yapıcı Fonksiyonu
# Yönetici Sınıfının Bilgileri GÖsteriliyor...
# Ad: Alper Soyad: Aybak Meslek: Elektrik-Elektronik Mühendisi Bilinen Yabancı Diller: İngilizce ve Almanca Bildiği Yazılım Dilleri: Python,C ve C++,Php,Java,Web Development,Kotlin Maaşı: 100000 İlgilendiği Kişi Sayısı: 100


# Daha da güzel görünsün isterseniziçin print kısmında alt alta gelsin diye \n parametremizi kullanabilirsiniz.




# Konumuz bu şekilde arkadaşlar gerçekten önemli ve kolaylık sağlayan bir konu.
# Sıkıntı olursa ulaşabilirsiniz.
# Örnek ile beraber anlatmaya çalıştım unmarım yararlı olmuştur.
# Diğer dersimizde görüşmek üzere....