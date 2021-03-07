# AAI Company - Python

# Örnek Program




print("AAI Company'e Hoşgeldiniz\n\n")

while True:
    print("Üye Olmak İster Misiniz?\nLütfen Belirtildiği Gibi Yazınız\nEvet/Hayır\nCevap:")
    cevap=input()
    if (cevap == "Evet"):

        print("Lütfen Bekleyiniz...")
        print("Kayıt Ekranına Hoşgeldiniz.")
        ad=input("Adınız:")
        soyad=input("Soyadınız:")
        email= input("E-Mail Adresiniz: ")

        while True:
            sifre = input("Şifreniz:")
            sifre2 = input("Lütfen Şifrenizi Tekrar Giriniz:")

            if (sifre!=sifre2):
                print("Şifreniz Uyuşmuyor Lütfen Tekrar Oluşturunuz")

            else:
                print("Şifreniz Başarıyla Doğrulandı. Lütfen Devam Ediniz")
                break


        while True:
            yas = int(input("Yaşınız: "))
            if (yas>=16):
                print("16 yaşından büyüksüzünüz lütfen devam ediniz. ")
                break

            else:
                print("16 yaşından büyük değilsiniz, üzgünüz...")

        print("Bilgileriniz Gösteriliyor...\n Lütfen Kontrol Ediniz!")
        print("Ad: ", ad, "\nSoyad: ", soyad, "\nE-Mail: ",email, "\nŞifre: ",sifre,"\nYaş: ",yas)
        break

    else:
        print("Lütfen Sisteme Üye Olunuz")