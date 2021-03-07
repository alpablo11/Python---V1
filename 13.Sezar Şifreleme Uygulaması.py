# AAI Company - Python

# Sezar Şifreleme Uygulaması:

# Bu kod uygulaması fonksiyonlar ile de kurulabilir fakat biz biraz daha başlangıç seviyesine indireceğiz.
# Python'da öğretilen en temel kodlardandır.
# İsterseniz başlayalım;



alfabe = "abcçdefgğhıijklmnoöprsştuüvyzwxq abc"
cumle = input("Cümle Giriniz: ")
for i in cumle:
    print("Harf -->>",i,"   ---    indeks -->> ", cumle.index(i))

# Deneme yaparak çıktısını alalım isterseniz;

# Harf -->> A    ---    indeks -->>  0
# Harf -->> l    ---    indeks -->>  1
# Harf -->> p    ---    indeks -->>  2
# Harf -->> e    ---    indeks -->>  3
# Harf -->> r    ---    indeks -->>  4
# Harf -->>      ---    indeks -->>  5
# Harf -->> A    ---    indeks -->>  0
# Harf -->> y    ---    indeks -->>  7
# Harf -->> b    ---    indeks -->>  8
# Harf -->> a    ---    indeks -->>  9
# Harf -->> k    ---    indeks -->>  10


alfabe = "abcçdefgğhıijklmnoöprsştuüvyzwxq abc"
cumle = input("Cümle Giriniz: ")
yenicumle = "" 

for i in cumle:
    indeks = alfabe.index(i)
    yenicumle += alfabe[indeks+ 3]

print(yenicumle)

# Çıktımız ==>
# Cümle Giriniz: alperaybakindustries
# çoşğtçxdçnlpgyuvtlğu (şifreleme yöntemi)

# Böyle bir çıktı aldık fakat büyük harf kullanarak da test edelim isterseniz;

# # Çıktımız ==> 
# Cümle Giriniz: Alper Aybak
# Traceback (most recent call last):
#     indeks = alfabe.index(i)
# ValueError: substring not found

# Gördüğünüz gibi hata aldık dilerseniz else koşulu ile hatayı engelleyelim;

alfabe = "abcçdefgğhıijklmnoöprsştuüvyzwxq abc"
cumle = input("Cümle Giriniz: ")
yenicumle = "" 

for i in cumle:
    if i in alfabe:
        indeks = alfabe.index(i)
        yenicumle += alfabe[indeks+ 3]

    else:
        print("Karakter alfabe içerisinde mevcut değil: ", i)
        quit()

print(yenicumle)

# Şimdi çıktımıza bakalım;

# Cümle Giriniz: Alper Aybak
# Karakter alfabe içerisinde mevcut değil:  A



# Dilerseniz hem büyük harf hem de küçük harflerle yazalım bu uygulamayı;

k_alfabe = "abcçdefgğhıijklmnoöprsştuüvyzqwx +-*\\/)({}&%$#^'! abc"
b_alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQWX ABC"
cumle = input("Cümle Giriniz: ")
yeniCumle = ""

for i in cumle:
    if i in k_alfabe:
        ind= k_alfabe.index(i)
        yeniCumle += k_alfabe[ind + 3]

    elif i in b_alfabe:
        ind= b_alfabe.index(i)
        yeniCumle += b_alfabe[ind + 3]

    else:
        print("Bu karakter alfabe düzeninde mevcut değil !")
        print("Çevirilebilen cümle: ", yeniCumle)
        quit()

print(yeniCumle)


# İsterseniz şimdi de son üç karakteri kaldırarak şifreyi deşifre edelim;

k_alfabe = "abcçdefgğhıijklmnoöprsştuüvyzqwx +-*\\/)({}&%$#^'! abc"
b_alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQWX ABC"
cumle = input("Cümle Giriniz: ")
yeniCumle = ""

for i in cumle:
    if i in k_alfabe:
        ind= k_alfabe.index(i)
        yeniCumle += k_alfabe[ind - 3]

    elif i in b_alfabe:
        ind= b_alfabe.index(i)
        yeniCumle += b_alfabe[ind - 3]

    else:
        print("Bu karakter alfabe düzeninde mevcut değil !")
        print("Çevirilebilen cümle: ", yeniCumle)
        quit()

print(yeniCumle)

# Sezar Şifreleme Uygulamamız Tamamlanmış Bulunmakta. 13.dersimizde görüşmek üzere...
#! Herhangi bir sorun olursa iletişime geçmeyi unutmayın

