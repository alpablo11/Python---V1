# AAI Company - Python

#! Küme Veri Tipi
# Matematik dersinde öğrendiğimiz kümeler konusu ile tamamen alakalıdır. Yani kümelerin birleşimi veya kesişimi Python'da da sorgulanabilir.
# Sözlükler gibi sırasız veri tipleridir.


#! Kümelerin Kullanımı:
# Kümeleri anlatarak sizi de çok fazla sıkmak istemiyorum. O yüzden nasıl liste,demet veya sözlük oluuşturuyorsak, küme oluşturarak başlayalım dedim
# İsterseniz vakit kaybetmeden devam edelim;

kume = set()

# Sözlüklerde süslü parantez ifadesi hem kümelerde hem sözlüklerde kullanılıyor demiştik
# Fakat {} şeklinde bir değer atarsak bu python tarafından sözlük olarak algılanıyor.
# Yani boş bir küme set() ile tanımlanıyor.


#! Küme Metodları:
# isterseniz dir() fonksiyonumuzu tekrar çağıralım ve yine "__" olmasın;

kume = set()
for i in dir(kume):
    if "__" not in i:
        print(i)


# # Çıktımız :

# add
# clear
# copy
# difference
# difference_update
# discard
# intersection
# intersection_update
# isdisjoint
# issubset
# issuperset
# pop
# remove
# symmetric_difference
# symmetric_difference_update
# union
# update

# Önceki konularda yaptığımız gibi tek tek ele alalım isterseniz;

#! add() Metodu:
# Adından da anlaşılacağı gibi eklemek anlamına geliyor ve kümeye öge eklememizi sağlıyor.

kume = set() # Boş küme
kume.add(11)
kume.add("Alper Aybak")

print(kume)

# Çıktımız ==> {'Alper Aybak', 11}


#! clear() Metodu:
# Daha öğrendiğimiz metodlarla aynı işlevdedir.
# Kümeyi silmemizi sağlar. Görelim;

aybak = set()
aybak.add("Alper")
aybak.add(11)
aybak.add("Yazılım")
print(aybak)

aybak.clear()
print(aybak)

# Çıktılarımız:
# {11, 'Yazılım', 'Alper'}
# set()


#! copy() Metodu:
# Kümelerimizi kopyalamamızı sağlayan veri tipidir.
# Örnekle açıklayalım;

aybak = set() # boş küme
aybak.add("Alper")
aybak.add(11)
aybak.add("N")

aybak2 = aybak.copy()
aybak.clear()
print(aybak)
print(aybak2)

# Çıktılarımız =>
# set()
# {11, 'Alper', 'N'}



#! difference() Metodu:
# Difference => Fark anlamına gelir.
# İki farklı kümede ortak olmayan çıktıları bize verir
# İsterseniz görelim;

aybak1 = set("endüstri")
aybak2 = set("alper")
print(aybak1.difference(aybak2))

# Çıktımız ==> {'n', 's', 'i', 'd', 't', 'ü'}



#! difference_update() Metodu:
# difference() metodu ile aynı görevi yapmakta aslında yani oluşan fark kümesini yeni küme olarak tanımlar.

aybak1 = set("endüstri")
aybak2 = set("alper")
aybak1.difference_update(aybak2)

print(aybak1)

# Çıktımız ==> {'n', 't', 'ü', 'd', 'i', 's'}



#! intersection() Metodu:
# Kelime anlamı kesişimdir.
# İki kümedeki ortak ögeleri bulur.
# Görelim;

aybak1 = set("endüstri")
aybak2 = set("alper")

print(aybak1.intersection(aybak2))

# Çıktımız ==> {'e', 'r'}



#! intersection_update() Metodu:
# Kümelerin kesişimine güncelleme yapan metoddur.
# Görelim;

aybak1 = set("endüstri")
aybak2 = set("alper")
aybak1.intersection_update(aybak2)

print(aybak1)

# Çıktımız ==> {'r', 'e'}



#! isdisjoint() Metodu:
# Bu metodumuz ise iki kümenin kesişiminin boş olup olmadığını sorgular.
# Dilerseniz örneğe bakalım;

alper = set("emin ellerde")
aybak = set("dünyanın ötesinde")

if alper.isdisjoint(aybak):
    print("Kesişim Kümesi Boş Küme!")

else:
    print("Bu kümelerin ortak elemanı var")

# Çıktımız ==> Bu kümelerin ortak elemanı var




#! issubset() Metodu:
# Bize bool veri tipinde geri dönüş yaparlar.
# Bir küme diğerinin alt kümesi mi olduğunu sorguluyoruz.
# Görelim isterseniz;


alper = {1,2,3,4,6}
aybak = {1,2,3,4,5,6,7,8,9}
print(alper.issubset(aybak))

# Çıktı ==> True
# Yani alper kümesi aybak kümesinin alt kümesiymiş


#! issuperset() Metodu:
# Önceki metodumuzun tam tersi (kapsama işlemi yani) 
# Bir küme diğerinin üst kümesi mi onu kontrol ediyoruz
# Görelim;

alper = {1,2,3,4,6}
aybak = {1,2,3,4,5,6,7,8,9}

print(aybak.issuperset(alper))

# Çıktımız ==> True 
# aybak kümesi alper kümesini kapsadığı için çıktımız True


#! pop() Metodu:
# pop() Metoduna artık aşinayızdır.
# Kümedeki son elemanı siler.
# Dilerseniz örneğe bakalım;

alper_aybak = {1,2,3,4,5,67,8,9,0,11}
alper_aybak.pop()

print(alper_aybak)

# Çıktımız ==> {1, 2, 3, 4, 5, 67, 8, 9, 11}



#! remove() Metodu:
# Kümeden eleman silmek için kullanılır
# Fakat eğer kümede olmayan bir eleman yazarsak hata alırız görelim;

aybak = {1,2,3,4,5,67,8,9,0,11}

aybak.remove(67) # Sorunsuz çalışır
aybak.remove(21) # Hata verir



#! union() Metodu:
# İki kümeyi birleştirmemize yarıyor.
# Görelim;

A = {1,2,3,4,56,7,11,21,0}
N = {"n","a"}

print(A.union(N))

# Çıktımız ==> {1,2,3,4,56,7,11,21,0,"n","a"}




#! update() Metodu:
# Eğer bir listenin tamamını kümeye eklemek istiyorsak bu metodu kullanıyoruz.
# İsterseniz örnek verelim;

aai_urunler = {"Python Eğitim","C ve C++ Eğitimi","Web Geliştirme","Siber Güvenlik"}
yeni_urunler = ["İşletim Sistemleri","Oyun Geliştirme"]

aai_urunler.update(yeni_urunler)
print(aai_urunler)

# Çıktımız ==> {'C ve C++ Eğitimi', 'İşletim Sistemleri', 'Python Eğitim', 'Oyun Geliştirme', 'Siber Güvenlik', 'Web Geliştirme'}




#! symmetric_difference() Metodu:
# difference() metodu ile kümeler arası fark alabiliyoruz.
# Fakat bu farkı ayrı ayrı iki küme içinde alırsak toplamda farklı olan elemanlara erişmiş oluruz.
# Anlaşılmamış olabilir o yüzden geli örneğe bakalım;

n = {11,21,2,6,111,1321}
a = {21,111,1321,31,23}

print(n.symmetric_difference(a))

# Çıktımız ==> {2, 6, 23, 11, 31}
# Farklı elemanların hepsini bizim için bir küme haline getirdi.



#! symmetric_difference_update() Metodu:
# Bu metodumuz da objeyi güncellemek için kullanılır.
# İsterseniz örnekle açıklayalım;

n = {11,21,2,6,111,1321}
a = {21,111,1321,31,23}

n.symmetric_difference_update(a)
print(n)

# Çıktımız ==> {2, 6, 11, 23, 31}
# symmetric_difference() metodundan farklı olarak sıralamamıza yardımcı oldu aslında.




#! Dondurulmuş Kümeler:
# Eğer bir küme yapısının bozulmasını istemiyorsak dondurulmuş kümeleri kullanırız.
# Yani üzerinde değişiklik yapılamayan kümelerdir. 
# kullanacağımız fonksiyon ==> frozenset() 
# İsterseniz örnek yapalım;

NA = frozenset([11,6,2,12])

# Artık NA kümesi üzerinde değişiklik yapılamaz.
# Hatta bunu teyid etmek amaçlı NA kümesinin metodlarına bakalım;

NA = frozenset([11,6,2,12])

for i in dir(NA):
    if "__" not in i:
        print(i)

# # Çıktımız :
# copy
# difference
# intersection
# isdisjoint
# issubset
# issuperset
# symmetric_difference
# union

#! Gördüğümüz gibi NA kümesinde update() metodları yok. Bu güncelleme yapılamaz anlamına gelir.

# Evet arkadaşlar kümeler dersimizin sonuna geldik. 
# Elimden geldiği kadar açık olmaya çalıştım
# Eğer bir sorunuz veya anlamadığınız kısım varsa iletişime geçebilirisinz.
# Diğer dersimizde görüşmek üzere...
