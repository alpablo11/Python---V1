# AAI Company - Python 

#! Gömülü Fonksiyonlar:
# Python da bulunan hazır fonksiyonlara gömülü fonksiyon diyoruz.

# İsterseniz şu ana kadar işlediğimiz gömülü fonksiyonlara liste halinde bakalım;

# print (yazdırma)
# len   (uzunluk)
# min   (min. değer)
# max   (max. değer)
# range (sıralı sayı)
# list  (liste)
# tuple (demetler)
# dict  (sözlük)
# set   (kümeler) 
# int   (tam sayı)
# str   (string karakter dizisi)
# bool  (true/false)
# float (ondalık sayı)
# type  (veri tipi)
# input (kullanıcıdan veri isteme)


# İsterseniz şimdiye kadar kullandığımız fonksiyonların üzerine farklı bilgiler katalım;

#! Farklı Gömülü Fonksiyonlar
# Programcılık maceramızda bize eşlik edecek diğer fonksiyonları göreceğiz.
# Fazla beklemeden geçelim isterseniz;





#! open()
# open() fonksiyonu bize bir dosya objesi yaratır.
# Yani list() objesi ile nasıl liste oluşturuyorsak open() objesi ile de dosya yaratırız.
# İsterseniz örneğe bakalım;

dosya = open("alperaybakindustries.txt", "w")
print(type(dosya))
dosya.close()

# Çıktımız => <class '_io.TextIOWrapper'>
# Böyle bir çıktı karşımıza çıktı ve bizim için bir .txt uzantılı dosya oluşturdu.
# "w" metodunu anlamamış olabilirsiniz ilerideki konularda işleyeceğimiz bir metod. (w=write (yani dosyanın içerisine yazı yazmak istiyoruz))
# RAM  bellekte yer kaplamasın diye de close() metodunu kullandık.




#! abs()
# Absolute kelimesinde türeyen bir fonksiyondur. Türkçe de karşılığı "mutlak"'dır.
# Az çok oturmuştur mutlak olarak çıktı verdiğine göre matematikteki mutlak değer ile aynı işlevi yapacağı.
# Örneğe bakalım;

n = -11
a = 11
print(abs(n))
print(abs(a))

# Çıktılarımız ==> 
# 11
# 11

# Görüldüğü gibi mutlak değer çıktısı aldık.





#! round() 
# Herhangi bir küsüratlı sayıyı yuvarlama işlemini gören fonksiyondur.
# Dilerseniz örneğe bakalım;

numbers = [11.2, 1.06, 0.23, 21.11, 4.9, 12.02]

for i in numbers:
    print("{} -->> {} ".format(i,round(i)))

# Çıktımız==> 
# 11.2 -->> 11 
# 1.06 -->> 1 
# 0.23 -->> 0 
# 21.11 -->> 21 
# 4.9 -->> 5 
# 12.02 -->> 12 

# Gördüğümüz gibi yuvarlama işlemini yaoıyor.





#! all()
# all kelimesinin Türkçe karşılığı hepsi/tümü anlamına gelmektedir.
# Pythonda şöyle bir şey mümkündür tüm verilerin bool karşılığı true ise true döndürebilir.
# Test edelim;

numbers = [11.2, 1.06, 0.23, 21.11, 4.9, 12.02]

print(all(numbers))

# Çıktımız ==> True
# Eğer sayılardan birisi 0 olsaydı bu çıktı bize False olarak dönüş yapacaktı.




#! any()
# all() fonksiyonunun tersidir.
# Eğer en az bir değerin bool değeri True ise True dönüş yapar
# Görelim;

liste = [0,0,0,0,0,0,0]
print(any(liste))

# Çıktımız ==> False
# 0 değeri false veriyordu



#! bin()
# Binary sayı sisteminin kısaltılmasıdır. (0,1 arası)
# Bu ikilik sayı anlamına geliyor.
# Herhangi bir sayıyı ikilik sistemde yazmak istersek kullanırız. Görelim;

print(bin(2002))

# Çıktımız ==> 0b11111010010
#! Eğer 0b yazıyorsa o sayı ikilik, 0x yazıyorsa onaltılık sistemde, 0o yazıyorsa da sekizlik sayıyı temsil etmektedir




#! hex() 
# Aldığı ondalık değerdeki sayıyı onaltılık sisteme dönüştürür.
# Bakalım;

print(hex(1106020022122002))

# Çıktımız ==> 0x3edeb5a887612
# Gördüğümüz gibi önünde 0x yazıyor önceki fonksiyonda 0b yazıyordu.





#! oct()
# Oktal yani sekizlik sistemde sayı üretmek için kullandığımız fonksiyon oct() fonksiyonudur.
# Dilerseniz görelim;

print(oct(231145678))

# Çıktımız ===> 0o1561600316
# Görüldüğü gibi bunun da baş kısmında 0o (sekizlik sistem) var.





#! divmod()
# Verilen bir sayıyı diğer sayıya bölüp demet halinde bize döndürmesidir.
# İnceleyelim;

number1 = 11
number2 = 3

print(divmod(number1,number2))

# Çıktımız ==> (3, 2)





#! exit() 
# Programımızı sonlandırmaya yarar.
# Örnekle daha açıklayıcı yapalım;

while True:
    a= input("İşlem Giriniz:")
    if (a == "q" or a == "Q"):
        exit()

# Yukarıdakı kodumuzu çalıştırırsanız q veya Q girene kadar program durmayacaktır.




#! pow()
# Kuvvet hesaplamak için kullanılan fonksiyondur.
# Görelim;

print(pow(11,3))

# Çıktımız ==> 1331
#! Hatırlatma == Bir diğer kuvvet alma işlecimiz de ** dır. (11**3)


#! isinstance()
# Herhangi bir fonksiyonun veri tipini öğrenebileceğimiz fonksiyonlardan biridir.
# Normalde type kullanıyorduk ama daha kolay halledebileceğimiz için bu sefer bunun kullanacağız.
# Dilerseniz bakalım;

na = "AAI Company"

if (isinstance(na, int)):
    print("Bu bir tamsayı")

elif (isinstance(na, str)):
    print("Bu bir karakter dizisi")


elif (isinstance(na, tuple)):
    print("Bu bir demet")


elif (isinstance(na, list)):
    print("Bu bir liste")


else:
    print("Bu başka bir fonksiyon olabilir...")


# Çıktımız ==> Bu bir karakter dizisi

# Dilerseniz na'ya input (kullanıcıdan veri alma) fonksiyonunu da adayabiliriz şöyle;

na = input("Bir şeyler giriniz:")

if (isinstance(na, int)):
    print("Bu bir tamsayı")

elif (isinstance(na, str)):
    print("Bu bir karakter dizisi")


elif (isinstance(na, tuple)):
    print("Bu bir demet")


elif (isinstance(na, list)):
    print("Bu bir liste")


else:
    print("Bu başka bir fonksiyon olabilir...")






# Evet arkadaşlar gömülü fonksiyonların sonuna gelmiş bulunuyoruz.
# Elimden geldiği kadar açık şekilde anlatmaya çalıştım umarım yararlı olmuştur.
# Kafanıza takılan herhangi bir şey varsa iletişime geçebilirsiniz.
# Bir sonraki dersimizde görüşmek üzere.....