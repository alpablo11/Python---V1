 # AAI Company - Python

 # Liste Veri Tipi

# Liste verisi derken aslında tam olarak da listeden bahsediyoruz.
# Python'da  bu listeler ne yaoıyor peki?
# Örneğin bir alışveriş sepeti düşünün sepet bizim listemiz olsun. Biz sepetimize ürün ekleyip, çıkartabiliriz.
# Veya alacağımız ürünün sayısını arttırabiliriz. Sepetteki ürünleri evimize veya başka adrese götürebiliriz.
# İşte aynı şekilde günlük hayatta yaptığınız listeler veya düşüncelerle aynı işleri Python'da yapıyor.



# Eğer başka bir programlama dili biliyorsanız dizi ifadesini duymuşsunuzdur.
# Listeler, dizilere benzemekte fakat listeler dizilerden daha gelişmiştir.
# Eğer bilmiyorsanız da sorun değil ne demek istediğimi açıklayayım;
# Dizilerde tek bir veri tipi barındırabiliriz. Ama listelerde istediğimiz kadar veri tipi barındırabiliriz.

# Eğer biz bir liste tanımlamak istersek ne yapıyoruz görelim;

bos_liste = list[]
# Bu list[] değerini atıyarak, liste oluşmasını isatedik.

# Yalnızca bir eleman tanımlamak istersek ne yapıyoryuz? Görelim;
liste = ["AAI Company"]
 
# Birden çok eleman olmasını istersek de virgüller ile ayırıyoruz görelim;
programlama_dilleri  =["Python","C","C++","Java","JavaScript","HTML5","CSS3","PHP"]

# Listelerimiz tabiki de sadece stringlerden oluşmuyor, başka karakterler de ekleyebiliriz.

company = ["alper","aybak",11,"yazılım",21,2]

#! Listeler içlerinde her türlü veri tipini tutabilir ve listeler değiştirilebilir veri tipidir.


# Değiştirilebilir ve Değiştirilemeyen Veri Tipleri
# Değiştirilebilir üzerinden gidersek daha anlaşılır olacaktır. Bir örnek verelim isterseniz;

n = "Alper Aybak"
print(n)
n = "AAI Company"
print(n)

# Burada durum Python için n yeniden atanmıştır, fakat listeler de değişim söz konusudur.
# Peki bu nasıl teyit edilir? id() Metodunu kullanmak bu sorulara cevap verecektir;

n = "Alper Aybak"
print(id(n))
n = "AAI Company"
print(id(n))

# Çıktımız:
# 52062232
# 52062152

# Görüldüğü üzere farklı sonuçlar aldık n yeniden tanımlanmış oldu fakat id() Metodunu bir de listeler de uygulayalım;

liste = [1,2,3,4,5,6,7,8,9,0]
print(liste)
print(id(liste))

liste.append("Alper Aybak") # .append() ==> listeye veri eklemek için kullanılır (işleyeceğiz)
print(liste)
print(id(liste))

# Çıktımız:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 48553576
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'Alper Aybak']
# 48553576

# Gördüğünüz gibi listeler değiştirilebilir veri tipiyken Integer,Float ve String değiştirilemeyen veri tipidir.



# Listelerin Kullanımı
# -Liste Tanımlama:
# Boş bir liste tanımlamak için list() metodu kullanılır. Görelim;

Company = list()
print(Company)

#Çıktımız ==> []
# Çıktımız köşeli parantez olarak geldi yani köşeli parantez demek liste anlamına gelir.

# Bir de şu örneğe bakalım;

company = list("alperaybakindustries")
print(company)

# Çıktımız ==>  ['a', 'l', 'p', 'e', 'r', 'a', 'y', 'b', 'a', 'k', 'i', 'n', 'd', 'u', 's', 't', 'r', 'i', 'e', 's']

# Gördüğünüz gibi alperaybakindustries dizisinin her öğesi liste haline geldi

# İsterseniz örneklerle devam edelim;

company = ("Alper Aybak","Yazılım","Endüstri","AAI","Aybak Holding")
liste = list(company)
print(liste)

# Çıktımız ==> ['Alper Aybak', 'Yazılım', 'Endüstri', 'AAI', 'Aybak Holding']


for i in range (11):
    print(i)
# Yukarıdaki kodumuzu listeye dönüştürelim isterseniz

liste = list(range(11))
print(liste)

# Çıktımız ==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]





#! Liste Verilerine Erişme:
# Listelerde herhangi bir veriye ulaşmak için ne yapmamız gerekiyor?
# Örneğin binlerece satırlık bir liste var diyelim bu listeden 11.verinin önemli olduğunu öğrendik bunu nasıl öğrenebiliriz?
# İsterseniz örneklerle öğrenelim;

calisan1 = ("Alper Aybak","Yazılım",18)
calisan2 = ("Hüseyincan Bağcı","Finans",19)
calisan3 = ("Tom","Endustri",23)
calisan4 = ("Tony","Mühendislik",30)
calisan4 = ("Chris","Uzay Bilimi",27)

aai_company = [calisan1,calisan2,calisan3,calisan4]

print(aai_company)
# Yazılım dillerde sayma sıfırdan başlayarak devam eder.
# Sırayla öğrenmek istediğimiz çalışanları görelim.

print(aai_company[0]) # Görüldüğü üzere 1.olarak adlandırdığımız eleman 0'a karşılık geldi
print(aai_company[1])
print(aai_company[2])
print(aai_company[3])

# Gördüğümüz gibi liste adımız ve köşeli parantez ile elemanlarımızı öğrenebiliyoruz.

# Bir de şu örneğe bakalım;

liste = ["alper","aybak","industries","company"]
print(liste[3][5])
# Çıktımız ==> n

# Bu sefer ise yaptığımız işlem şu şekilde;
# listenin içerisindeki 3.karakter dizisini al (company) ve 3.karakter dizisinin 5.indeksini bize yazdır.


#! Listeye Eleman Ekleme:
# Örneğin liste oluşturduk ve daha sonra eklememiz gereken veriyi unuttuğumuzu fark ettik.
# İşte bu işlemi kolay hale getirmek için bir metodumuz var ==> .append()
# İsterseniz örnekle görelim;

programlama_dilleri = ["Python","C","C++","JavaScript","Java","CSS3","HTML5"]
print(programlama_dilleri)

programlama_dilleri.append("Php")
print(programlama_dilleri)

# Çıktımız :
# ['Python', 'C', 'C++', 'JavaScript', 'Java', 'CSS3', 'HTML5']
# ['Python', 'C', 'C++', 'JavaScript', 'Java', 'CSS3', 'HTML5', 'Php']


#! Listeden Eleman Çıkarma:
# Listeye eleman eklediğimiz gibi istediğimiz elemanı da çıkarabiliriz. Görelim;

programlama_dilleri = ["Python","C","C++","JavaScript","Java","CSS3","HTML5","Php","Fransızca"]
print(programlama_dilleri)

# Gördüğünüz gibi Fransızca programlama dili değil ve çıkarmak istiyorum bunun içi kullanacağımız metod ==> .remove()

programlama_dilleri = ["Python","C","C++","JavaScript","Java","CSS3","HTML5","Php","Fransızca"]
programlama_dilleri.remove("Fransızca")
print(programlama_dilleri)

# Çıktılarımız :

# ['Python', 'C', 'C++', 'JavaScript', 'Java', 'CSS3', 'HTML5', 'Php', 'Fransızca']
# ['Python', 'C', 'C++', 'JavaScript', 'Java', 'CSS3', 'HTML5', 'Php']

# .remove() metodu ile listeden eleman silebildiğimiz gibi pop() metodu ile de yapabiliriz bunu görelim;

programlama_dilleri = ["Python","C","C++","JavaScript","Java","CSS3","HTML5","Php","Fransızca"]
programlama_dilleri.pop()
print(programlama_dilleri)

# Çıktımız ==> ['Python', 'C', 'C++', 'JavaScript', 'Java', 'CSS3', 'HTML5', 'Php']

# Tekrar deneyelim isterseniz;
programlama_dilleri = ['Python', 'C', 'C++', 'JavaScript', 'Java', 'CSS3', 'HTML5', 'Php']
programlama_dilleri.pop()
print(programlama_dilleri)

# Çıktımız ==> ['Python', 'C', 'C++', 'JavaScript', 'Java', 'CSS3', 'HTML5']
# Gördüğümüz gibi pop() metodu sondaki elemanı siliyor sadece.


# Fakat hangi sıradakini silmek istediğimizi remove ile kısayoldan belirtebiliriz. Görelim;

programlama_dilleri = ['Python', 'C', 'C++', 'JavaScript', 'Java', 'CSS3', 'HTML5']
programlama_dilleri.remove(programlama_dilleri[-3])
print(programlama_dilleri)

# Çıktımız ==> ['Python', 'C', 'C++', 'JavaScript', 'CSS3', 'HTML5']
# [-3]  demek sondan 3.yü sil anlamına gelir. (Java)


# Listelerin Metodları:
# Önceki derslerimizde hatırlarsanız dir() metodu ile karakter dizilerinin tamamını öğrenmiştik.
# Burada da alt tre bulunduranlar işimize yaramayacak o yüzden şöyle bir kod yazalım ve çıktısını görelim;

for i in dir(list()):
    if '__' not in i:
        print(i)

# append
# clear
# copy
# count
# extend
# index
# insert
# pop
# remove
# reverse
# sort

# Liste Metodlarımız Bu şekilde append,pop ve reverse metodunu gördük.
# Dilerseniz diğer metodları da tek tek inceleyelim...


#! index() Metodu:
# Aslında karakter dizilerinden aşina olduğumuz bir konu ne iş yapıyorlardı yine de hatırlayalım isterseniz;
# Bir öğenin içinde bulunduğu karakter dizisinin ya da listenin içindeki konumu(adresi)'dir.
# İsterseniz örneğe geçelim;

company = ["Yazılım","Web Geliştirme/Tasarlama","Oyun Geliştirme","BOM GYM","Siber Güvenlik"]
print(company.index("BOM GYM"))

# Çıktımız ==> 3
# Görüyoruz ki BOM GYM 3.indekste yer alıyor.


company = ["Yazılım","Web Geliştirme/Tasarlama","Oyun Geliştirme","BOM GYM","Siber Güvenlik"]
new_company = list() # [] şeklinde de yazabiliriz.
#Devam edelim;

for i in company:
    indeks = company.index(i)
    if indeks%2==0:
        new_company.append(i)

print(new_company)

# Çıktımız ==> ['Yazılım', 'Oyun Geliştirme', 'Siber Güvenlik']
# Ne yaptığımızı anlamayanlar için veya anlayanlar için tekrar amaçlı açıklayayım;
# company değerini i ye atadım ve koşul durumu oluşturdum. Karakter sayısı 2'ye bölününce 0 kalanları new_company listesine eklemesini (append() ile) söyledim. Ve çıktımızı yazdırdım.


#! count() Metodu:
# Yine dizilerde kullandığımız count() metodu ile beraberiz. Hatırlayalım;
#  Sıralı verilerimizde bir ögenin kaç defa yer aldığını verir.
# İsterseniz örnek ile açıklayalım;

rastgele_sayiar = [11,2432,44535,6,67,11,52,334,56,3,4,355,11,67,534,56,575,341231,56543,11,345,12,11]
print(rastgele_sayiar.count(11))

# Çıktımız ==> 5
# Demek ki 11 sayısı listemizde 5 defa yer alıyormuş.

#! extedn() Metodu:
# İki listeyi birleştirmek için kullandığımız metoddur.
# Örnek ile açıklayalım dilerseniz;

company_left = ["Software","Developers","Secrutiry","Series","Movies","Games","Design","Engineering","Industries"] 
company_right = ["Alper","Aybak","Hüseyincan","Bağcı","Finans","Hukuk","Auto"]

company_left.extend(company_right)
print(company_left)

# Çıktımız ==> ['Software', 'Developers', 'Secrutiry', 'Series', 'Movies', 'Games', 'Design', 'Engineering', 'Industries', 'Alper', 'Aybak', 'Hüseyincan', 'Bağcı', 'Finans', 'Hukuk', 'Auto']
# Gördüğünüz gibi listemizi birleştirdik.
# Dilerseniz alt alta nasıl sıralayacağız görelim;

company_left = ["Software","Developers","Secrutiry","Series","Movies","Games","Design","Engineering","Industries"] 
company_right = ["Alper","Aybak","Hüseyincan","Bağcı","Finans","Hukuk","Auto"]

company_left.extend(company_right)
for i in company_left:
    print(i)

# # Çıktımız :
# Software
# Developers
# Secrutiry
# Series
# Movies
# Games
# Design
# Engineering
# Industries
# Alper
# Aybak
# Hüseyincan
# Bağcı
# Finans
# Hukuk
# Auto


#! reverse() Metodu:
# Listeleri tam tersine çevirmek için kullanılır.
# Örnek ile açıklayalım;

rakamlar = [0,1,2,3,4,5,6,7,8,9,]
print(rakamlar)

rakamlar.reverse()
print(rakamlar)

# # Çıktılarımız:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



#! sort() Metodu:
# Karakterleri alfabetik şekilde sıralamamızı sağlar.
# İsterseniz örnekle görelim;

kelimeler = ["Dahi","Playboy","Amerikalı Vatansever","Zampara","Miyoner",]
kelimeler.sort()
print("A-Z'ye Sıralama:",end=" ")
print(kelimeler)

# Çıktımız ==> A-Z'ye Sıralama: ['Amerikalı Vatansever', 'Dahi', 'Miyoner', 'Playboy', 'Zampara']

# reverse() metodumuzda stringler geçerli değil fakat sort() metodunda sayılar mevcut görelim;

sayilar = [242,42342,5566,7,6,435434,67,4342,1,465,11,21,0]
sayilar.sort()
print(sayilar)

# Çıktımız ==> [0, 1, 6, 7, 11, 21, 67, 242, 465, 4342, 5566, 42342, 435434]

# Gördüğünüz gibi herhangi bir işlemi alfabetik sıraya koymak istersek sort() metodunu kullanmalıyız.



#! copy() Metodu:
# İsminden de anlaşılacağı gibi listemizi kopyalamamıza yarıyor.
# İsterseniz görelim neler yapıyormuş;

n = ["ALper","Aybak","N Kişisi"]
a = n.copy()
n.append("Audi R8")

print(a)
print(n)

# # Çıktılarımız ==> 
# ['ALper', 'Aybak', 'N Kişisi']
# ['ALper', 'Aybak', 'N Kişisi', 'Audi R8']

# a'ya baktığımız zaman n listesini kopyaladı fakat daha sonra n listesine eklediğimiz elemanı göremedik.
# Yani copy() metodu kopyalandıktan sonra değişiklik yapıldığı ile ilgilenmez, kopyalanan andaki kısmı baz alır.




#! clear() Metodu:  
# Bir listenin içeriğini temizlemek için kullanılır.
# İsterseniz örnek ile görelim;

n = [11,21,31,41,51,61,71,111]
print(n)
n.clear()
print(n)

# Çıktılarımız ==>
# [11, 21, 31, 41, 51, 61, 71, 111]
# []



# Evet arkadaşlar liste veri tipleri konumuzun sonuna geldik. Elimden geldiğince açıklamaya çalıştım. Aklınıza herhangi bir şey takılırsa iletişime geçebilirsiniz.
# Diğer dersimizde demet veri tiplerini göreceğiz, diğer derste görüşmek üzere....

