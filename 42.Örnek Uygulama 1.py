# AAI Company - Python

# Örnek Uygulama - 1




#! Tarih ve Saat

import datetime;

gun = datetime.datetime.now().strftime("%d");
ay = datetime.datetime.now().strftime("%m");
yil = datetime.datetime.now().strftime("%Y");
saat = datetime.datetime.now().strftime("%H");
dakika = datetime.datetime.now().strftime("%M");
tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");

print("Tarih : ", gun + "-" + ay + "-" + yil);
print("Tarih Saat :", tarihsaat);



#! Sonsuz Saat Döngüsü

import time
while True:
    from datetime import datetime
    now = datetime.now()  
    print ("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)) 
    time.sleep(1)