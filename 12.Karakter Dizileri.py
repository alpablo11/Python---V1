# AAI Company - Python

# Karakter Dizileri:
# Arkadaşlar bu konumuz python'da gerçekten büyük öneme sahip sakin kafayla bakmanızı tavsiye ederim. 
# Dilerseniz derse geçelim ve örneklerle işleyeceklerimizi açıklayalım...

# ! Verilerimizi düzenlerken çok fazla kullanacağız o yüzden iyi öğrenmemiz gerekiyor !

# Örnekle başlayalım isterseniz;

aai_company = "Alper,Aybak,Yazilim,industries,HüseyinCan,Bağcı,Finans"

# Gördünüz gibi karakter dizisi oluşturduk (string)
# Yazılanları tek tek sıralamak için şöyle bir kod çalıştıralım

aai_company = "Alper Aybak,Yazilim,Industries,Hüseyin Can Bağcı,Finans,Company"

company = aai_company.split(',')

for alper in company:
    print(alper)

# Gördüğünüz gibi sonuç aldık ama nasıl olduğunu anlamamış olabilirsiniz, birazdan hepsini işleyeceğiz.



# KARAKTER DİZİLERİNİ DİLİMLEMEK:
# Hatırlarsanız daha önce for döngüsünde karakter dizilerini kullanmıştık. Hatırlamak için isterseniz şu örneğe bakalım;

aybak = "AA INDUSTRIES|alperaybakindustries"

for a in aybak:
    print(a)

# Gördüğünüz gibi harfler a değişkenine atandı ve tek tek yazdırıldı.
# Bu kodu isterseniz bir de şöyle çalıştırayım;

aybak = "AA INDUSTRIES|alperaybakindustries"

for a in aybak:
    print(aybak.index(a),a)

# Harflerin başında numara gördük. 
# Bu gördüğümüz numaralar "a" değişkeninin, "aybak" değişkeni içerisindeki """indeks""" değerleridir.
# Ancak bazı harflerin yanında aynı numaralar çıktı. İsterseniz daha detaylı inceleme yapalım;

# !!! Karakter dizilerinde her bir öğenin sıra numöarası vardır. Ve değerler 1'den değil her zaman 0'dan başlar !!!
# Örnek olarak "alper" karakter dizisinin indeksi şu şekildedir.

harf -->> 0 Index -->> a
harf -->> 1 Index -->> l
harf -->> 2 Index -->> p
harf -->> 3 Index -->> e
harf -->> 4 Index -->> r

# Her bir harfin bir numaraya sahip olması bizim için kolaylık sağlar.
# Eğer sayısı belli olan bir veriyi merak ediyorsam kolayca çağırmamı sağlayabilir.
# İsterseniz örnek ile açıklayalım;

aybak = "Burası AAI Company."

print(aybak[0])
print(aybak[1])
print(aybak[2])
print(aybak[3])
print(aybak[4])
print(aybak[5])

print(aybak[6])

print(aybak[7])
print(aybak[8])
print(aybak[9])

print(aybak[10])

print(aybak[11])
print(aybak[12])
print(aybak[13])
print(aybak[14])

# Yukarıdaki örnekleri incelemenizi istiyorum.
# "aybak[0]"  aslında aybak karakter dizisinin içindeki "0.karakteri" göster anlamına gelir.
# 6 ve 10'u ayrı olarak belirttim fark ettiyseniz sebebi şu ikisini de tek başına çalıştırırsanız boş bir çıktı alacaksınız.
# !!! Karakter dizileri içindeki bıraktığınız boşluk, noktalama işareti veya semboller bir karakter olarak sayılır. !!!


# Bir de şu örneğe bakmanızı istiyorum;

aybak = "Burası AAI Company."

print(aybak[7:10])

# Bu kodu çalıştırırsak ekranda "AAI" çıktısını alacağız. Peki bu yaptığım ne anlama geliyor?
# "aybak[7:10]" aslında aybak karakter dizisinin içindeki "7.karakterden başla 10.karakter"e kadar yazdır anlamına geliyor.


# Örneklerle açıklamaya devam edelim isterseniz;

aybak = "Burası AAI Company."

print(aybak[0:])

# "aybak[0:]" ==> 0'dan başlayıp tüm karakter dizilerini yazdır anlamına geliyor
# ! İki nokta(:) bıraktıktan sonra bir şey yazmazsak sonuna kadar gider!
# Aynı şekilde [::] paramatresi de [0:] ile aynı anlama geliyor (En baştan sona kadar yazdır.)



# İsterseniz şu örneği inceleyelim bir de;

aybak = "Burası AAI Company."

print(aybak[::2])

# Burada da tüm karakter dizisini al fakat ikişer atlayarak yaz anlamına geliyor.

# Aynı şekilde sondan başlatıp da yazabiliriz, örnek olarak görelim;

aybak = "Burası AAI Company."

print(aybak[::-1]

# Sonuna "-" işareti koyduğumuz zaman sondan anlamı katmaktadır yani bize tersten okunuşunun çıktısını verir. (-2,-3,-4... şeklinde de başlayabilir)



# .upper() metodu:
# İsminden de anlaşılacağı gibi küçük harfleri, büyük harflere çevirmeye yarar.
# Örnekle açıklayalım isterseniz;

aai = input("Bir Kelime veya İsim Giriniz: ")
aai = aai.upper()

print(aai)




# KARAKTER DİZİLERİNİN METODLARI:
# Karakter dizileri de nesnedir. Ve belli başlı metodları vardır.
# Bu metotlar pek çok işi yapabilmemize olanak sağlar.
# İsterseniz başta yaptığımız örneği hatırlayalım;

aai_company = "Alper Aybak,Yazilim,Industries,Hüseyin Can Bağcı,Finans,Company"

company = aai_company.split(',')

for alper in company:
    print(alper)

#! Örneğin burada split() metodu sayesinde virgülleri kaldıurmış olduk.

# Karakter dizilerinin tüm metodlarını şu şekilde görebiliriz.
# Hatta unuttuğunuz zaman mutlaka hatırlayın bu kısmı ! dir() !
# İsterseniz görelim;

aybak = "AAI Company"

for a in dir(aybak):
    print(a)

# Kodu çalıştırdıysanız gömüşsünüzdür fakat ben bu metodları tam liste olarak vereceğim

# __add__
# __class__
# __contains__
# __delattr__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __getitem__
# __getnewargs__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __iter__
# __le__
# __len__
# __lt__
# __mod__
# __mul__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __rmod__
# __rmul__
# __setattr__
# __sizeof__
# __str__
# __subclasshook__
# capitalize
# casefold
# center
# count
# encode
# endswith
# expandtabs
# find
# format
# format_map
# index
# isalnum
# isalpha
# isascii
# isdecimal
# isdigit
# isidentifier
# islower
# isnumeric
# isprintable
# isspace
# istitle
# isupper
# join
# ljust
# lower
# lstrip
# maketrans
# partition
# replace
# rfind
# rindex
# rjust
# rpartition
# rsplit
# rstrip
# split
# splitlines
# startswith
# strip
# swapcase
# title
# translate
# upper
# zfill

# Görmüş olduğunuz gibi karşımızda baya uzun bir liste var. Ama bunların çoğu bizi ilgilendirmiyor.
#! Bizi ilgilendiren kısımlar alt çizgi (_) olmayanlardır. Peki bunları nasıl öğrenebiliriz görelim;

aybak = "AAI Company"

for a in dir(aybak):
    if a[0] != '_':
        print(a)

# Öncelikle kodu açıklayalım ve sonra çıktı olarak karşımıza neler geliyor görelim
# "aybak" değişkenini "a" harfine atadım ve a => 0'dan başlasın "_" olanları yazdırma dedim ve print(a) ile çıktımı aldım.

# capitalize
# casefold
# center
# count
# encode
# endswith
# expandtabs
# find
# format
# format_map
# index
# isalnum
# isalpha
# isascii
# isdecimal
# isdigit
# isidentifier
# islower
# isnumeric
# isprintable
# isspace
# istitle
# isupper
# join
# ljust
# lower
# lstrip
# maketrans
# partition
# replace
# rfind
# rindex
# rjust
# rpartition
# rsplit
# rstrip
# split
# splitlines
# startswith
# strip
# swapcase
# title
# translate
# upper
# zfill

# Bizim karakter dizileri metodlarımızın bunlar olduğunu gördük. 
# Peki burada kaçtane var isterseniz onu öğreneceğimiz bir kod çalıştıralım;

aybak = "AAI Company"
sayac = 0
for a in dir(aybak):
    if a[0] != '_':
        sayac +=1

print(sayac)

# Gördüğümüz gibi 45 adet metod bulunmaktadır.
# Dilerseniz kodu da açıklayalım:
# saymaya başladığı sayının 0 olmasını istediğimiz için sayac değerini 0 değerine atadık 
# daha sonra "_" olanları yazdırmaması için koşulumuzu sağladık ve sayac her seferinde 1 arttırsın dedik
# 1'den başlayıp yazmasın diye print() fonksiyonunu koşulun dışına yazdık (direk sonucu öğrenmek için)






# split(), rsplit() Metodu:
# Elimizdeki bulunan karakter dizisini belli ögeleri baz alarak bölme işleminde kullanılan metoddur.
# Örneğin bir metinde kaç kelime kullanıldığını ölçmemizi sağlar.
# Kaç kelime olduğunu öğrenmemiz biraz da listeye giriyor henüz işlemedik fakat bu konu için sorun yok sadece len() metodunu bilmemiz fayda sağlayacaktır.
#! len() ==> Uzunluğu ölçmemizi sağlayan liste metodu.

aybak = " Dünyanın ötesinde emin ellerdesiniz, hem de AAI Company farkıyla."

aybak = aybak.split(" ")
print(len(aybak))

# Gördüğünüz gibi 10 çıktısını aldık.
# Kodumuzu açıklayalım isterseniz;
# "aybak" adında karakter dizisi oluşturdum
# Daha sonra split() metodunu kullanara çift çentiği kaldırdım ve len() metodu ile kaç kelime olduğunu öğrendim.


# rspilt() ise bölme işlemlerini sağdan yapıyor. Eğer ikinci argüman verilmezse bu işlemin bir farkı olmaz.
# Önce splite bir örnek daha sonra da rsplit için bir örnek verelim isterseniz;

# split() örnek:
aybak = "AAI Company Alper Aybak tarafından 2021 yılında kurulmuştur."

aybak = aybak.split(" ")

print(len(aybak))
print(aybak)

# rsplit() örneği:
aybak = "AAI Company Alper Aybak tarafından 2021 yılında kurulmuştur."

aybak = aybak.rsplit(" ",3)

print(len(aybak))
print(aybak)

# Üstteki kodu çalıştırdığımız zaman çıktımız şu şekilde oluyor:
# 4
#['AAI Company Alper Aybak tarafından', '2021', 'yılında', 'kurulmuştur.']
# Bu şekilde 2 tane çıktımız var, anlaşıldığı üzere rsplit() metodunun sonuna girdiğiğmiz sayı kadar sında kelime bırakıyor. 
#! Yani sonda kaç kelime bırakmak istediğimizi rsplit()'in sonuna yazabiliriz anlamı çıkıyor 



# replace() Metodu:
# Yerine geçmek, yerine koymak anlamına gelir.
# Aslında anlamı görevini açıklıyor karakter dizisindeki bir karakteri, başka bir karakter yerine koymamızı sağlıyor.
# İsterseniz örnekle açıklayalım;

isim = "alper"
# İlk harfini dilerseniz bildiğimiz yöntemlerle değiştirmeye çalışalım;
isim = "alper"
isim = 'A' + isim[1:]
print(isim))

# Ama bunu yapmak istemeyebiliriz, o yüzden kolaylık için replace() metodu getirilmiş.
# Görelim;

isim = "alper"
isim = isim.replace('a','A')
print(isim)

# Gördüğünüz gibi küçük olan a harfinin büyük A harfine çevirdi.

# Farklı bir örnek vermek istiyorum;

soyisim = "aybak"
soyisim = soyisim.replace('a','A')
print(soyisim)

# Yukarıda yazmış olduğumuz kodun çıktısı AybAk olarak çıkıyor pek ya bunu nasıl düzeltiriz? Görelim;

soyisim = "aybak"
soyisim = soyisim.replace('ay', 'Ay')
print(soyisim)

# Gördüğünüz gibi çıktımız Aybak haline döndü.
# Fakat sıralamaya dikkat etmeniz gerekiyor. Ne demek istiyorum görelim;

 örnek = "tertemiz"
 örnek = örnek.replace("ter","Ter")
 print(örnek)

 # Gördüğünüz gibi aybak'ta ay kısmını almam yeterli olduk fakat tertemiz örneğinde ter kıısmını almak zorunda kaldım sebebi de şu arkadaşlar:
 # Eğer te kısmını alsaydım sadece çıktım TerTemiz olacaktı sadece baş harfi büyütmek istediğim için t harfinden sonraki harflere de bakıyorum aynı olan yerlere ek olarak farklı olan kelimeyi de ekliyorum.




 # lower() Metodu:
 # Bu metodun amacı karakter dizilerindeki büyük harfli elemanları küçük harfe çevirmektir
 # İsterseniz örnekle açıklayalım;

 aai = "ALPER AYBAK INDUSTRIES"
 aai = aai.lower()
 print(aai)

 # Bu şekilde olduğu gibi farklı şekilde de yazabiliriz görelim;

aai = "ALPER AYBAK INDUSTRIES"
print(aai.lover())

# İkisi de aynı kapıya çıkıyor istediğinizi kullanabilirsiniz.



# upper() Metodu:
# Bu metodun amacı karakter dizilerindeki küçük harfli elemanları büyük harfe çevirmektir
# İsterseniz örnekle açıklayalım;

aai = " alper aybak industries"
aai = aai.upper()

print(aai)

# Yine üstteki gibi diğer yöntemle yapabiliriz;

aai = " alper aybak industries"
print(aai.upper())



# islower() ve isupper() Metodu:
# lower ve upper metodunu işledik onlardan tek farkı bize bool veri tipi olarak dönüyor
# Yani true/false geri dönüşü alıyoruz isterseniz örnekle açıklayalım>;

print("alper aybak industries".islower()) #hepsi küçük harf anlamına geliyor o yüzden geri dönüş true.
print("Alper Aybak Industrıes".islower()) #hepsi küçük harf olmadığı için false geri dönüşü alıyoruz.

# Aynı şekilde isupper() metoduna bakalım;

print("AAI COMPANY".isupper()) #hepsi büyük harf anlamına geliyor o yüzden geri dönüş true.
print("AAI Company".isupper()) #hepsi büyük harf olmadığı için false geri dönüşü alıyoruz.




# endswitch() Metodu:
# Belki de programlama hayatınız boyunca hiç kullanmayacağınız bir metod ama göstermek istiyorum
# adından anlaşılacağı gibi sondaki karakterin ne olduğunu giriyoruz ve bize bool veri tipi olarak geri dönüs yapıyor (true/false)
# İsterseniz örnekle açıklayalım ne demek istediğimizi;

aybak = "Dünyanın Ötesinde Emin Ellerdesiniz"

print(aybak.endswith("z")) # Son karakter "z" olduğu için true sonucu aldık
print(aybak.endswith("a")) # Son karakter "a" olmadığı için false sonucu aldık




# startswitch() Metodu:
# endswitch() metodunun tersine baştaki karakterin ne olduğunu söylediğimiz zaman geri dönüşü bool veri tipi(true/false) ile aldığımız metoddur.
# İsterseniz örnekle açıklayalım ne demek istediğimizi;

dosya = "aaicompany.doc"

print(dosya.startswith("a"))
print(dosya.startswith("aaicompany"))

# Yukarıdaki örnekte veriler true olarak dönüş yaptı.
# İsterseniz tek karakter isterseniz de kelime sorgulayabilirsiniz.




# capitalize() Metodu:
# Herhangi bir karakter dizisinin ilk harfini büyütmek için kullanılır.
# replace() metodu gibi fakat buradaki avantajımız öge belirtmek zorunda değiliz direk ilk harfi büyütebiliriz
# İsterseniz örnekle devam edelim;

aybak = "hoşgeldiniz,burası AAI Company."

print(aybak.capitalize())

# Çıktımız => Hoşgeldiniz,burası aai company.
# Gördüğünüz gibi sadece ilk harfi büyüttük ve diğer harfler küçük kaldı



# title() Metodu:
# title başlık anlamına gelmektedir
# title() metodu ise başlıkları düzeltmemize yardımcı olur.
# Örnekle açıklayalım;

baslik = "alper aybak industries python programlama dersi"

print(baslik.title())

# Çıktımız ==> Alper Aybak Industries Python Programlama Dersi
# Gördüğünüz gibi çıktımız olması gerektiği başlık düzeninde oldu.



# swapcase() Metodu:
# Bu metodumuzla büyük ve küçük harfleri tam tersine çeviriyoruz
# İsterseniz örneğimize bakalım;

text = "aLPER aYBAK"

print(text.swapcase())

# Çıktımız ==> Alper Aybak 
# İsmimizi bu metod sayesinde düzelttik :)




# strip(), lstrip(), rstrip() Metodu:
# Yaptıkları iş aynı fakat işlem yönü farklı.
# Üst kısımda değinmiştik aslında ama isterseniz örnek üzerinde tekrar değinelim;

aybak = "AAI Company, Alper Aybak tarafından 2021 yılında kurulmuştur."

print(aybak.strip())
print(aybak.lstrip())
print(aybak.rstrip())

# #Çıktımız ==>AAI Company, Alper Aybak tarafından 2021 yılında kurulmuştur.
#              AAI Company, Alper Aybak tarafından 2021 yılında kurulmuştur.    
#                          AAI Company, Alper Aybak tarafından 2021 yılında kurulmuştur.

# split normal çıktı almamızı sağlıyor 
# lstrip (l=left(sol)) taraftaki boşlukları silmemizi sağlıyor
# rsplit (r=right(sağ)) sağ taraftaki boşlukları sildi

# strip metodlarında hangi gereksiz şeyler kırpılıyor isterseniz görelim;

# ''  Boşluk Karakteri
# \t  Sekme Kaçış Dizisi (TAB)
# \n Alt Satıra İnme Kaçış Dizisi 
# \r İmleci Satırın Başına Döndüren Kaçış Dizisi
# \v Düşey sekme Kaçış Dizisi
# \f Yeni Sayfa Kaçış Dizisi  

#! Bu 3 metod yukarıda açıkladıklarımı kırpmaya yarıyor 

# İsterseniz karakter dizilerini nasıl kırpıyoruz bunu da görelim;

aybak = "merhaba, AAI Company'e Hoşgeldiniz Size Nasıl Yardımcı Olabilirim"

print(aybak.strip("m")) # Her iki "m" harfini de kırptı
print(aybak.lstrip("m")) # sol taraftaki "m" harfini kırptı
print(aybak.rstrip("m")) # sağ taraftaki "m" harfini kırptı



# join() Metodu:
# split() metodu ile böldümüz karakterleri join() metodu ile birleştireceğiz 
# İsterseniz örnek üzerinde inceleyelim;

aybak = "Alper Aybak Yazılım AAI Company"
parcala = aybak.split(" ")

print(parcala)

# Çıktımız şu şekilde oldu ==> ['Alper', 'Aybak', 'Yazılım', 'AAI', 'Company']

parcala = ['Alper', 'Aybak', 'Yazılım', 'AAI', 'Company']
birlestir = " ".join(parcala)
print(birlestir)

# Göründüğü gibi join() metodu ile tekrar birleştirdik





# count() Metodu:
# Belki de karakter dizi metodlarından en çok kullanacağımız metoddur.
# Karakterin kaç defa tekrar ettiği bilgisini verir.

example = "alperaybakindustries"
print(example.count("a"))

# "a" harfinin 3 defa tekrar ettiğini gördük





# index(), rindex() Metodu:
# Daha önce işlediğimiz gibi index bize karakterlerin indeksini veriyor
# İsterseniz örneklerle inceleyelim;

isim = "aybak"
indeks  = isim.index("a")
print(indeks)

# Program bize gördüğünüz gibi 0 çıktısını verdi.
# Bir de şu örneğe baklalım;

isim = "alperaybak"
indeks  = isim.index("a")
print(indeks)

# Bu örnekte de 0 çıktısını aldım.
# Peki diğer verilere nasıl ulaşacağım? İşte bunun için sağdan saydırabiliriz ==> rindex() Metodu

isim = "alperaybak"
indeks  = isim.rindex("a")
print(indeks)

# rindex() sayesinde 8 indeksimiz olduğunu anlamış olduk  





# find(), rfind() Metodu:
# index() ve rindex() metoduna benziyor. Hatta yaptıklarıı iş tamamen aynı.
# Farkı şudur; index() ve rindex() metodları sonuç bulamazsa hata verir fakat find() ve rfind() "-1" çıktısını verir


aybak = "Merhaba, Alper Aybak Industrıes Sizin İçin Çalışıyor"

print(aybak.find("w"))

# Çıktımız ==> -1 
# Gördüğümüz gibi aybak karakter dizisinin içide "w" harfi olmadığı için -1 çıktısı aldık

# İsterseniz bunu index() ile de deneyip hata aldığımızı görelim;

aybak = "Merhaba, Alper Aybak Industrıes Sizin İçin Çalışıyor"

print(aybak.index("w"))

# Çıktımız hata verdi böylece ikisi arasındaki farkı anlamış olduğumuzu düşünüyorum.




# center() Metodu:
# Bu metod karakter dizilerini belli bir karakter aralığının ortasına getiriyor
# İsterseniz bir örnek verelim;

string = "AAI Company Python"
print(string.center(36))

# Çıktımız ==>          AAI Company Python
# Neden 36 yazdığımı merak etmişsinizdir. Sebebi şu;
# 18 karakterden oluşan bir stringimiz var ortalaması için 2 katı olan sayıyı girmemiz gerkiyor.
#! Karakter dizimiz kaç karakterden oluşuyorsa onun 2 katı center() Metodunun içine yazılır.

string = "AAI Company Python"
print(string.center(36,"-"))

# Çıktı ==> ---------AAI Company Python---------
# Gördüğünüz gibi bu sever de çizgilerle ortaladık
# İsterseniz nokta,virgül,#,/,* gibi karakter dizileri ile de ortalayabilğirsiniz.






# rjust(),ljust() Metodu:
# Bu metod center() metoduna benzemektedir.
# Ama bu metod karakter dizilerini ortalamak yerine ya sağa ya da sola yaslıyor.
# İsterseniz örnekle açıklayalım;

string = "Alper Aybak"
print(string.rjust(44), end="")

#Çıktımız ==>                                  Alper Aybak
# Gördüğünüz gibi sağ tarafa yaslanmış durumda.
# Aynı şekilde sol tarafa yaslamak içinse ljust() metodunu kullancağız.
# İsterseniz daha net örnek yapalım;

string = "AAI Company"
print(string.ljust(55,"-"),end="")
print("Şirketimize Hoşgeldiniz")

# Çıktımız ==> AAI Company--------------------------------------------Şirketimize Hoşgeldiniz
# Böyle çok daha iyi anlaşıldığından eminim.
# Dilerseniz siz de örnekler yapın ve iyice pekişsin.




# isalpha() Metodu:
# Alpha latin alfabesinin ilk harfidir.
# Alfabe kelimesinin ilk kısmı olan "alfa" da oradan gelir.
# isalpha() metodu bir karakter dizisinin tamamen alfabe karakterlerinden olup olmadığını sorgular.
# Bool veri tipi ile dönüş yapar (true/false)
# İsterseniz örnek verelim;

aybak = "AA INDUSTRIES|alperaybakindustries"
print(aybak.isalpha())

# Çıktımız ==> False
#! False alma sebebimiz Alfabede boşluk diye bir karakter yoktur.
# İsterseniz tekrar örnek verelim;

aybak = "alperaybakindustries"
print(aybak.isalpha())

# Çıktı ==> True
# Gördüğümüz gibi çıktımız True.



# isdigit() Metodu:
# Bu metod bir önceki metodumuzun tam tersi diyebiliriz.
#! isdigit() metodundaki karakterler tamamen sayısal ifadelerden oluşmalıdır
# İsterseniz örnek verelim;

kod = "BirİkiÜç"
print(kod.isdigit())

# Çıktı ==> False
# İfademizde sayısal değer yoktu bir de şu kod örneğine bakalım;

kod = "0123456789"
print(kod.isdigit())

# Çıktı ==> True
# Görüldüğü üzere karakter dizisi sayısal ifadeler içerdiği için true çıktısını aldık.




# isalnum() Metodu:
# Bu metod hem alfabetik hem de sayısal olduğunu kontrol eder.
# Yani karakter dizisinde alfabedeki karakterler, sayısal karakterler veya her ikisi birden varsa bize True çıktısını verir.
# İsterseniz örnekle açıklayalım;

aa1 = "112131"
aa2 = "alperaybak"
aa3 = "alperaybak11"
aa4 = "alper>><<x!'+"

print(aa1.isalnum())
print(aa2.isalnum())
print(aa3.isalnum())
print(aa4.isalnum())

# # Çıktımız ==> True
#                True
#                True
#                False



# isdecimal() Metodu:
# Karakter dizisinin ondalık sayı cinsinden olup olmadığını sorgulayabiliyoruz.
# Bool veri tipine(true/false) göre çıktı veriyor.
#! Fakat sayı tipimiz Integer ise true, eğer Float ise false çıktısını alıyoruz
# Örneğe bakalım;

aa1 = "111"
aa2 = "11.1206"

print(aa1.isdecimal())
print(aa2.isdecimal())

# Çıktımız ==> True
#              False

# Gördüğümüz üzere dediğimiz çıktıları aldık.
# Atladığım herhangi bir metod varsa  .metod şeklinde yaptığımız gibi yapabilirsiniz.
# Sıkıntı olursa yine iletişime geçebilirsiniz.
# Bu dersimizin de sonuna gelmiş bulunuyoruz. Biliyorum baya uzun bir ders oldu isterseniz bunları güzelce sindirelim daha sonraki derse öyle geçelim.
# Görüşmek üzere.
