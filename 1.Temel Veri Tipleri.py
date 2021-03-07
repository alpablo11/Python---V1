# AAI Company - Python 

# Temel Veri Tipleri 

#Değişkenler:
# Kendi içlerinde değer tutarlar.
# Örneğin ben a harfine 11 değerini atamak istiyorum ve a'yı çağırdığım zaman 11'i görmek istiyorum
#Yani şu şekilde;

 a=11
 b=21
 n=111
 aa=2121

 # Aslında ben şunu söyledim Python'a: 
 # a'yı yazdır dediğimde=11
 # b'yi yazdır dediğimde=21
 # n'yi yazdır dediğimde=111
 # aa'yı yazdır dediğimde=2121

 #Bir sonraki derste öğreneceğiz ama kafanızda daha iyi oturması için şöyle göstereyim;

 print(a)
 print(b)
 print(n)
 print(aa)
# NOT: print kısaca yazdır anlamına geliyor 

ad= "Alper"
soyad= "Aybak"
yas = "18"
depertman = "yazilim"

# aynı şekilde burada da;
# ad'ı yazdır dediğimde = Alper
# soyad'ı yazdır dediğimde = Aybak
# yas'i yazdır dediğimde = 18
# depertman'ı yazdır dediğimde = yazilim
 




 # Integer Veri Tipi :
 # Tam sayı tipleridir yani virgülü olmayan sayılardır.
 #  int(sayı girin) şeklinde yazdırabiliriz.

a=int(11)
b=int(21)

print(a+b)

# peki ya biz burada int olduğunu belirtmezsek "" arasına sayı yazarsak ne fark edecek? Gelin beraber bakalım;

a="11"
b="21"

print(a+b)

# tırnak içine almadan yazarsak ta bize integer sonuç verecektir. Örneğe bakalım yine;

a=11
b=21

print(a+b)



# Float Veri Tipi
# Ondalık sayı tipidir yani virgülden sonrası vardır. Fakat burada değer atarken virgül yerine nokta kullanırız
#Örnek olarak; 
# n=11,02 (yanlış)
# n= 11.02 (doğru)
# float(sayi) şeklinde yazılabilir.

n=float(12.06)
na=float(11.02)

print(n+na)

# Veya düz şekilde de yazılabilir.

n=12.06
na=11.02

print(n+na)



# String Veri Tipi
# Karakter dizisidir.
# En önenli unsur burada tırnak işaretidir. Yoksa sistemimiz hata verecektir.
# Aslında yukarıda yaptığımız örnek string türündendir. İsterseniz tekrar hatırlayalım;

ad= "Alper"
soyad= "Aybak"
yas = "18"   #Tırnak içine aldığım için integer veri tipini stringe çevirmiş oldum.
depertman = "yazilim"

print(ad)
print(yas)
print(soyad)
print(depertman)