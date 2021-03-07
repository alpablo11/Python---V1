# AAI Company - Python

# Fonksiyonlar konumuz önemli olduğu için tekrar etmeden geçmeyelim istedim.
# Ayrıca buraya kadar net bir şekilde anladıysak devam edelim. Ve baştan bir tekrarın zararı olmaz gibi :)
# Örneğimize geçelim isterseniz;




def aai_company():
    username = input("Kullanıcı Adı Oluşturunuz: ")
    password = input("Şifre Oluşturunuz: ")

    print("Hoşgeldiniz {} ".format(username))

    while True:

        print("Özel Erişim İçin Şifrenizi Tekrar Girmeniz İsteniyor!")
        password1 = input("Şifrenizi Tekrar Giriniz: ")

        if (password1 == password):

            print("Maaşlar Gösteriliyor...")
            yazilim = 30000
            gelistirici = 50000
            genel_tasarimci = 60000
            siber_guvenlik = 80000
            web_tasarim = 15000
            print(
                "Yazılımcı: {}\nGeliştirici: {}\nGenel Tasarımcı: {}\nSiber Güvenlik Uzmanı: {}\nWeb Designer: {}".format(
                    yazilim, gelistirici, genel_tasarimci, siber_guvenlik, web_tasarim))

            ad = "Alper Aybak"
            depertman = "Yazılım"
            maas = 150000
            print("Kurucu Bilgileri Gösteriliyor...\nAd: {}\nDepertman: {}\nMaaş: {} ".format(ad, depertman, maas))

            ad2 = "Hüseyincan Bağcı"
            depertman2 = "Hukuk ve Finans"
            maas2 = 150000
            print(
                "Ortaklığımızın Olduğu HCB Finance'ın Bilgileri Gösteriliyor...\nAd: {}\nDepertman: {}\nMaaş: {} ".format(
                    ad2, depertman2, maas2))

            print("from Alper Aybak")
            print("AAI Company\n©2021")

            print("Çıkmak İçin 'q' veya 'Q' Harfini Tuşlayınız!")

            cevap = input()

            if (cevap == "q" or cevap == "Q"):
                print("Çıkış Yapıldı...")
                print("Teşekkür Ederiz {} ".format(username))
                exit()

            else:
                print("Bilgiler Baştan Gösteriliyor...")



        else:
            print("Girdiğiniz Şifre Uyuşmuyor!")
            print("Şifrenizi Mi Unuttunuz ?\nŞifrenizi Değiştirmek İster Misiniz?")
            print(
                "Eğer cevabınız 'Evet' ise 'e' veya 'E' harfini tuşlayınız.\nEğer cevabınız 'Hayır' ise veya şifrenizi yeniden denemek istiyorsanız herhangi bir tuşa basınız")

            cevap = input()

            if (cevap == "e" or cevap == "E"):
                yeni_sifre = input("Lütfen Yeni Şifrenizi Giriniz: ")
                print("Yeni Şifreniz Kaydediliyor...")
                password = yeni_sifre
                print("Yeni Şifre Başarıyla Kaydedildi.")

            else:
                print("Lütfen Tekrar Deneyiniz.")


aai_company()






# Herhangi bir sorun olursa iletişime geçebilirsiniz.
# Diğer dersimizde görüşmek üzere...