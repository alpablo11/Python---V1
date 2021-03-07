# AAI Company - Python 

#! Ekstralar - 3

# İnternetten Python'a nasıl forğraf/resim indirilir onu göreceğiz;


import urllib.request

url1 = "kopyalanan adres buraya yapıştırılacak"
url2 = "kopyalanan adres buraya yapıştırılacak"

urllistesi = [url1,url2]
say  = 1
for url in urllistesi:
    urllib.request.urlretrieve(url,"Resim/Fotoğraf" + str(say)+ ".jpg") # Dosya uzantımız PNG ise .png eklemeniz gereklidir.
    say+=1


# Dilerseniz 2'den fazla ya da tek fotoğraf ta indirebilirsiniz.
# url sayısı ekleyip silmek tek yapmanız gereken