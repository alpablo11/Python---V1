# AAI Company - Python

# Koşul Durumları

# Arkadaşlar bu kısımda koşulları göreceğiz.
# 3.bölümdeki operatörleri hatırlatmak için ve mantığını tamamen oturtmak için tekrar işleyeceğiz.
# O yüzden aynı dersi görüyoruz diye lütfen geçmeyin :)

# Koşullara aslında hayatın her anında ihtiyaç duyarız hatta kullanırız. Örneğin istemsiz bir şekilde gerçekleştirdiğimiz reflekslerden örnek verelim;
# Bir cismin gözümüze doğru geldiğini düşünelim. Beynimize bu sinyali gönderiyoruz ve o da eğer cisim geliyorsa gözleri kapat komutunu veriyor. Veya Tehlikeli değilse açık tut gibi düşünebiliriz.
# O zaman biz koşulu şöyle tanımlayabiliriz => başka bir şey olursa, gerçekleşirse ya da yerine gelirse olması gereken şey, gereklilik.


# KOŞULLU İFADELER
# Python da ve diğer yazılım dillerinde koşullar 3 bloktan oluşur. Bunlar IF,ELIF,ELSE bloklarıdır.
# Ama bunlara geçmeden dediğim gibi önce operatörleri hatırlayalım;


#ARİTMATİK İŞLEÇLER:

# Toplama: +
# Çıkarma: -
# Çarpma: *
# Bölme: /
# Kuvvet Alma: **
# Mod Alma: %

# KARŞILAŞTIRMA İŞLEÇLERİ:

# Eşittir: = veya == (koşul durumlarında == kullanırız, değer atarken de = kullanırız)
# Eşit Değildir: !=  (İngilizcede olumusuz yapmak için nasıl not eki geliyorsa cümle başlarına pythonda da ! işareti gelir.)
# Büyüktür: >
# Küçüktür: <
# Büyük Eşit: >=
# Küçük Eşit: <=



# BOOL VERİ TİPİ:
# Öğrendiğimiz gibi bunlar true/false parametreleridir.

#İsterseniz bunlarla ilgili hatırlamak amaçlı birkaç örnek verelim;

a=11
n=6

print(n+a)
print(a-n)
print(n/a)
print(n*a)
print(n%a)
print(n**a)

print(n>a)
print(n<=a)
print(a<n)
print(n!=a)
print(n>=a)

# IF - ELIF - ELSE :

# "if" => Eğer anlamına gelmektedir
# "elif" => "if" koşulu sağlanmadığı zaman minimum 3 koşul olduğu zaman devreye girer. Anlam karışıklığını gidermek içindir. Öyle değil de bu anlama geliyorsa anlamındadır.
# "else" => Hiçbir koşul sağlanmazsa else durumu devreye girer

# İsterseniz bir örnek verelim;
x=int(input("Açı1: "))
y=int(input("Açı2: "))
z=int(input("Açı3: "))
w=int(input("Açı4: "))

if (x+y+z+w == 360):
    print("Bu bir dörtgendir.")

else:
    print("Bu bir dörtgen değildir!")

# Yukarıdaki örnekte de anlaşılacağı gibi koşullarımızı verdik ve kullanıcıya göre bize sonuç verecektir. 
# Ayrıca fark ettiyseniz "else" yazdıktan sonra koşul belirtmedim. Başta da dediğim gibi herhangi bir koşul geçerli olmazsa yazdıracağımız parametredir.

# IF ve ELSE ile bir örnek daha yapalım isterseniz;

print("Mekanımıza Hşgeldiniz (+18 mekandır)")
yas= int(input("Lütfen Yaşınızı Giriniz: "))

if (yas >= 18):
    print("Mekana Girebilirsiniz.\nİyi Eğlenceler...")

else:
    print("18 yaşından küçüksünüz mekana giremezsiniz.")

# Anlaşıldı diye düşünüyorum ve bir diğer koşulumuz olan ELIF koşulu nasıl kullanılıyormuş bakalım;

print("Dersten Geçmiş Sorgulama Sistemine Hoşgeldiniz")
notunuz= float(input("Lütfen Notunuzu Giriniz: "))

if (notunuz>=90):
    print("Dersten A ile geçtiniz,durumunuz başarılı.")

elif (notunuz>=80):
    print("Dersten B ile geçtiniz,durumunuz iyir")

elif(notunuz>=70):
    print("Dersten C ile geçtiniz, durmunuz normal")

elif (notunuz>=55): 
    print("Dersten D ile geçtiniz, biraz daha çalışalım!")

else:
    print("Üzgünüm dersten kaldınız :(")



# BOOL İŞLEÇLERİ:
# İki koşulu birbirine bağlamak için bool işleçlerini kullanırız. Peki bunlar nelerdir? Gelin beraber bakalımm...
# "and","or","not" 
# Bu 3 işleç sayesinde koşulları istediğimiz gibi bağlayabiliriz.
# and = ve anlamını verir. Alper ve Hüseyin yazılımcı mı? sorusunu sorduğumuz zaman doğruysa bize true dönüşü yapacaktır fakat herhangi biri yanlışsa dönüş false olarak çıkacaktır.
# or = veya anlamını verir. adn işlecinin tersine true çıktısı almamız için iki koşuldan birinin doğru olması yeterlidir.
# not = değil anlamı verir. Az çok tahmin etmissinizdir fonksiyon sağlanmıyorsa kullanacağımız işleçtir.
# İsterseniz örnekle hafızamıza kazıyalım 

# and örneği:

a = float(input("Bir sayı giriniz: "))
n = float (input("Bir sayı giriniz: "))

if (a>11 and n<=6):
    print("İstenilen koşullar sağlandı")

else:
    print("İstenilen koşul sağlanmadı") 



# or örneği:

username1 = "Alper Aybak"
username2 = "AAI Company"
login = input("Lütfen Kullanıcı Adı Giriniz")

if (login == username or login == username2):
    print("Başarılı Giriş Yaptınız")

else:
    print("Giriş Başarısız, böyle bir kullanıcı yok!")


# not örneği:

print("sociAlmediA'ya Hoşgeldiniz...")

text = input("Lütfen Bir Şeyler Yazınız: ")

if not text:
    print("Text kısmını boş bıraktınız , lütfen bir şeyler yazınız!")

else:
    print("Text kısmı onaylandı.")



# EWvet arkadaşlar bool işleçlerimiz bu şekilde. bool işleçleri fark ettiğiniz gibi true/false mantığı ile çalışıyor. Anladığınızı düşünüyorum kafanıza takılan bir şey olursa sorabilirsiniz :)



# Aitlik İşleçleri:
# İçinde anlamını veren "in" operatörümüz bize aitlik kazandırır.
# Örnekle açıklamak daha kolay anlamamızı sağlayacaktır;

alper = "AA INDUSTRIES|alperaybakindustries"

if "a" in alper:
    print("a harfi var.")

if "c" not in alper:
    print("İçinde c harfi yok!)



# Değer Atama İşleçleri 
# Değer atama operatörlerinden bahsetmiştik.
# Fakat ben burada bazı kısa yolları gösterip 6.dersimizi de bitireceğim
# İsterseniz önce değer atama işleçlerini hatırlayalım daha sonra kısayollara geçelim;

a = 11
n = 2

print(a)
print(n)


a = a-9
n = n+9

print(a)
print(n)

# a'nın değerini azaltırken ve n'nin değerini arttırırken bu işlemleri uyguluyoruz gördüğünüz üzere fakat bunların bir kolay yolu daha var;

a = 11
a +=1
print(a)

n = 28
n -= 17
print(n)

# GÖrdüğünüz gibi daha kolay bir şekilde halletmiş olduk. Diğer işleçleri de yazalım...

#  +=
#  -=
#  *=
#  /=


# Evet arkadaşlar 6.dersimizin sonuna gelmiş bulunduk. Burayı güzelce öğrendiysek diğer dersimizde döngüler kısmına değineceğim. Herhangi bir sıkıntı olursa iletişime geçebilirsiniz.