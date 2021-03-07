# AAI Company - Python

# Fonksiyonlar ile İlgili Örnek Uygulamalar :


#! Asal Sayı Sorgulama:

def asal_mi(a: int):

    dogrulama = "Sayı Asal"
    if a == 2:
        return dogrulama  # return ==> Geri Dön

    elif (a % 2 == 0):
        dogrulama = "Sayı Asal Değil"  # Eğer sayı çiftse asal olmayacağı için False veri tipini yolladık.

    if dogrulama:  # Değer False değilse kontrole geçelim

        for n in range(3, int(a / 2)):
            if (a % n == 0):
                print(a, "Sayısının", n, "Sayısına Bölümü:", a / n, "Kalan ise 0'dır.")
                dogrulama = "Sayı Asal Değil"
                break

    return dogrulama


a = asal_mi(11)
print(a)

# Çıktımız ==> Sayı Asal

a = asal_mi(68)
print(a)

# Çıktımız :
# 68 Sayısının 4 Sayısına Bölümü: 17.0 Kalan ise 0'dır.
# Sayı Asal Değil



#! Kesişim Kümesi Bulan Fonksiyon:

N = {11,21,"N","NA","Aybak",232,423,544,566,45,22,2,71}
A = {13,34,345,3,"Alper","AAI",213,11,2,12,"NA","A"}

def kesisim( N: set, A: set):
    kesisim_kumesi = set()


    for N_eleman in N:
        for A_eleman in A:
            if (N_eleman == A_eleman):
                kesisim_kumesi.add(N_eleman)

    

    if kesisim_kumesi:
        return kesisim_kumesi

    
    else:
        return False


print(kesisim(N,A))

# Çıktımız ==> {2, 11, 'NA'}






#! Faktoriyel Hesaplama: 

def factoriel(numara):
    faktoriyel=1

    for i in range(1,numara+1):
        faktoriyel*=i

    print("Faktoriyel: {}".format(faktoriyel))


factoriel(11)

# Çıktımız ==> Faktoriyel: 39916800



#! Eğer print kısmını koşuldan çıkarmazsak o sayıya gelene kadar ki yerleri çıktı alırız.
# İsterseniz bir de öyle bakalım;

def factoriel(numara):
    faktoriyel=1
    for i in range(1,numara+1):
        faktoriyel*=i
        print("Faktoriyel: {}".format(faktoriyel))


factoriel(11)

# Çıktımız :
# Faktoriyel: 1
# Faktoriyel: 2
# Faktoriyel: 6
# Faktoriyel: 24
# Faktoriyel: 120
# Faktoriyel: 720
# Faktoriyel: 5040
# Faktoriyel: 40320
# Faktoriyel: 362880
# Faktoriyel: 3628800
# Faktoriyel: 39916800