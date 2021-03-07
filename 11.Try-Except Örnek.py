# AAI Company - Python 

# Try - Except Örneği ile devam edelim isterseniz;

sayi1=input("SAYI1:")
sayi2=input("SAYI2:")

try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1/sayi2)

except ValueError:
    print("Lütfen 10'luk tabanda sayı giriniz.")

except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")



sayi1=input("SAYI1:")
sayi2=input("SAYI2:")

try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1/sayi2)

except (ValueError,ZeroDivisionError):
    print("Bir hata oluştu")
