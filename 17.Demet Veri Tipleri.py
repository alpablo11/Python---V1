# AAI Company - Python

# Demet Veri Tipleri 

# Demetler, liste ve karakter dizileri gibi sıralı yapılardır.
# Bir indeks değerine sahiplerdir.
# Aynı listeler gibi tüm veri tiplerini içerisinde barındırabilir.


#! Demetlerin Kullanımı:
# Bir demet tanımlamak istersek normal parantezden "()" yararlanıyoruz.
# İsterseniz örnekle açıklayalım;

demet = ("Alper Aybak","N harfi","AAI Company","alperaybakindustries")

# Demet tanımlamak da aynı liste tanımlamak gibi kolay liste tanımlamak için şöyle yapıyorduk hatırlarsanız;

liste = list() #  Veya [] kullanabiliriz.

# İsterseniz şimdi de demet tanımlayalım;

demet = ()
print(type(demet))  # type() Metodu ==> hangi sınıfa ait olduğunu gösterir (tipini gösterir) 

# Çıktımız ==> <class 'tuple'>
# Gördüğünüz gibi demet sınıfı olduğunu gördük (tuple=demet)

# Örnek verelim isterseniz;

programlama_dilleri = (["Python","Java","C ve C++"],["C#","JavaScript","Php","Perl"],["CSS","HTML","Angular"])
programlama_dilleri[1].append("Kotlin")
print(programlama_dilleri)

# Çıktımız ==> (['Python', 'Java', 'C ve C++'], ['C#', 'JavaScript', 'Php', 'Perl', 'Kotlin'], ['CSS', 'HTML', 'Angular'])

# Dilerseniz demet metodlarına bakmak için dir() kodumuzu yazalım;

programlama_dilleri = (["Python","Java","C ve C++"],["C#","JavaScript","Php","Perl"],["CSS","HTML","Angular"])
for i in dir(programlama_dilleri):
    if "__" not in i:
        print(i)

# Çıktımız ==> 
# count
# index

#! Demetlerin Metodları:

# index() Metodu:
# Demet içerisindeki bir ögenin kaçıncı indekste yer aldığı çıktısını aldığımız veri tipidir
# İsterseniz örnekle açıklayalım;

company = ("ALPER","alper","AYBAK","aybak","INDUSTRIES","industries")
print(company.index("AYBAK"))

# Çıktımız ==> 2
# Zaten aşina olduğumuz için fazla üzerinde durmayalım.


# count() Metodu:
# Ögenin kaç adet olduğu çıktısını veriyordu
# Daha önceden bildiğimiz için, üzerinde yine fazla durmayalım örneğe geçelim;

sayilar = (1,23,4,2345235,11,34425,11,43254,3,465,43,3244,11,43234,11,54,45,11,25432,11,324134,34,2,4,23,424,2,34,11)
print(sayilar.count(11))

# Çıktımız ==> 7


# Arkadaşlar demetler dersimiz bu kadardı. Aklınıza takılan bir şey olursa iletişime geçebilirsiniz.
# Görüşmek üzere...