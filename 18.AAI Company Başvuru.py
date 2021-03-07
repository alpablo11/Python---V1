
# AAI Company - Python


#! AAI Company Başvuru Formu:





print("AAI Company'e Hoşgeldiniz")
print("İş Başvurusu Yapmak İster Misiniz\nEvet/Hayır")

cevap = input()
calisan_listesi = ["Alper Aybak - Yazılım ","Hüseyincan Bağcı - Finans"]



if (cevap=="Evet" or cevap =="evet" ):
    print("Başvuru Ekranına Hoşgeldiniz\n\t\nLütfen Bekleyiniz...\n\nYönetici Listesi Gösteriliyor...\n")
    for i in calisan_listesi:
        print(i)




    while True:
        calisan_listesi = ["Alper Aybak - Yazılım ","Hüseyincan Bağcı - Finans"]
        ad = input("Ad: ")
        soyad = input("Soyad: ")


        yas = int(input("Yaş: "))
        if (yas<18):
            print("18 Yaşının Altındasınız Üzgünüz...") 
            break

        else:
            print("Lütfen Devam Ediniz")


        mail = input("E-Mail Adresiniz: ")
        depertman = input("Çalışmak İstediğiniz Pozisyon: ")
        meslek = input("Mesleğiniz: ")
        öz_biyografi = input("Kısaca Kendinizi Tanıtın: ")
        tarih  = input("Tarih: ")

        print("Bilgileriniz Gösteriliyor...")

        print("Ad: {}\nSoyad: {}\nYaş: {}\nE-Mail Adresi: {}\nÇalışmak İstediğiniz Depertman: {}\nMeslek: {}\nÖz Biyografi: {}\nTarih: {}".format(ad,soyad,yas,mail,depertman,meslek,öz_biyografi,tarih))
        
        print("Bilgilerinizi Gözden Geçiriniz ve Onaylayınız")
        print("Bilgileri Onaylayıp Göndermek İstediğinize Emin Misiniz?\nE/H")
        cevap = input()


        if (cevap == "E" or cevap == "e"):
            print("Başvurunuz Teslim Edilmiştir.Sizi Aramızda Görmek İçin Sabırsızlanıyoruz")
            print("= AAI Company Çalışanları =")
            calisan_listesi.append("...Ve Gelecek Sizsiniz...")
            for i in calisan_listesi:
                print(i)
            print("Bizi Tercih Ettiğiniz İçin Teşşekür Ederiz...")
            break
        

        else:
            print("Lütfen Baştan Yazın ve Onaylayın")


else:
    print("Başvuru Ekranını Göremezsiniz, Bizi Tercih Ettiğiniz İçin Teşşekür Ederiz...")


print("== from Alper Aybak ==\n== AAI Company ==")




                   # from Alper Aybak 


# Listeleri ve veri tipinden de örnek verebileceğim bir kod yazdım. Dilerseniz siz daha da geliştirebilirsiniz...
# 19.ders olan Sözlük Veri Tiplerinde görüşmek üzere...