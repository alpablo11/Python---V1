# AAI Company - Python

# Sözlük Veri Tipi:
# Sözlük Veri Tipi derken aslında tam olarak sözlükten bahsediyoruz.
# Örneğin ingilizce - türkçe sözlük düşünelim;
# Genius'un karşılığı dahi demektir. Biz buna anahtar-değer ilişkisi diyoruz.
 


# Sözlüklerin Kullanımı:
# Sçzlük belirteçleri süslü parantezlerdir {}.
# Süslü parantezler sadece sözlüklere ait değildir daha sonra göreceğimiz kümeler konusuna da aittir.
# Fakat tanımlanma şekilleri farklı olduğu için sorun yaşanmıyor

# Boş bir sözlük oluşturarak başlayalım dilerseniz;

sozluk = {}
print(type(sozluk))  # type ==> Ait olduğu sınıfı gösterir (tipini)

# Çıktımız ==> <class 'dict'> 
#! dict ifadesi dictionary (sözlük) kelimesinin kısaltmasıdır.

# Boş bir sözlük oluşturmak için şu yöntem de kullanılabilir;

sozluk = dict()
print(type(sozluk))

# Çıktımız ==> <class 'dict'> 

#! Liste için ==> list(), Demet için ==> tuple(), Sözlük için ==> dict()

# İsterseniz bir sözlük oluşturarak örnek verelim;

sozluk = {
    "genius" : "dahi",
    "industries" : "endüstri",
    "computer" : "bilgisayar",
    "software" : "yazılım",
    "company" : "şirket",
    "iron" : "demir",
    "printer" : "yazıcı"
    
}

print(sozluk)

# Çıktımız ==> {'genius': 'dahi', 'industries': 'endüstri', 'computer': 'bilgisayar', 'software': 'yazılım', 'company': 'şirket', 'iron': 'demir', 'printer': 'yazıcı'}

#! Sözlüklerin Ögelerine Erişmek:
# Tıpkı listeler gibi içlerinde bir çok veri tutabilirler.
# Ve tıpkı listelerdeki gibi erişim sağlıyoruz isterseniz örnekle netleştirelim;

sozluk = {
    "genius" : "dahi",
    "industries" : "endüstri",
    "computer" : "bilgisayar",
    "software" : "yazılım",
    "company" : "şirket",
    "iron" : "demir",
    "printer" : "yazıcı"
    
}

print(sozluk[0])

# # Çıktımız ==> 
# Traceback (most recent call last):
#     print(sozluk[0])
# KeyError: 0

# Gördüğümüz gibi hata aldık.
# Yapmamız gereken şey aynı sözlük kullanır gibi bir öge aramak görelim;


sozluk = {
    "genius" : "dahi",
    "industries" : "endüstri",
    "computer" : "bilgisayar",
    "software" : "yazılım",
    "company" : "şirket",
    "iron" : "demir",
    "printer" : "yazıcı"
    
}

print(sozluk["genius"])

# Çıktımız ==> dahi

# Gördüğünüz gibi aradığımız ögeyi belirtmemiz gerekiyor.


#! Sözlüklerin Metodları:
# Daha önce de yaptığımız gibi "__" almadan dir() fonksiyonu ile metodları öğreneceğiz.
# Görelim;

sozluk = {}
for i in dir(sozluk):
    if "__" not in i:
        print(i)

# Çıktılar:

# clear
# copy
# fromkeys
# get
# items
# keys
# pop
# popitem
# setdefault
# update
# values

# İsterseniz daha önce yaptığımız gibi bunları tek tek ele alalım;

#! keys() Metodu:
# Anahtarlar anlamına gelir. 
# Ancak anahtarların liste mi demet mi ya da sıralı veya sırasız nasıl döneceğini bilmiyoruz. 
# İsterseniz test edip görelim;

aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}

print(aai_company.keys())

# Çıktımız ==> dict_keys(['alper', 'hüseyin', 'tony'])
# Görüldüğü gibi veri tipimiz dict_keys' imiş.
# Devam edelim;

aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}

print(aai_company.keys()[0])

# # Çıktımız:
# Traceback (most recent call last):
#     print(aai_company.keys()[0])
# TypeError: 'dict_keys' object is not subscriptable

#! Anladığımız kadarıyla sözlükler sıralı veri tipleri değilmiş.

# Peki sözlükleri sıralı veri tipine çevirebilir miyiz görelim;


aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}
company = list(aai_company.keys())
print(company)

# Çıktımız ==> ['alper', 'hüseyin', 'tony']
# Gördüğümüz gibi sıralı veri tiplerine dönüşebiliyor.


# İstersek for döngüsü ile de sıralayabiliriz. Görelim;


aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}
for i in aai_company.keys():
    print(i)

# Çıktımız :
# alper
# hüseyin
# tony


#! get() Metodu:
# Sözlüklerde sorgu yaparken kullanacağımız metoddur.
# İsterseniz görelim;

aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}

print(aai_company.get("alper"))

# Çıktımız ==> yazılım
# sözlükte alperin karşılığı olduğu için çıktımızı verdi isterseniz bir de şunu deneyelim;

print(aai_company.get("chris"))

# Çıktımız ==> None
# Gördüğümüz gibi chris ögesini bulamadığı için None çıktısı aldık.



#! copy() Metodu:
# Daha önceden görmüş olduğumuz bir metod 
# Adından da anlaşıldığı gibi kopyalama işlemi yapıyor. Görelim;

aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}

na = aai_company.copy()

# İsterseniz id'lerine bakalım daha önce yaptığımız gibi;

print(id(na))
print(id(aai_company))

# Çıktılar 
# 52586488
# 52586408
# Baktığımız zaman son iki(2) hanesi farklı bu da bize şu sonucu veriyor sadece hafıza bölmeleri farklı


#! clear() Metodu:
# Yine listelerden aklımıza gelen bir metoddur ve aynı işlevi yapar.
# Sözlükleri temizlememizi sağlar. Görelim;

aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}

aai_company.clear()
print(aai_company)

# Çıktımız ==> {}



#! pop() Metodu:
# pop() Metodu sözlükten bir ögeyi silmek için kullanılır.
# Görelim;

aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}

aai_company.pop("tony")
print(aai_company)

# Çıktımız ==> {'alper': 'yazılım', 'hüseyin': 'finans'}



#! popitem() Metodu:
# Aynı pop() metodu gibi çalışır.
# Fakat bir fark vardır popitem() sözlükteki son ögeyi siler.
# Görelim;

aai_company = {
    "alper" : "yazılım",
    "hüseyin" : "finans",
    "tony" : "elektrik"
}

print(aai_company)
aai_company.popitem()
print(aai_company)

# Çıktılarımız :
# {'alper': 'yazılım', 'hüseyin': 'finans', 'tony': 'elektrik'}
# {'alper': 'yazılım', 'hüseyin': 'finans'}

# İkinci print fonksiyonu ile bunu ispatladık!


#! setdefault() Metodu:
# Sözlüğe yeni öge eklemek için kullanılır.
# İki farklı yöntem göreceğiz.
# İsterseniz görelim;

sozluk = {"sofware" : "yazılım"}
sozluk["developer"] = "geliştirici"
print(sozluk["developer"])

# Çıktımız ==> geliştirici

# şimdi de setdefault() metodumuzu kullanalım;

sozluk = {"sofware" : "yazılım"}
sozluk.setdefault("developer","geliştirici")
print(sozluk.get("developer"))

# Çıktımız ==> geliştirici
# İstediğimiz metodu kullanabiliriz size kalmış bir şey.


#! update() Metodu:
# Sözlüklerin tüm değerlerini güncelleyeceğimiz zaman kullanırız.
# Görelim;

aai_company_maaslar ={
    "yazılımcı" : 20000,
    "geliştirici" : 15000,
    "avukat" : 15000,
    "mühendis" : 30000,
}

aai_company_zamlı = {
    "yazılımcı" : 25000,
    "geliştirici" : 20000,
    "avukat" : 30000,
    "mühendis" : 40000,

}

aai_company_maaslar.update(aai_company_zamlı)
print(aai_company_maaslar)

# Çıktımız ==> {'yazılımcı': 25000, 'geliştirici': 20000, 'avukat': 30000, 'mühendis': 40000}

# Gördüğümüz gibi güncellemiş olduk maaşlarımızı


#! items() Metodu:
# Sadece anahtar veya değer değil de, hem anahtar hem değere ulaşmak istiyorsak kullanıyoruz.
# Görelim;

sozluk = {
    "genius" : "dahi",
    "industries" : "endüstri",
    "computer" : "bilgisayar",
    "software" : "yazılım",
    "company" : "şirket",
    "iron" : "demir",
    "printer" : "yazıcı"
    
}

print(sozluk.items())

# Çıktımız ==> dict_items([('genius', 'dahi'), ('industries', 'endüstri'), ('computer', 'bilgisayar'), ('software', 'yazılım'), ('company', 'şirket'), ('iron', 'demir'), ('printer', 'yazıcı')])



#! values() Metodu:
# keys() metodu ile tüm anahtarları çekiyorduk
# values() metodu ile tüm değerleri çekiyoruz görelim;

sozluk = {
    "genius" : "dahi",
    "industries" : "endüstri",
    "computer" : "bilgisayar",
    "software" : "yazılım",
    "company" : "şirket",
    "iron" : "demir",
    "printer" : "yazıcı"
    
}

print(sozluk.values())

# Çıktımız ==> dict_values(['dahi', 'endüstri', 'bilgisayar', 'yazılım', 'şirket', 'demir', 'yazıcı'])


#! fromkeys() Metodu:
# Sözlük metodu olsa da sözlüğe bir etkisi olmayan metoddur.
# Yalnızca yeni sözcük üretmek için kullanılır.
# Birden fazla sözcük alır fakat tek bir deeğer koyar (yani her sözcük karşılığı aynı)
# Görelim;

aaiCompany_ürünler = "Yazılım Eğitimi" , "Web Geliştirme Eğitimi", "Android Oyun Geliştirme"
fiyat = " 200 TL"

sozluk = dict.fromkeys(aaiCompany_ürünler,fiyat)
print(sozluk)

# Çıktımız ==> {'Yazılım Eğitimi': ' 200 TL', 'Web Geliştirme Eğitimi': ' 200 TL', 'Android Oyun Geliştirme': ' 200 TL'}

#! Sözlük Üreteçleri:
# Sözlüklerdeki son konumuza gelmiş bulunuyoruz.
# Liste üreteçlerini görmüştük daha önce benzer bir yöntemdir.
# Liste üreteçleri nasıl liste üretiyorsa, sözlük üreteçleri de sözlük üretiyor
# İsterseniz örnekle netleştirelim;

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
kelime = input("Kelime Giriniz: ")

sozluk = {i : alfabe.index(i) for i in kelime}

print(sozluk)

# Çıktımız ==> 
# Kelime Giriniz: aybak
# {'a': 0, 'y': 27, 'b': 1, 'k': 13}





# Evet arkadaşlar sözlük veri tipleri dersimizin sonuna geldik.
# Aklınıza takılan herhangi bir şey olursa iletişime geçebilirsiniz.
# Sonraki derste rehber uygulaması yapacağız. Sözlükler konusu tam oturmadan geçmeyelim lütfen
# Görüşmek üzere...