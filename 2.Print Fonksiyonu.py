# AAI Company - Python 

# Print Fonksiyonu 

# Arkadaşlar aslında python'a ilk girişte öğrenmeniz gereken ve asla unutmamamız gereken komuttur.
# Sebebini açıklayayım; Python'ı kurduktan sonra bize gelen IDLE dosyası dışında hiçbir programda print fonksiyonu olmadan (örnek olarak söylüyorum) 3+5 işleminin çıktısını alamayız.
# Sosyal medyada yazılım sayfaları takip edenler varsa veya reklam olarak falan karşınıza çıktıysa görmüşsünüzdür "Hello World" yazdırırlar işte bu çıktıyı almamızı sağlayan fonksiyon "print" fonksiyonudur.
# Print fonksiyonundan string çıktısı istiyorsak:  print("yazmak isteediğiniz metin veya yazı") 

# Ne demek istediğimi anlamışsınızdır zaten ama gelin örnekle destekleyelim bubları;

print("AAI Company Python Dersine Hoşgeldiniz")

print("AA INDUSTRIES|alperaybakindustries")

print("Alper Aybak")

print("Software")

print("Bilgiler Gösteriliyor...")

print("Hüseyincan Bağcı")

# Print fonksiyonu ile alt alta çıktı da almak istersiniz bunun için yazılarınız arasına \n koymalısınız.

print("AAI Company\nAlper Aybak\nHüseyincan Bağcı")

# Yan yana yazdırmak için ise stringleri virgül(,) ile ayırmanız gerekir.
#18 integer sayı tipi olduğu için "" kullanmama gerek yok.
print("Alper Aybak","Sofware",18) 


#Değişken atayıp onları da yazdırabiliriz

company= "AAI"
fullname= "Alper Aybak"
age= 18

print(fullname,company,age)

#Başka bir örnek verelim 

simdikiyil= 2021
dogumyili= 2002
yas= simdikiyil-dogumyili

print("Yaşınız: ",yas)


# Detaylara inecek olursak, Print fonksiyonunu birkaç bir şeyden daha bahsetmeden geçmek istemiyorum...

# sep Parametresi:
# Print fonksiyonun içine yazdığınız birden çok karakterlerin aralarına aynı işaretleri koyacaksanız kolayca halletmenizi sağlar.
#Örnekle açıklamak gerekirse;

print("Alper","Aybak","Software","Colifornia/Malibu", sep="_")

print("Alper","Aybak","Software","Colifornia/Malibu", sep=".")

print("Alper","Aybak","Software","Colifornia/Malibu", sep="0")

print("Alper","Aybak","Software","Colifornia/Malibu", sep="-")


# end Parametresi:
# İsminden de anlaşılacağı gibi en sona istediğinizi ekliyor
# Yine örnekle açıklayalım

print("Alper Aybak, AA INDUSTRIES|alperaybakindustries'in kurucusudur ", end=".")

print("Alper Aybak, AA INDUSTRIES|alperaybakindustries'in kurucusudur ", end="\n")
print("AAI Company: Software,Developers,Sport Club,Space,Engineering" ,end="...")


