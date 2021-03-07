# AAI Company - Python 

#! Fonksiyonlarda İleri Seviye Konular

# Python'a ait son konumuza gelmiş bulunmaktayız.
# Ekstralar ve örnek programlarımız olacak elbette.
# Eksiksiz bir şekilde gelebildiysek anladıysak gerçekten ne mutlu bize ileri seviye Python biliyoruz demektir. Hem de gönül rahatlığı ile diyebiliriz :)
# Fazla uzatmadan konumuza geçelim isterseniz.


#! İç İçe Fonksiyonlar 
# Fonksiyonları nasıl tanımlarız fonksiyonlar neler yapabilir aslında bunları biliyoruz.
# Ama fonksiyonlar bizim işlediklerimizden çok daha fazlasını yapabilirler.
# Bu konuyu ise NTP içerisinde almak mantıklı çünkü fonksiyonları artık bir obje olarak öğreneceğiz
# Python'ın temelinde fonksiyonlar da birer obje ise aslında pobjenin sahip olduğu her şey birer fonksiyon anlamını çıkarabiliriz.
# Yani bir fonksiyonu istediğimiz değeri atayabilir ve dönüşümünü yapabiliriz isterseniz görelim;

def func(n,a):
    return sum((n,a))


na = func 
print(na(11,21))

# Çıktımız ==> 32
# Gördüğümüz gibi fonksiyonu çağırmadık ve değişkene atadık bu şekilde de toplamamızı yapabildik
#! sum ==> Toplama İşlemi


# Listeleri hatırlarsak, bir listeyi başka bir değişkene atadiığımız zaman bellekte yeni adresleme yapamıyorduk 
# Dilerseniz örnekle açıklayalım;

liste1 = [1,2,3,4,5,6,7,8,9,0]
liste2 = liste1

print("Liste 1 ID : ", id(liste1))
print("Liste 2 ID: ",id(liste2))

# Çıktımız ==> 
# Liste 1 ID :  23453320
# Liste 2 ID:  23453320

# Küçük bir hatırlatma yaptık.
# Bakalım aynısı fonksiyonlarda da olacak mı? Görelim;

def func(n,a):
    return sum((n,a))

na = func

print("na ID : ",id(na))
print("func ID :",id(func))

# Çıktımız ==>
# na ID :  21811960
# func ID : 21811960

# Görüldüğü gibi func değerini "na"ya atadığımız zaman bir değişiklik olmadığını görebiliyoruz.

# İsterseniz bir örnek kod yazıp çalıştıralım;


def func(islem):
    def toplama(*args):
        return sum(args)

    def cikarma (n,a):
        return n-a

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i

        return carpim

    
    def bolme(n,a):
        return n/a


    if islem == "toplama":
        return toplama

    elif islem == "cikarma":
        return cikarma

    elif islem == "carpma":
        return carpma

    elif islem == "bolme":
        return bolme


    else:
        print("Hatalı Tuşlama Yaptınız")
        return None



        
# Programımızı test edelim;

na = func("carpma")
print(na(3,4,10,11))

# Çıktımız ==> 1320
# *args anlaşılmamış olabilir aslında açılımı ==> Argümanlar
# Şimdi daha net oturacağına eminim
# Dİlerseniz konuya geçelim;


#! Sayısız Argüman Alabilme
# Yukarıda yazmış olduğumuz kodumuzda *args kullandık fakat ne işe yaradığını bilmiyoruz.
# Dönüp bakarsanız çarpma ve toplamada yapmış olduk bu işlemi
# Aslında olay şöyle kullanıcının kaç sayı gireceğini bilmediğimiz için sayısız argümanlara ihtiyaç duyarız.
# Benim çarpma işleminde 4 sayı yazdığım gibi.
# *args yazmanın bi önemi yok istersek argumanlar da yazabilirdik.
# Dilerseniz bu konuyla ilgili örneklere geçelim;

def func(*argumanlar):
    return argumanlar

print(func(11,21,2,12,2002))

# Çıktımız ==> (11, 21, 2, 12, 2002)


# Bunları sürekli demet üzerinde yapmamıza gerek yok bir string üzerinde de yapabiliriz.
# İşte tam bu noktada yani string veri tipinde yardım edecek fonksiyon;
#! **kwargs  (veya "**isimli_argumanlar" da olabilir )
# Örnek olarak görelim;

def func(**kwargs):
    return kwargs

print(func(username = "alperaybak", password = "AAICompany"))

# Çıktımız ==> {'username': 'alperaybak', 'password': 'AAICompany'}

#! Herhangi bir veri tipine ulaşmak için sözlük veri tipinde öğrendiklerimizi kullanabiliriz. Örneğin get() ile değer alalım;

def func(**kwargs):
    print("Kullanıcı Adı: ",kwargs.get("username"))
    print("Parola/Şifre: ",kwargs.get("password"))

func(username = "alperaybak", password = "AAICompany")

# Çıktılar :
# Kullanıcı Adı:  alperaybak
# Parola/Şifre:  AAICompany



#! Decorators
# Fonksiyonların bir obje olarak kullanılabilmesi sayesinde decarator(bezelyeci) oluşturabiliyoruz.
# Peki bu bezelyeler ne anlama geliyor?
# Fonksiyonlara ek özellik veren başka bir fonksiyondur.
# Birden fazla fonksiyona özellik tanımlayabilmemizi sağlar ve kullanılır.

# Örnek ile açıklayalım gelin;

def topla(liste):
    print(sum(liste))

def carp(liste):
    sonuc = 1
    for i in liste:
        sonuc *= i
    
    print(sonuc)

# Bu fonksiyon istediğimz gibi hazırda olmadığı için toplama ve çıkarmayı kendimiz yazdık.
# Yapmak istediğimiz kendi kendine işlem yapabilen bir kod. Görelim;

def frekans(func):
    def wrapper(liste):
        d = dict()
        for i in liste:
            d[i] = liste.count(i)

        max_ = 0
        key = 0

        for i in d.keys():
            if d.get(i) > max_:
                max_ = d.get(i)
                key = i

            
        print(f"Listede {key} sayısı en çok tekrar edendir.\nTekrar sayısı: {max_}")
        
        func(liste)
    
    return wrapper

# Karmaşık bir fonksiyon gibi gelebilir.
# Fonksiyonumuzun adı frekans(). Tekrar eden şeyler için kullanılan bir terimdir.
# Kendi içinde yeni bir fonksiyon tanımlanmış ==> wrapper() fonksiyonudur.
# Decorator konusunda yaygın isimleri bunlardır. Dilerseniz değiştirebilirsiniz fakat pek önerdiğim bir şey değildir.

# Şimdi bilgilerimiz oturduğuna göre decorator fonksiyonun asıl özelliklerini ekleyelim
# Devam edelim kodumuza;


def frekans(func):
    def wrapper(liste):
        d = dict()
        for i in liste:
            d[i] = liste.count(i)

        max_ = 0
        key = 0

        for i in d.keys():
            if d.get(i) > max_:
                max_ = d.get(i)
                key = i

            
        print(f"Listede {key} sayısı en çok tekrar edendir.\nTekrar sayısı: {max_}")
        
        func(liste)
    
    return wrapper

@frekans
def topla(liste):
    print(sum(liste))


@frekans 
def carp(liste):
    sonuc = 1
    for i in liste:
        sonuc *= i

    
    print(sonuc)

topla([11,32,552,23,4,98,11,56,11,56,21,12,11,121,67,11])

#! Geliştirmek istediğimiz fonksiyonun heme üzerine @ ile birlikte yazıyoruz.

# Çıktımız ==> 
# Listede 11 sayısı en çok tekrar edendir.
# Tekrar sayısı: 5
# 1097


# Evet arkadaşlar Ekstralar ve Örnek Uygulamalar hariç derslerimizin sonuna geldik.
# Son derste ve son konuda biraz fazla yüklenmiş olabilirim fakat biraz kafa yorduktan sonra anlaşılacağına eminim normal yaptıklarımızdan farkı @ işaretinin işlevini öğrendik.
# Anlamadığınız konu olursa iletişime geçebilirsiniz.
# Ekstralar ve Örnek Uygulamalarda görüşmek üzere....
