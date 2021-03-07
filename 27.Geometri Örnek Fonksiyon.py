# AAI Company - Python


# Fonksiyonlar konumuzu pekiştirmek için örnekle devam edelim;
# Üçgen ve dörtgenleri bulacağımız bir geometri fonksiyonu yazalım:


def geometri(sekil):
    if len(sekil)==3:
        a=sekil[0]
        b=sekil[1]
        c=sekil[2]

        if(a+b)>c and(a+c)>b and (b+c)>a:
            if(a==b)and(a==c)and(b==c):
                print("Eşkenar Üçgen")
            elif(a==b)and(a==c):
                print("İkizkenar Üçgen")
            else:
                print("Çeşitkenar Üçgen")
        else:
            print("Üçgen Belirtmiyor")



    elif len(sekil)==4:
        a=sekil[0]
        b=sekil[1]
        c=sekil[2]
        d=sekil[3]
        if(a==b)and(a==c)and(a==d):
            print("Kare")
        elif(a==c)and(b==d):
            print("Dikdörtgen")
        else:
            print("Normal Dörtgen")


    else:
        print("Herhangi bir şekil değil")

while (True):
    eleman_sayisi=int(input("Eleman Sayısı Girin:"))
    if(eleman_sayisi==3):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometri([a,b,c])


    elif(eleman_sayisi==4):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        d=int(input("d:"))
        geometri([a, b, c,d])


    else:
        print("Lütfen Tekrar Giriniz")