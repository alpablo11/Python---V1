# AAI Company - Python

# Temel Dosya İşlemleri 

# Python'da hangi dosya işlemleri var kabaca bakalım isterseniz;
# Dosyadan Okuma
# Dosyaya Yazma
# Satır Okuma
# Satır Yazma

# Bu işlemleri yapmak için bazı kipleri bilmemiz gerekiyor isterseniz kısa ve net şekilde açıklayalım;
# "r" => Dosyayı okumamızı sağlar. (read)
# "w" => Dosya yazma kipinde açılır (write)
# "a" => Dosya yazma kipidir. "w"den farkı eğer öyle dosya yoksa oluşturmamızı sağlar.
# "x" => Dosya yazma kipinde açar. Eğer belirtilen yolda dosya mevcut ise hata mesajı alırız.
# "r+" => Dosyayı hem yazma hem de okuma yetkisine sahip oluruz. Ancak dosyanın var olması gerekir.
# "w+" => Dosyayı hem yazma hem de okuma yetkisine sahip oluruz. Eğer belirtilen yolda dosya mevcutsa silinir.
# "a+" => Dosyayı hem yazma hem de okuma yetkisine sahip oluruz. İçeriğe dokunulmaz içerikler kaydedilerek devam eder.
# "x+" => Dosyayı hem yazma hem de okuma yetkisine sahip oluruz. Dosya mevcutsa açmak yerine hata mesajı gönderir.


# İsterseniz şimdi alperaybakindustries.txt dosyası açalım.

dosya = open("alperaybakindustries.txt","r")

for i in dir(dosya):
    if i[0] != '_':
        print(i)

dosya.close()

# Çıktımız ==>
# buffer
# close
# closed
# detach
# encoding
# errors
# fileno
# flush
# isatty
# line_buffering
# mode
# name
# newlines
# read
# readable
# readline
# readlines
# reconfigure
# seek
# seekable
# tell
# truncate
# writable
# write
# write_through
# writelines


#! Pythondan direk dosya oluşturmak içinse şöyle bir şey yapabilirsiniz;

dosya = open("aaicompany.txt","w")
print(dosya)



#! Dosya Okuma

# Dosya okumak için iki veri kullanabiliriz;
# read() 
# readlines()
# read() metodu dosyayı okumamızı sağlar, readlines() metodu ise lines(satır)'dan anlaşılacağı gibi satır okumamızı sağlar.

# Oluşturduğumuz dosya içerisine gidip bir şeyler yazalım.
# Ve sırasıyla uygulayıp nasıl okuyoruz görelim;

dosya = open("aaicompany.txt","r")

veri = dosya.read()
print(veri)

dosya.close()

# Çıktımız :
# Alper Aybak
# Yazilim
# Elektrik - Elektronik
# 1.8 m boy
# Iron - Man
# Audi R8

# Bir de readlines() verisini görelim;

dosya = open("aaicompany.txt","r")

veri = dosya.readlines()
print(veri)

dosya.close()

# Çıktımız => ['Alper Aybak\n', 'Yazilim\n', 'Elektrik - Elektronik\n', '1.8 m boy\n', 'Iron - Man\n', 'Audi R8\n']


#! Dosyaya Yazmak 

# Yazı yazabilmek için yazma modunda açmamız lazım üst tarafa gösterdiğim gibi aslında.
# "w" verisini kullanıyoruz.
# Görelim;

dosya = open("alperaybak.txt","w")

isim = "Alper Aybak\n"
araba = "Audi R8\n"
meslek = "Yazilim"

dosya.write(isim)
dosya.write(araba)
dosya.write(meslek)

dosya.close()

# Çıktımız => 
# Alper Aybak
# Audi R8
# Yazilim


# writelines() metodumuzda var fakat bu metod ile sadece demetleri yazabiliriz.
# İsterseniz deneyebilirsiniz;



#! CSV Dosyaları

# Sıklıkla kullanılan bir doya tipidir.
# Açılımı => Comma Separated Values (Virgülle Ayrılmış Değerler)
# Bu dosya ile işlem yapmak için modüllerimiz vardır fakat bu konuya değinmeyeceğim 
# İsterseniz araştırabilirsiniz.





# Evet arkadaşlar Temel Dosya İşlemleri dersimizin sonuna geldik.
# Kafanıza takılan herhangi bir yer olursa iletişime geçebilirisniz.
# Bir sonraki derste görüşmek üzere....