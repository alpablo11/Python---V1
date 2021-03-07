# AAI Company - Python

#! Rehber Uygulaması:
# Bir önceki derste işlediğimiz sözlük konusunu isterseniz uygulama yaparak daha da geliştirelim;





rehber = {}

while True:
    print("""
    
    [1] Sorgula
    [2] Kişi Ekle
    [3] Kişiyi Sil
    [Q] Çıkış
    
    """)

    secim = input("Lütfen İşlem Numarasını Tuşlayınız: ")

    if secim == "1":
        kisi = input("İsim: ")
        if kisi in rehber.keys():
            print(rehber.get(kisi))

        else:
            print("Aranan Kişi Rehberde Bulunamıyor !")

    
    elif secim == "2":
        kisi = input("İsim: ")
        numara = input("Numarası: ")
        rehber.setdefault(kisi,numara)

    

    elif secim == "3":
        kisi = input("Silinecek İsmi Giriniz: ")
        varmı = kisi in rehber.keys()

        if varmı:
            rehber.pop(kisi)

        else:
            print("{} kişisi rehberde yer almıyor !".format(kisi))

    
    elif (secim == "q" or secim =="Q"):
        break


    else: 
        print("Hatalı Giriş Yaptınız! Lütfen Tekrar Deneyiniz.")





# # Örnek Çıktı ==> 




#     [1] Sorgula
#     [2] Kişi Ekle
#     [3] Kişiyi Sil
#     [Q] Çıkış


# Lütfen İşlem Numarasını Tuşlayınız: 1
# İsim: Alper
# Aranan Kişi Rehberde Bulunamıyor !


#     [1] Sorgula
#     [2] Kişi Ekle
#     [3] Kişiyi Sil
#     [Q] Çıkış


# Lütfen İşlem Numarasını Tuşlayınız: 2
# İsim: Alper Aybak
# Numarası: 536xxxxxxx


#     [1] Sorgula
#     [2] Kişi Ekle
#     [3] Kişiyi Sil
#     [Q] Çıkış


# Lütfen İşlem Numarasını Tuşlayınız: 1
# İsim: Alper Aybak
# 536xxxxxxx


#     [1] Sorgula
#     [2] Kişi Ekle
#     [3] Kişiyi Sil
#     [Q] Çıkış


# Lütfen İşlem Numarasını Tuşlayınız: 3
# Silinecek İsmi Giriniz: Alper Aybak


#     [1] Sorgula
#     [2] Kişi Ekle
#     [3] Kişiyi Sil
#     [Q] Çıkış


# Lütfen İşlem Numarasını Tuşlayınız: 1
# İsim: Alper Aybak
# Aranan Kişi Rehberde Bulunamıyor !


#     [1] Sorgula
#     [2] Kişi Ekle
#     [3] Kişiyi Sil
#     [Q] Çıkış


# Lütfen İşlem Numarasını Tuşlayınız: Q





#! Beraber basit bir Rehber Uygulaması yaptık umarım yararlı olmuştur ve kafanızda az çok şekillenmiştir.
#! Diğer dersimizde görüşmek üzere...