# AAI Company - Python

#! Ekstralar - 2

# SMTP modülü ile Mail gönderme işlemi yapacağız.


import smtplib

content = "AAI Company'e Hoşgeldiniz"

mail = smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()

mail.starttls()


mail.login("email_adresi","şifre")


mail.sendmail("alperaybakiletisim@gmail.com",content)


# Arkadaşlar burada mail ayarlarınızdan Daha az güvenli uygulamaları etkinleştirmeniz gerekiyor aksi takdirde google kendini korumaya alacaktır.

