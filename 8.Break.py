# AAI Company - Python
# Break


# break:
# Break => şartlı bir döngünün isteğimizin gerçekleştiği yerde kırılması yani döngüyü durdurması demektir.
# Örnekle açıklayalım isterseniz;

defkullanıcı="AAI Company"
defparola="alperaybak"

while True:
    kullanıcı=input("Kullanıcı adı:")
    parola=input("Parola:")
    if((kullanıcı!=defkullanıcı)or(parola!=defparola)):
        print("Yanlış Giriş!")
    else:
        print("Hoşgeldiniz")
        break

# Gördüğümüz gibi kullanıcı adı ve parolayı doğru yazarsak döngümüz duruyor ve sanki bir sisteme giriş yapmış gibi "Hoşgeldiniz" çıktısını ekrana yazdırıyor. 
# Fakat bool çıktısı olarak "true" olmazsa doğru sonucu alana kadar sonsuz döngümüz çalışacaktır, deneyebilirsiniz.

#  Break konusuna dair detayları verdiğimi düşünüyorum, yine de aklınıza takılan bir şey olursa iletişime geçebilirsiniz.

# Geldiğimiz konuları tekrar etmek için örnek program yazdım. 10.dersimizde hata yakalamaya geçeceğiz...