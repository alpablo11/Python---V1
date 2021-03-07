#  AAI Company - Python


#  Hata Yakalama Nedir? 
# Programlamada bazı hatalarla karşılaşmak mümkündür.
# Örnekle anlatırsam daha iyi anlaşılacağına eminim;

a = int(input("Bir Sayı giriniz: "))

# Yukarıdaki örneğe ben herhangi bir sayı girersem hata almayacağım.
# Fakat "string" tipinde veri girip çalıştırırsam ekrana çıktım => "ValueError" şeklinde çıkacaktır.
# Yani sistemimiz doğal olarak çökmüş bulunuyor.
# İşte böyle durumlardan kurtulmak için bir çok yöntem deneyebiliriz. Bu dersimizde hata çeşitleri, neler yapmalıyız onlara değineceğiz.


# Hata Çeşitleri:

# -Programcı Hatası:
# Kodun kullanıcıya ulaşmadan önce fark edilip düzeltilmesidir.
# Python dilinden basit bir örnek verelim isterseniz;

a=1
while (a<21)
print(a)
a +=1

# Yukarıdaki kodu çalıştırdığımız zaman bize hata verecektir. Sebebi ise şu iki nokta (:) koymadığımız için print ve sonraki işleçlerin yeri kaydı ve en başa geçti.


# -Program Hatası:
# Bug olarak ta adlandırılabilir. Sorun çıkmadan çalışır ama sistemin doğruyu yanlışı ayıramadığı durumdur.

# -İstisnai Durumlar:
# Programın bazen çalışıp bazen çalışmaması durumudur.
# Örnek ile açıklamak gerekirse;

import os

userFolder = os.path.expanduser('~')
os.chdir(userFolder + '\\' + 'Desktop')

with open('AAI Company.txt'):
    print("Dosya Mevcut")


# Arkadaşlar yukarıdaki kodu anlamamış olabilirsiniz. Açıklayalım:
# Biz os (Operating System - İşletim Sistemi ) aktif olsun dedik ve aktif etmek için import metodunu kullandık.
# Python'a şöyle bir komut verdik "AAI Company.txt" dosyasını aç.
# Eğer sizin sisteminizde bu dosya varsa açacaktır yoksa hata alacaksınızdır.
# İsterseniz "AAI Company.txt" dosyasını oluşturup tekrar deneyelim.
# Şimdi açılıyordur fakat yine açılmayabilir sebebi de windows işletim sistemi kullanmıyor olmanız olabilir.


# ! Tüm bu hataların çözüm yöntemlerinden bahsedeceğiz !

# Hataları Yakalayalım 

# Yine bir örnekle gitmek istiyorum;

a = input("Bir sayı giriniz: ")
n = input("Bir sayı giriniz: ")

print(int(a)/ int(n))

# Baktığımız zaman sistemimizde sorun gözükmüyor fakat n sayısı için 0 değerini verirsek sistemimiz hata verecektir.
# Bundan çok basit yöntemle kurtulabiliriz, görelim;

a = input("Bir sayı giriniz: ")
n = input("Bir sayı giriniz: ")

if (n == "0"):
    print(" Girdiğiniz İşlem Tanımsız")
else:
    print(int(a)/int(n))



# İsterseniz işleri iyice ilerletelim ve heyecan katalım.
# Yapacağımız işlemleri anlamayabilirsiniz o yüzden açıklayacağım;
# 1)Kullanıcıdan sayı al
# 2)Kllavyedeki tuşlardan biri bu sayılar içerisinde var mı kontrol et
# 3)Eğer varsa kullanıcının anlayacağı hata mesajı ver
# 4)Eğer yalnızca sayı varsa ikinci sayımız 0 mı onu kontrol et
# 5)Eğer 0 ise kullanıcıya hata mesajı ver
# 6)Eğer 0 değilse bölme işlemini tamamla

# İşlemleri kafamızda oturttuğumuza göre artık yazabiliriz.

klavye_tuslari ="abcçdefgğhıijklmnoöprsştuüvyzwqx!^#,./*-+\\"
sayi_1 = input("1.Sayıyı Giriniz: ")
sayi_2 = input("2.Sayıyı Giriniz: ")

flag = True

for i in klavye_tuslari:
    if i in sayi_1 or i in sayi_2:
        print("Yalnızca Sayı Girmelisiniz !")
        flag = False
        break

if flag:
    if (sayi_2 == '0'):
        print("Sıfıra Bölüm Tanımsızdır!")

    else:
        print("Sonuç: ",float(sayi_1)/float(sayi_2))

# Eminim ki örnekle çok daha rahat anlaşılmıştır.

# Bir örnek daha yapalım ve aklımıza iyice kazınsın;

rakamlar =  "0123456789"
sayi_1 = input("1.Sayıyı Giriniz: ")
sayi_2 = input("2.Sayıyı Giriniz: ")

flag = True

for n in sayi_1:
    if n not in rakamlar:
        flag = False
        break

for a in sayi_2:
    if a not in rakamlar:
        flag = False
        break

if flag:
    if (sayi_2 == "0"):
        print("Sonuç Tanımsız!")

    else:
        print("Sonuç: ", float(n)/float(a))

    
else:
    print("Yalnızca Rakam Giriniz!")


# Evet arkadaşlar umarım çok daha net anlaşılmıştır. Eğer burada bir sıkıntı varsa lütfen belirtin.



# Hata Yakalama Blokları:
# Bu mekanizmayı try except bloklarıyla yapacağız, kısaca bahsedip örnekle açıklayalım
# try bloğunda yapılmaya çalışılan, denenen bir veya birden fazla işlem yer alır.
# Örnekle açıklayalım isterseniz;

a = input("Sayı 1: ")
n = input("Sayı 2: ")

try:
    a = float(a)
    n = float(n)

except ValueError:
    print("Yalnızca sayı giriniz.")
    quit()

try:
    print("Sonuç: ",a/n)

except ZeroDivisionError:
    print("Sonuç Tanımsız")


# Arkadaşlar ilk defa gördüğünüz metodlar çoğu anlamış olabilirsiniz ama yine de üzerinde geçeceğim

# İlk olarak kullanıcıdan sayı almak için a ve n'ye input ile değer atadık.
# try bloğumuz ile geri dönüş sağlayıp a ve n değerlerinin float (ondalık) sayı tipinde olmasını istedik.

# Daha sonra kullanıcı sayı girmezse diye except ValueError bloğumuzu devreye sokduk yani ValueError çıktısı yerine bize hatamızı söylesin 
# Ve quit() metodu ile çıkış yapmamızı sağladık.

# Eğer bunlar olmazsa diye try bloğunu devreye soktuk ve sonucu yazdırmasını istedik.
# Bölme işlemi yaptığımız için except ZeroDivisionError bloğunu çağırarak n sayımız 0 olursa Tanımsız çıktısını yazdırdık.


# Evet arkadaşlar hata yakalama konumuz bu kadar umarım anlaşılmıştır. En olmadı hata çıktılarını düzelte düzelte öğrenirsiniz :)
# Herhangi bir sorunuz olursa iletişime geçebilirsiniz. Bu dersi güzelce sindirelim daha sonraki derste görüşmek üzere.