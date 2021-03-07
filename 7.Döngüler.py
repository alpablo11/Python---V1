#  AAI Company - Python

#  Döngüler:
#  - Döngü Nedir?
#  Döngüler sadece Python programlama dilinde değil tüm programlama dillerinde kullanılır.
#  Döngü algoritması, sürekli ya da belli sayıda tekrar eden işlemler için geliştirilmiş algoritmalardır.

# Birazdan bahsedeceğim ama tanımı açıklamak için bir örnek göstereceğim anlamazsanız sıkıntı etmeyin, dediğim gibi öğreneceğiz;

for i in range (111): # Bu kod bize 0 ile 111 arası sayıları bastıracaktır. (0 dahil)
    print(i)


# Acele etmeden bir örnek daha vermek istiyorum. 
# Bu örneğimizde de Kullanıcının 11'den büyük sayı girmesi koşuluna bağlı olan sonsuz yani sayısı belli olmayan döngümüzü yazalım;

while True : 
    a = int(input("Bir sayı giriniz: "))
    if a > 11 :
        print("Sayı doğrulandı")
        break

    else: 
        print("Tekrar sayı giriniz")




# Döngü Çeşitleri: 
#Döngü çeşitlerinden az çok bahsettik aslında burada bu işleri hangi döngü ile yaptığımızdan bahsedeceğiz ve yukarıda yazmış olduğum örnekler kafanızda oturacaktır.

  # -While Döngüsü:
  # Sayılamaz döngüler için kullanılır. (Sonsuz döngü)
  # Bir koşula bağlıdır aynı if gibi bool cinsinden veriye bağlıdır.

  # Aşağıdaki örneği inceleyelim;

  while True: 
      print("AAI Company ile Dünyanın Ötesinde Emin Ellerdesiniz!)

  # Çıktısını aldığımız zaman (run yaptığımızda) sonsuza uzanan bir döngü ile karşı karşıyayız. 
  # Buradan çıkmak için "Ctrl+C" veya "Ctrl+Z" tuş kombinasyonuna basmanız gerekiyor. Aksi takdirde döngümüzün sonu gelmez (Program kapatılmadığı sürece).
  # Yani biz döngümüze bir sınır vermezsek sonsuza kadar gideceğini öğrenmiş olduk.
  # Peki döngüye nasıl sınır koyabiliriz? İsterseniz beraber bakalım;

sayia = 11
while (sayia <= 111):
    print(sayia)
    sayia +=11


# Gördüğünüz gibi döngümüze bu şekilde limit vererek durdurabiliriz.

# Döngüler için kırılma noktası yaratmamız şarttır. Eğer kırılma noktası belirlemezsek ya da Python'a bunu bildirmezsek program sonuç vermeden sürekli döngüde kalır.
# İsterseniz while döngüsünü daha iyi anlamak için başka örnekler de yapalım;

sayi = 0
while True:
    print(sayi)
    sayi += 10
    if sayi >= 100:
        break  # Adından da anlaşılacağı gibi break durdurma metodudur.

# Yukarıdaki kodumuz bize 100 kadar (100 dahil) çıktı verecektir.

# Fark ettiyseniz koşulu while içine yazmadık onun yerine True kullandık.
# !!! Arkadaşlar burası çok önemli eğer while True olarak kullanıyorsak döngüyü durdurmak için break metodunu kullanmamız şarttır !!!

# İki tane aynı örneği yapalım ve buna netlik getirelim;

a = 1
while a<11:
    print(a)
    a +=1

# while True  ile yaparsak;

a = 1
while True:
    print(a)
    a +=1
    if a <11:
        break 

# İkisi de aynı sonucu verecektir istediğinizi kullanabilirsiniz.



# FOR DÖNGÜSÜ:
# for döngüsünü örnekler üzerinde anlatalım isterseniz;

for i in range(10):
    print(i)

# Gördüğünüz  gibi 0'dan 10'a kadar olan sayıları yazdırdık.
# While döngüsünden daha kolay bir şekilde hallettik fakat bu genel olarak sayılar için  geçerlidir diyebiliriz. 
# İlerleyen zamanlarda nerde while döngüsü seçmemiz gerekiyor örnekler üzerinde anlayacaksınız


# range fonksiyonuyla sayılar üretebiliyoruz hatta sayıları istersek ikişer istersek üçer şekilde olacak şekilde üretebiliriz.
# Örnekle açıklayalım;

for i in range(0,111,2):
    print(i)

# Çok kolay şekilde 0'dan 111'e kadar sayıları ikişer artarak yazdırabiliyoruz.
# Yapmamız gereken şey range fonksiyonu içine sırasıyla range(kaçtan başlayacağı,kaça kadar yazılacağı,kaçar artacak)

# Peki azaltmak istersek ne yapacağız? Aslında tahmin ettiğiniz gibi tam tersi yani şunu demek istiyorum:
# range(hangi sayıdan başlayacağı, hangi sayıya inmek istediğimiz,kaçar azalacağı)
# Örnekle kafamıza oturtalım isterseniz;

for i in range(111,0,-2):
    print(i)


# Biz for föngüsünde sadece range fonksiyonu değil, ileride işleyeceğimiz "Tuple ve List" veri tipleri ile de çokça kullanacağız.
# İsterseniz örnek verelim;

a = list(range(0,11))
print(a)
for i in a:
    print(i)

# Bu örnekte ekrana 0'dan 11!e kadar olan sayılar basılacak. 
# Ancak ilk önce liste şeklinde
# Daha sonra alt alta basacaktır.


# !!! NOT= Listelerin belirteçleri köşeli parantezlerdir []  !!!


# For döngüsünü kullanmak için bir veriye ihtiyaç duyarız. 
# Bunu ister "range" ile, ister "tuple", istersek de "list" ile yapabiliriz.
# Hatta "String" ile de yapabiliriz.
# İsterseniz örnekle inceleyelim

alper = "AA INDUSTRIES|alperaybakindustries"

for AAI in alper:
    print(AAI)


# İsterseniz alfabemizdeki harfleri de bastırabiliriz, görelim;

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

for harf in alfabe:
    print(harf)


# "for" döngüsünü kullanmak için bir veriye ihtiyaç duyuyoruz.
# Fakat "for" aynı zamanda koşul ifadesidir.
# Bu yüzden for döngüsüne verdiğimiz bool değeri "true" olmalıdır.
# Örneğin "boş bir string" olursa döngümüz çalışmayacaktır.
# İsterseniz örnekle inceleyelim;

aybak = ""

for i in aybak:
    print(i)

# Gördüğünüz gibi program çıktı vermeden sonlandı.
# Üst kısımda "while" döngüsünde break (sonlandır) deyimini kullanmıştık. Döngümüzü kırmaya yarıyordu. Burada da aynı şey geçerli.
# ! Eğer bir şart sağlandığı zaman döngünün kırılmasını (durmasını) istiyorsak "break" deyimini kullanacağız. !

# Dilerseniz bir örnek yapalım bununla ilgili;

karisik_harfler = "aslkfhalşhflashgvlasfbn"
aranan_harf = input("Aramak istediğiniz harfi giriniz: ") 

if aranan_harf in karisik_harfler:
    print("Aradığınız harf var.")

else:
    print("Aradığınız harf yok!")


# Kodumuz çalışıyor. Fakat bazı durumlarda bu yeterli olmayabilir.(Yani içinde var mı yok mu sorgusu) 
# İlerde uygulayacağımız list ve tuple ile veri kıyaslamaları yapacağız ve çok eğleneceğiz.
# İsterseniz bir örnekle açıklayalım ne demek istediğimizi;

karisik_harfler = "aslkfhalşhflashgvlasfbn"
aranan_harf = input("Aramak istediğiniz harfi giriniz: ") 

flag = false

if harf in karisik_harfler:
    if harf == karisik_harfler:
        flag = True
        break

if flag:
    print("Aradığınız harf var.")

else:
    print("Aradığınız harf yok!")


# Çalıştırdığımız zaman anlaşılmıştır diye düşünüyorum ama ayine de açıklayıp 7.dersimizi bitirelim.

# 1) İçerisine klavyeden girdiğim rastgele harflerle oluşmuş bir "string" oluşturduk.
# 2) Kullanıcıdan harf istedik sorulmamız için.
# 3)flag adında bir değişken oluşturduk. Bu değişken ileride yapacağımız arama sonuçlarına göre yeniden atanacak.
# 4) for döngüsü sayesinde karisik_harfler değişkenindeki her bir harf adlı değişkene atadık.
# 5) Eğer aranan harf ile o anki harf aynı ise flag değişkenini "true" duruma getirdik ve döngünün durmasını söyledik( break ile).
# 6) flag ile koşullu mekanizma yarattık. flag eğer "true" ise ekrana Aradığınız har var yazacsak. Eğer flag true sonucu vermezse else bloğu çalışacak ve Aradığınız harf yok! sonucunu verecek.



# Evet arkadaşlar döngüler dersimizin sonuna gelmiş bulunduk. Elimden geldiğince akılda soru işareti bırakmayacak şekilde açıklamaya çalıştım. 
# Umarım anlaşılmıştır. Eğer sorun varsa da hiç sıkıntı etmeyin benimle iletişime geçebilirsiniz.

#  8.derste break ile ilgili  örnek yapacağız ve örnek üzerinden açıklayacağız.