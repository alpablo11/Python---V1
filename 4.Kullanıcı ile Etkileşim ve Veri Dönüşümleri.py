# AAI Company - Python

# Kullanıcı ile Etkileşim ve Veri Dönüşümleri

# Input Fonksiyonu: 
# Kullanıcıdan string veri tipinde bilgi almamızı sağlar
#Örnek verelim daha iyi anlaşılacaktır;


ad=input("Adınızı Giriniz: ")
soyad= input("Soyadınzı Giriniz: ")
yas= input("Yasınızı Giriniz:")
meslek = input("Mesleğinizi Griniz: ")

print(ad,soyad,"\n",yas,"\n",meslek)

# Veri Tipi Dönüşümleri:
# Veri tipi dönüştürmemizin asıl amacı yukarıda da bahsettiğimiz gibi input fonksiyonu "string" olarak değer alıyor. 
# Yani sayı isteyeceğimiz zaman float mı yoksa integer mı olduğunu belirtmemiz gerekiyor.
#İsterseniz örnekle destekleyelim;

sayi1 = input("Sayı1: ")
sayi2 = input("Sayı2: ")
toplam= int(sayi1)+int(sayi2)

print("Sonuç", toplam)


# Integer Dönüşüm:
# Herhangi bir sayıyı ya da sayı barındıran diziyi tam sayıya dönüştürme metodudur.
# İsterseniz örnekle açıklayalım;

sayı1=35.8
tamsayı= int(sayı1)

print(tamsayı)
print(type(tamsayı))




#Type Metodu:
#Yukarıda öğrenmediğimiz bir terim var "type" metodu. 
# "type" metodu bize verinin cinsini döndürür. 
#İsterseniz buna da örnek verelim;

print(type("AAI Company from Alper Aybak"))


#Eğer örneği Run yaptıysanız <class 'str'> olarak geri dönüş yaptığını göreceksiniz.
# Buradaki str aslında String'in kısatlmasıdır.

sayı2=11.21
tamsayı2= int(sayı2)

print(type(tamsayı2))

#Yularıdaki "tamsayı" örneğine bakarsanız da Integer (int) olarak dönüş yaptı bize. (class=sınfı anlamına gelir)



# Float Dönüşümü:
# Tıpkı Integer gibi float fonksiyonu da mevcuttur.
# Geri dönüş almak istediğimiz fonksiyonlarda float olarak almak istersek float() şeklinde yazarız.
# İsterseniz örnek ile pekiştirelim;
 
a= input("1.Sayıyı Giriniz: ") 
n= input("2.Sayıyı Giriniz: ")

a = float(a)
n = float(n)

print("İşlem Sonucu: ", n+a)



# String Dönüşüm:
# Tıpkı int ve float gibi string veri tipini de dönüştürebiliriz.
# Farkı şudur: Diğer iki dönüşümde hata alma payımız vardır fakat string dönüşümlerinde hata şansı yoktur.
# Ancak karakter dizileri içerisinde çokça karakter bulunabilir. Örneğin 'A' karakteri varsa bir karakter dizisinde bu veri sayıya dönüşmez
# Örnekle pekiştirelim isterseniz;

sayi_1= input("Sayı Giriniz: ")
sayi_2= input("Sayı Giriniz: ")

sayi_1= float(sayi_1)
sayi_2= float(sayi_2)

toplam= sayi_1 + sayi_2

print("İşlem Sonucu: ", toplam)
toplam = str(toplam)
sonhane = toplam[-1:] #Listeler dersinde göreceğiz ama kısaca şöyle demektir sondan başla en başa doğru yazdır.
print("Son İki Hane:", sonhane)




