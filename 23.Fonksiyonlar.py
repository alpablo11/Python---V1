# AAI Company - Python

#! FONKSİYONLAR













#! Fonksiyonun Tanımlanması ve Çağırılması:
# Fonksiyon tanımlayacağımız zaman kodumuza def ile başlarız.
# Ve fonksiyonu print ile değil adı ile çağırırız.
# İsterseniz örnekle pekiştirelim;

def alperaybakindustries():
    print("Alper Aybak\nYazılım\nElektrik-Elektronik Mühendisliği")

alperaybakindustries()

# # Çıktımız :
# Alper Aybak
# Yazılım
# Elektrik-Elektronik Mühendisliği

# Sanırım şimdi eksik kalan taşlar yerine oturmuştur.
# Örnekle devam edelim;

def aai_company():
    ad = "Alper Aybak"
    depertman = "Yazılım"
    maas = 100000
    print("İsim: {}\nDepertman: {}\nMaaş: {}".format(ad,depertman,maas))

aai_company()

# Çıktımız :
# İsim: Alper Aybak
# Depertman: Yazılım
# Maaş: 100000

# Biraz daha ilerieyelim ve örneklere devam edelim;
#! Belirli aralıkta girdiğimiz sayıları toplama kodu:

def topla(x:list):
    toplam = 0
    for i in x:
        toplam += i

    return toplam  # Fonksiyona geri dön anlamına gelir.

liste = [i for i in range(1,12)]

print(topla(liste))

# Çıktımız ==> 66
# İsterseniz kodumuzu açıklayalım;
# topla adında bir fonksiyon oluşturdum ("def" ile). Başlangıç olarak toplama 0 değerini verdim x'e i değerini atadım ve her severinde  toplam+i kadar artmasını istedim
# return parametresi ile toplama işlemine geri dondüm verilerimi girmek için liste oluşturdum. print içerisindeki topla() fonskiyonunu çağırdım ve yazdırdım.
# Sanırım şimdi tam anlamıya kafamıza oturmuştur.



# İsterseniz burada duralım ve diğer dersimizde daha da pekiştirmek için örnek uygulamalar yazalım. 
# Anlaşılmayan yerler olursa iletişime geçmeyi unutmayın
# Diğer derste görüşmek üzere...
