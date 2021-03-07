

# AAI Company - Python 


#! Ekstralar - 1

import _sqlite3

con=_sqlite3.connect("aaindustries.db")

cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREAT TABLE IF NOT EXISTS uyeler(ad TEXT,soyad TEXT,numara INT)")


def degerekle():
    cursor.execute("INSERT INTO UYELER VALUES ('Alper','Aybak',11)")
    con.commit()
    con.close()


tabloolustur()




#! sqlite3 dosyası oluşturmak için kullanıyoruz.
# sqlite3  olması gerektiğini unutmuyoruz.
