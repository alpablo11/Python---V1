# AAI Company - Python

# Karakter Dizilerini Biçimlendirmek (format() Metodu İle)

# .format() Metodu 
# Bu metod aslında işlerimizi kolaylaştırmak için vardır.
# Yani bir nevi kısayoldur.
# İsterseniz örnekle açıklayalım;

ad = "Aper"
soyad = "Aybak"
print("Benim adım {}, soyadım {}'dır.".format(ad,soyad))

# Kullanıcıdan veri de alabiliriz görelim;

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = input("Yaşınız: ")
meslek = input("Mesleğiniz: ")

print("Ad: {}\nSoyad: {}\nYaş: {} \nMeslek: {}".format(ad,soyad,yas,meslek))


# İşlemleri de kolayca yapabiliriz şu örneğimiz inceleyelim;

a = 11
n = 21
print("{x} + {y} = {sonuc}".format(x=a,y=n, sonuc = a+n))

# Yukarıdaki örneği başka yolla da yapabiliriz;

a = 11
n = 21
print("{} + {} = {}".format(a,n,a+n))

#! format() metodu ile belli bir alanda sağa veya sola yaslayarak biçimlendirmeyi görelim;

aybak = "|{:21}|".format("AAI Company")
print(aybak)


#! Sıra Belirleme:

print("{birinci} {ikinci}".format(birinci= "Alper", ikinci= "Aybak"))

# Değişken yerine direk sıra numarası da verebiliriz, görelim;

print("{0} {1} {2}".format("Alper","Aybak","Industries"))


#! Sayı Zorunluluğu: {:d}

# Eğer sadece sayı dizisinden oluşmasını istersek bunu belirtebiliriz.
# Dilerseniz örneğe bakalım;

print("{:d} + {:d} = {:d}".format(11,21,32))

# Peki sayı girmezsek nolacak görelim;

print("{:d} + {:d} = {:d}".format(a,n,na))

# # Çıktımız: 

# Traceback (most recent call last):
#     print("{:d} + {:d} = {:d}".format(a,n,na))
# NameError: name 'a' is not defined

# Gördüğümüz gibi hata verdi. Programımız hata vermesin diye karakter dizisi zorunluluğu metodunu kullanmamız gerekiyor.

#! Karakter Dizisi Zorunluluğu: {:s}

# Sadece stinglerden oluşmalıdır.
# Örneğimiz bakalım;

print("{:s} + {:s} = {:s}".format(n,a,na))

# Şimdi de sayı ile deneyelim;

print("{:s} + {:s} = {:s}".format(11,21,32))

#  Çıktımız:
#     print("{:s} + {:s} = {:s}".format(11,21,32))
# ValueError: Unknown format code 's' for object of type 'int'

#! Kısaca stirng için => {:s}, sayılar için => {:d}


#! ASCII Tablosundaki Karşılığı:
# Her bir karakter ASCII tablosunda bir değere karşılık gelmektedir.
# Örnekle gösterelim;

print("65 Sayısının ASCII Tablosundaki Karşılığı: {:c}".format(65))

# Çıktımız ==> 65 Sayısının ASCII Tablosundaki Karşılığı: A
# Gördüğümüz gibi sayıların ASCII tablosunda bir değeri var.
# Fakat harf girersek hata alırız, Görelim;

print("A Harfinin ASCII Tablosundaki Karşılığı: {:c}".format(A))

# Çıktı :
# Traceback (most recent call last):
#     print("A Sayısının ASCII Tablosundaki Karşılığı: {:c}".format(A))
# NameError: name 'A' is not defined

# ASCII tablosunda karşılık bulamadığınız sayılar olabilir. Bazen bu sürümden kaynaklanır, bazen de uygulamanın o karakteri desteklememesi.
# Çok detaylı öğrenmek için linki bırkayım;
#  https://tr.wikipedia.org/wiki/ASCII



#! İkilik Sistemde Karşılığı:
# Herhangi bir sayının ikilik sistemde karşılığını öğrenmek için de format() Metodu kullanılıyor.
# İsterseniz örnekle bakalım;

print("11 sasyısının ikilik sistemdeki karşılığı: {:b}".format(11))

# Çıktımız ==> 11 sasyısının ikilik sistemdeki karşılığı: 1011

# 11 sayımızın ikilik sistemdeki karşılığını öğrendik isterseniz başka bir yolla daha yapalım.
# Hem format() hem de bin() fonksiyonu ile atayalım;

n = "{:b}".format(11)
a = bin(11)

print(n)
print(a)

# Çıktımız:
# 1011
# 0b1011
# a değişkeninde 0b ibaresini görüyoruz bu ibare karakter dizisinin ikilik sistem barındırdığını gösteriyor.



#! Onaltılık Sistemde Karşılığı:
# İkilik yöntemle benzerdir.
# Farkı {:b} yerine {:x} yazıyoruz.
# İsterseniz örnek verelim;

n = "{:x}".format(111)
print(n)

# Çıktımız ==> 6f

# Yukarıda bahsettiğimiz bir diğer yöbntem ise hex() metodu ile bulunuyor. Görelim;

print(hex(111))

# Çıktımız ==> 0x6f
# 0x ile başlarsa karakterimiz hexadecimal yani onaltılık sayı barındırıyor.


#! Sekizlik Sistemde Karşılığı:
# Mantığı yukarıdakiler gibi burada ise; {:o} metodunu kullanıyoruz.
# İsterseniz görelim;

print("{:o}".format(11))
# Çıktımız ==> 13

# Bir diğer yöntem ise;

print(oct(11))
# Çıktımız ==> 0o13

# 0o ile başlıyorsa karakterimiz bunun sekizlik sisteme ait olduğunu söyleyebiliriz.


#! Sayıları Basamaklarına Ayırma:
# Sayıların okunmasını kolaylaştırmak için bir yöntemdir.
# {:,} ile uzun sayıları kolayca okuyabiliriz
# İsterseniz örnek olarak görelim;

print("{:,}".format(110602122002))
# Çıktımız ==> 110,602,122,002



# Evet arkadaşlar bu dersimizinde sonuna gelmiş bulunuyoruz. Herhangi bir sorunuz varsa iletişime geçebilirsiniz.
# Bu dersi iyice sindirdikten sonra bilgilendirme adlı .py dosyamızı okuyalım. Görüşmek üzere....