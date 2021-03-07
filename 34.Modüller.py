# AAI Company - Python

# Modüller

# Modül kısaca aktif etmek diyebiliriz. 
# Örneğin random sayı seçeceksek random modülüne ihtiyaç duyarız.


#! Modüllerin Kullanılması:
# Modülleri kullanmanın iki yolu vardır.
# Birisi Python'ın kendi modülleri, hazırda bulunan  bir de kendi oluşturduğumuz modüller vardır.
# Python tarafından yazılmış modül kullanacaksak o modülün hangi dizinde olduğunu bilmemize gerek yok.
# Fakat kendimiz modül yazıyorsak hangi dizinde olduğunu bilmemiz gerekiyor.


#! Hazır Modül Kullanımı:
# Modül aktif etmek için "import" komutunu kullanırız.
# Örnek verdiğimiz gibi random modülüne bir bakalım isterseniz nasıl aktif edebiliriz;

import random

sayi = random.randint(0,111)
print(sayi)

# Kodumuzu her çalıştırdığımızda 0'dan 111'e kadar rastgele sayı çıktısı alacağız.

# Başka bir örneğe bakalım;

from random import radnit

na = radnit(0,111)
print(na)

# radnit fonksiyonunu yukarıdaki gibi import edersek, yalnızca radnit fonksiyonunu kullanabiliriz anlamına gelimektedir.


# Devam edelim örnek üzerinde açıklamaya;

from random import *

# Yukarıdaki gibi sonuna yıldız eklersek radnitden başka fonksiyonları da kullanabileceğimiz anlamına gelir.


# Yukarıda yaptığımızın dışında import etmek için isim verebiliriz yani özelleştirebiliriz;

from random import randint as alperaybak

sayi = alperaybak(1,111)
print(sayi)



#! Kendimize Ait Modülün Kullanılması:
# Eğer kullanacağımız modül pythonda bulunmuyorsa, modül yazmamız gerekebilir.
# Veya herhangi bir geliştiricinin kodlarını biliyoruz uygulamak istiyoruz aynı şekilde modül oluşturabiliriz.

# İlk olarak pythonda hazır bulunan sys modülünü import edelim;
# Ve bu dizinler neymiş path değişkeni ile görelim; (karışık gelmiş olabilir şimdi oturacaktır :) )

import sys

for i in sys.path:
    print(i)

# Çıktımız =>
# C:\Users\ALPER\PycharmProjects\pythonProject40
# C:\Users\ALPER\PycharmProjects\pythonProject40
# C:\Users\ALPER\AppData\Local\Programs\Python\Python38-32\python38.zip
# C:\Users\ALPER\AppData\Local\Programs\Python\Python38-32\DLLs
# C:\Users\ALPER\AppData\Local\Programs\Python\Python38-32\lib
# C:\Users\ALPER\AppData\Local\Programs\Python\Python38-32
# C:\Users\ALPER\PycharmProjects\pythonProject40\venv
# C:\Users\ALPER\PycharmProjects\pythonProject40\venv\lib\site-packages

#! Yukarıdaki çıktı sizde farklı olabilir. Sebebi python sürümü ile alakalı. Ben şuanlık 3.8.5 sürümünü kullanıyorum.

# Örneğin masaüstünde yer alan yazmış olduğumuz modülü aktif etmek için;

import sys
adres = '/home/ALPER/Masaüstü'
sys.path.append(adres)

import alperaybak


# Eğer import edilmek istenen modül, proje dosyası ile aynı dizinde yer alıyorsa naparız?

import sys
adres = '/home/ALPER/Belgeler/src'
# İmport edeceğimiz modüle ulaşmak için de;
import src.AAICompany

#! Modül Kurulması:
# Bilgisayarımızda olmayan fakat normalde var olan bir modül kurmak istersek ne yapmalıyız?
# Eğer işletim sisteminiz Windows ise => arama kısmına "Komut Satırı (CMD)" yazarak aratabilirisniz.Kısayol olarak ise Başlat + R tuşuna basıp çıkan kısıma "cmd" yazmanız yeterli.
# GNU/Linux veya Macintosh kullanıyorsanız da terminali açmanız yeterli olacaktır. Kısayol olarak ise => Ctrl + Alt + T

# Kod penceremizde şu komutları uyguluyoruz;
# pip install <modül adı>  (Windows)
# sudo pip install <modul adı > (GNU/Linux or Mac)


# İsterseniz örnek olarak çok kullanılan "Python Selenium" yükleyelim;

#! Windows ==> pip install selenium
#! GNU/Linux or Max => sudo pip install selenium

# Eğer mac ve linuxta hata alınırsa komutun sonuna --user (örnek; --alper) ekleyebilirsiniz. Fakat çoğu sistemde sorun çıkmayacaktır.



#! Başlıca Modüller:
# Aslında herkesin başlıca modülleri farklıdır fakat bu başlıkla demek istediğim, sıklıkla kullanılan modüller.
# İsterseniz görelim en sık nelerle karşılaşırız.

#! Random MOdülü:
# Az  önce kullandığımız modüldü az çok biliyoruz aslında. Daha doğrusu temelini kavradık.
# Random modülünde hangi fonksiyonlar varmış onu görelim öncelikle;

import random

for i in dir(random):
    if ('_' != i[0]):
        print(i)


# Çıktılarımız =>
# BPF
# LOG4
# NV_MAGICCONST
# RECIP_BPF
# Random
# SG_MAGICCONST
# SystemRandom
# TWOPI
# betavariate
# choice
# choices
# expovariate
# gammavariate
# gauss
# getrandbits
# getstate
# lognormvariate
# normalvariate
# paretovariate
# randint
# random
# randrange
# sample
# seed
# setstate
# shuffle
# triangular
# uniform
# vonmisesvariate
# weibullvariate


# Baktığımız zaman baya bir fonksiyonu var. Ama işimize yarayacak olanları görelim;

#! random() Kullanımı
# 0 ile 1 arasında rastgele sayı verir ( 0 <= n < 1 )
# Görelim;

import random

sayi = random.random()
print(sayi)

# Çıktı => 0.6791830579022602
# Çıktı elbette sizde farklı olabilir random atanmasından kaynaklı olarak
# Ayrıca unutmayalım sayı cinsimiz float :)


#! randint() Kullanımı
# Kullandığımı bir fonksiyondu
# İstediğiniz açıklıkta verebilirsiniz sayıyı ( min. <= n <= max.)
# Görelim tekrardan;

import random 

na = random.randint(1,111)
print(na)

# Çıktı => 49 
# Yine farklılık olabileceğini belirtelim.


#! randrange() Kullanımı
# for dingüsünen range() parametresini hatırlayalım
# Aslında aynı görevi yapıyorlar min. dahil fakat max. dahil değil ( mi.n <= n < max.)
# Görelim;

import random

aai = random.randrange(1,111)
print(aai)

# Çıktı => 88
# Farklılık göstereceğini artık anlamışızdır diye düşünüyorum ve bundan sonra bu hatırlatmayı geçiyorum :)


#! sample() Kullanımı 
# sample() fonksiyonu için bir liste gerekiyor.
# Bu liste içindeki herhangi bir ögeyi veya ögeleri rastgele geri döndürme işlemini yapıyır.
# Kaç adet değer döndüreceğini ikinci paramtresine yazıyoruz.
# Görelim;

import random

liste = [i for i in range (1,200) if i % 3 == 0]

na = random.sample(liste,5)
print(na)

# Çıktım ==> [174, 3, 30, 114, 87]

#! shuffle() Kullanımı 
# Liste metodlarında sort() fonksiyonumuz vardı hatırlıyor muyuz?
# Hatırladığınıza eminim fakat yine de hatırlatayım sort() ==> Listeleri belirli düzene sokar
# shuffle() ise listemizi rastgele sıralar. Görelim;

import random 

company = ["Alper","Hüseyin","Tony","Aybak","Stark","Bağcı"]
company.sort()
print("List V1 : ",company)
random.shuffle(company)
print("List V2 : ",company)

# Çıktılar :
# List V1 :  ['Alper', 'Aybak', 'Bağcı', 'Hüseyin', 'Stark', 'Tony']
# List V2 :  ['Aybak', 'Hüseyin', 'Tony', 'Alper', 'Bağcı', 'Stark']


#! choice() Kullanımı
# choice() fonksiyonu herhangi bir listeden sadece 1 değer döndürür.
# Hatırlarsanız sample() fonksiyonu geriye liste döndürürken choice() liste içinden 1 eleman döndürecek.
# Görelim;

import random

liste = [i for i in range (11,111,7) if i % 5 == 0]
print("Sayı: {}".format(random.choice(liste)))

# Çıktı => Sayı: 60








#! TIME MODÜLÜ
# Burada ise tahmin edebildiğiniz gibi zaman ile ilgili işlemleri yapabiliyoruz.

#! gmtime() Kullanımı:
# Zaman modülü ile işlem yapmak için öncelikle gmtime() fonksiyonu ile başlangıç zamanımızı bilmemiz gerekir.
# İstersniz zamanımızı görelim;

import time
time.gmtime(0)

# Bu kodu girdiğimiz zaman 1970'i başlangıç alacaktır. Ve değerler genelde 0 ile 3 arası değişir :)
# Aslında biz 0 girerek 0.saniyenin tarihini almış olduk
# Peki ya  0.saniyenin tarihini almayalım şöyle bir kod yazalım;

import time 
print(time.gmtime(11062002))

# Çıktımız => time.struct_time(tm_year=1970, tm_mon=5, tm_mday=9, tm_hour=0, tm_min=46, tm_sec=42, tm_wday=5, tm_yday=129, tm_isdst=0)
# Çıktmızı yorumlayalım isterseniz baştan sona 
#! yıl = 1970, 5.ay, 9.gün, saat 0, dakika 46, saniye 42, haftanın 5.günü, sene başından beri geçen gün sayısı ise 129



#! time() Kullanımı 
# gmtime() kısmında kullandığımız kavram epoch adını alıyor. Yani başlangıcı 1970 kabul ediyordu.
# time() fonksiyonu zamanından başlangıcından bu yana geçen saniyeyi verir
# Görelim;

import time
print(time.time())

# Çıktı => 1611963668.0202298
# Bu kodlar size ulaştığında zaman farkı olabilir tabiki :)
# Bu saniyeyi gmtime()'a çevirirsek şuanı bulabiliriz.

# Bir de şuanki zamanı bastıralım çıktı olarak;

import time
now = time.time()
print(time.gmtime(now))

# Çıktı => time.struct_time(tm_year=2021, tm_mon=1, tm_mday=29, tm_hour=23, tm_min=41, tm_sec=8, tm_wday=4, tm_yday=29, tm_isdst=0)



#! localtime() Kullanımı
# Sistmdeki yerel saat bilgisini verir 
# Görelim;

import time
print(time.localtime())

# Çıktı => time.struct_time(tm_year=2021, tm_mon=1, tm_mday=29, tm_hour=23, tm_min=42, tm_sec=8, tm_wday=4, tm_yday=29, tm_isdst=0)


#! asctime() Kullanımı 
# Zamanı bize karakter dizisi şeklinde verir. (string)
# İsterseniz daha net görelim;

import time 
print(time.asctime())

# Çıktımız => Sat Jan 30 02:43:06 2021
#! Çıktı gün ve ay isimlerinin İngilizce kısaltmasıdır




#! sleep() Kullanımı 
# Aslında gün içinde karşımıza çokça çıkabilen fonksiyondur.
# Örneğin telefonumuzda arka arkaya yanlış şifre girdiğimizde 30 saniye bekleyiniz yazısı çıkar
# Veya bir web sayfasına dosya upload etmek için belirli süre olabiliyor (tabiki dosya boyutuna göre değişir). Aslında o dosya boyutunun yüklenirken ne kadar saniye veya dakika geçmesinin ayarlanmasından kaynaklanır.
# İsterseniz 5 saniye beklememiz gereken daha sonra işlem yapabileceğimiz bir kod yazalım;

import time 

for i in range(5,0,-1):
    print(i)
    time.sleep(1)

print("İşlem Bitti\nfrom Alper Aybak")

# Çıktımız =>
# 5
# 4
# 3
# 2
# 1
# İşlem Bitti
# from Alper Aybak

# Kendiniz run (çalıştır) yaptığınız zaman daha iyi göreceksiniz :)






#! os Modülü
# os modülü dediğimiz şey aslında işletim sisteminin kısaltması os'tan geliyor (operating system).
# İşletim sistemi fonksiyonları bulundurur.
# OS modülü ile neler yapabiliriz?
# Hangi dizinde olduğumuzu öğrenme, dizin içindeki ögeleri listeleme, dizin silme, dosyalar üzerindeki yetkilere ulaşma...vb.
# İsterseniz kullandığımız işletim sistemini öğrenmek için aşağıdaki kodu yazalım (elbette biliyorsunuzdur eminim ama aklımızda bulunsun)
# GNU/Linux => "posix" Windows => "nt" yazacaktır;

import os
print(os.name)

# Çıktı => nt (sizlerde farklılık gösterebilir)


#! getcwd() Kullanımı 
# Python dosyasını çalıştırırken Termina(Uçbirim or Komut Listesi(cmd)) hangi dizinde iş görüyorsa o dizinin adresinin döndürür
# Görelim;

import os
print(os.getcwd())

# Çıktı ==> C:\Users\ALPER\PycharmProjects\pythonProject40
# Bu derslerdeki kodları PyCharm üzerinden çalıştırıp burada yazdığım için terminalimiz pycharm gözüküyor.


#! chdir() Kullanımı 
# chdir() fonksiyonu ile istediğiniz dizine hareket edebilirsiniz.

import os
print("Birinci Durum: ", os.getcwd())
os.chdir("/Users/ALPER")
print("İkinci Durum: ", os.getcwd())

# Çıktı ==> 
# Birinci Durum:  C:\Users\ALPER\PycharmProjects\pythonProject40
# İkinci Durum:  C:\Users\ALPER
# Ben orada bırakmak için bir şey yazmadım fakat ALPER'den sonra / bırakıp gitmek istediğiniz yere gidebilirsainiz. (örneğin /Users/ALPER/Downloads)
# Bir de öyle görelim isterseniz;

import os
print("Birinci Durum: ", os.getcwd())
os.chdir("/Users/ALPER/Downloads")
print("İkinci Durum: ", os.getcwd())

# Çıktı ==> 
# Birinci Durum:  C:\Users\ALPER\PycharmProjects\pythonProject40
# İkinci Durum:  C:\Users\ALPER\Downloads


#! listdir() Kullanımı 
# Herhangi bir dizinin içeriğini görmek için kullandığımız fonksiyondur.
# Dilerseniz görelim;

import os
dizindekiler = os.listdir(".")
print(dizindekiler)

# Çıktı ==> ['.idea', 'alperaybak.txt', 'alperaybakindustries.py', 'test.py', 'venv'] 
# Sizdeki dizinler farklı olabilir.
# Bu proje için açmış olduğum dosyaları görüyorsunuz :)


#! SEP Niteliği Nedir?
# OS modülünde yalnızca fonksiyonlar değil nitelikler de yer alıyor.
# İşletim sistemimizin dizin ayıracını saklayan niteliktir.
# Örneğin; Windows sisteminde ==> \\ iken GNU/linux ve MacOS sisteminde ==> / şeklindedir.
# Görelim;

import os
ayrac = os.sep
print(ayrac)

# Çıktı ==> \
# Şuanda Windows işletim sisteminde olduğum için \ çıktısını aldım.



#! mkdir() Kullanımı 
# Aslında Linux kullanıcılarının terminalden aşina olduğu komuttur. Yani GNU/Linux'taki görevi ile aynıdır.
# Bir dizin oluşturmamızı sağlıyor.
# Peki ya farkı ne? Linux sisteminde birden çok dizin oluştururken mkdir() fonksiyonu tek dizin oluşturuyor
# Görelim nasıl kullacağımızı;

import os
os.mkdir("AAI Company - Python")

# Bunun oluşumunu listdir() ile gösterelim dilerseniz;

import os
dizindekiler = os.listdir(".")
print(dizindekiler)

# Çıktı ==> ['.idea', 'AAI Company - Python', 'alperaybak.txt', 'alperaybakindustries.py', 'test.py', 'venv'] 
# Biraz yukarı kaydırıp incelerseniz çıktımızdaki farkı göreceksiniz (AAI Company - Python)


#! makedirs() Kullanımı 
# mkdir() fonksiyonununda söylemiştik tek bir dizin oluşturabiliriz diye.
# Birden çok dizin için ise ==> makedirs() fonksiyonunu kullanacağız
# Görelim;

import os
os.makedirs("alperaybakindustries.com/aai folder/Company Folder")

# Burada alt alta dizinler oluşturdum siz de göreceksiniz (Oluşturduğunuz dizinin içine giriş yaparak görebilirisniz)


#! renmae() Kullanımı 
# Dosyaların adını değiştirebildiğimiz komuttur.
# Bir nevi herhangi bir dosyaya sağ tıkladığımız zaman yeniden adlandır(ingilizce kullanıyorsanız rename) komutu.

import os 
os.mkdir("Alper Aybak")
os.rename("Alper Aybak", "Yeni İsim")



#! remove() Kullanımı
# Python'da dosya silmek için rename() fonksiyonunu kullanıyoruz.
# Az önce ismi değişen dosyayı silelim dilerseniz;

import os 
os.remove("Yeni İsim")



#! rmdir() Kullanımı 
# Linux kullanıcılarının alışık olduğu bir diğer komutlardan aslında 
# remove() fonksiyonu ile dosya siliyorduk fakat dizin silmek istersek (dosya içindeki bir kısım) ne yapıyoruz? Görelim;

import os 
os.rmdir("Ana Dosya Adı/Seçmek istediğimiz dizin/varsa bir diğer dizin/silinecek dizin ismine kadar")

#! NOT = Eğer 5.bir dizinimiz varsa removedirs() fonksiyonu devreye girer. Fakat bu dizine giden yolların boş olması gerekir yoksa hata alırız.
# Kullanımı Görelim;

import os 
os.removedirs("dizin1/dizin2/dizin3/dizin4/dizin5") 



#! stat() Kullanımı 
# stat() fonksiyonu bize dosyalar için detaylı bilgiler vermektedir.
# Detaylı bilgi edineceğimiz bir nesne döndürür.
# Örnek olarak daha önce oluşturmuş olduğumuz alperaybak.txt dosyasını inceleyelim;

import os
dosya = os.stat("alperaybaK.txt")

print("Dosyanın Boyutu: ", dosya.st_size,"Byte")
print("Dosyanın Son Erişilme Tarihi: ",dosya.st_atime)
print("Dosyanın Oluşturulma Tarihi: ",dosya.st_ctime)
print("Dosyanın Son Değiştirilme Tarihi: ",dosya.st_mtime)

# Çıktı ==>
# Dosyanın Boyutu:  29 Byte
# Dosyanın Son Erişilme Tarihi:  1611869809.4462104
# Dosyanın Oluşturulma Tarihi:  1611869734.118423
# Dosyanın Son Değiştirilme Tarihi:  1611869808.8450253
# Time modülleri ile yukarıdaki birimleri çevirebiliriz :)



#! system() Kullanımı
# Bazen sistemin komut satırına bir şeyler yazmak gerekebilir.
# Bunu Python içerisinde yapmamızı sağlayan fonksiyon system()'dır.
# Adından da belli olduğu üzere sistem komutlarını çalıştırır.
# Windows, GNU/Linux ve MacOS işetim sistemine göre farklılık gösterebilir.
# Ortak bir kod yazalım isterseniz;

import os 

if os.name == "posix":
    os.system("clear")

elif os.name == "nt":
    os.system("cls")

else:
    print("Bilinmeyen veya Python'ın Tanımadığı Bir Sistem")


# Bu kod ile komut satırını temizleyebiliriz.


#! os.path.expanduser() Kullanımı
# Aslında çok işe yarayan bir fonksiyondur 
# Bizim vereceğimiz komuta göre dizini gösterene veyahut dizin yolun yolunu gösteren komuttur.
# Herhangi bir dizine gideceksiniz bilgisayar başka birisinin kullanıcı adını bilmiyoruz diyelim işte o zaman bu kodu kullanacağız
# Dilerseniz görelim;

import os

home = os.path.expanduser("~")
print(home)

# Çıktı ==> C:\Users\ALPER
# Verilen path'e göre bir sonuç döndü 
#! Not => "~" karakteri ev dizinini temsil eder.






# Çok uzun bir konu olduğunun farkındayım ama çok fazla kullanılan fonksiyonlardır. Daha doğrusu modüllerin kullanımı yaygındır.
# Umarım anlaşılmıştır. Elimden geldiğince açık olmaya çalıştım.
# Herhangi bir sorun olursa iletişime geçebilirsiniz.
# Diğer dersimizde görüşmek üzere...

