# AAI Company - Python

#! İleri Düzey Fonksiyonlar:
# Burada iki adet başlık göreceğiz ilk olarak "Lambda Fonksiyonları" daha sonra da "Recursive Fonksiyonlar"
# İsterseniz çok uzatmadan geçelim;



#! Lambda Fonksiyonları:
# Eğer ki yazacağımız fonksiyon çok fazla kod içermiyor, yalnızca verilen paramtrelere göre matematiksel sonucu döndürüyorsa normal fonksiyon yerine lambda fonksiyonunu kullanmak daha avantajlıdır.
# Normal fonksiyonlara göre daha hızlı çalışır.
# Fonksiyon tanımlarken def metodunu kullanıyorken lamda'da şöyle tanımlıyoruz;

kare = lambda x:x*x

# Parametre değerini veriyoruz (x gibi)
# İki nokta ifadesinden sonra fonksiyonun return edeceği değeri giriyoruz.

# Örneğe bakalım (Çift Sayıları Bastırma);

dizi = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(list(filter( lambda x: x %2 == 0, dizi )))

# Çıktımız ==> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Bir sayı dizisi oluşturduk ardından liste şekl,inde bastırmak istedik ve çift olanları filtrele komutu verdik filter() ile
# lambda fonksiyonumuzu da girerek bastırdık.








#! Recursive Fonksiyonlar:
# Fonksiyonlarda uyguladığımız ve daha sonrasında çağırdığımız klasik fonksiyonlardır.
#! 'def' şeklinde olanlar

# Örnek yapalım dilerseniz;

def fibo(n:int):
    if (n == 1 or n == 2):
        return 1

    else: 
        return fibo(n-1) + fibo(n-2)

dizi = list()

for i in range(11):
    dizi.append(fibo(i+1))


print(dizi)

# Çıktımız ==> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Fibonaccii sayısının ilk 11 satırını yadırdık.



# Şu örneğe bakalım bir de;

def aai():
    print("AAI Company' e İlk Adımızı Hoşgeldiniz...")

aai()

# Çıktımız ==> AAI Company' e İlk Adımızı Hoşgeldiniz...
# Fonksiyon parametresinden çıkıp tanımladığım fonksiyonu çağırdım ve fonksiyonun içi çıktı olarak karşıma çıktı.




# Evet arkadaşlar ileri derece fonksiyonlar bu şekilde. 
# Elimden geldiğince açık olmaya çalıştım. Aslında Lambda Fonksiyonlarını öğrenmiş olduk diğerleri bildiklerimizdi.
# Anlaşılmayan bir yer olursa iletişime geçebilirsiniz.
# Diğer dersimizde görüşmek üzere...