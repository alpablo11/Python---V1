#AAI Company - Python 

# Örnek Uygulama - 3



#! WhatsApp Mesaj Yollama 
# NOT = selenium indirmeyi unutmayalım.


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get(“https://goo.gl/WCS3hC")
wait = WebDriverWait(driver, 600)
driver.maximize_window()
driver.execute_script(“window.open(‘about:blank’, ‘tab2’);”)
driver.switch_to.window(“tab2”)
driver.get(‘http://secim.parti.org.tr/')
wait = WebDriverWait(driver, 600)
kllnc = driver.find_element_by_xpath(“//*[@id=’txtKullaniciAdi’]”)
prl = driver.find_element_by_xpath(“//*[@id=’txtParola’]”)
kllnc.send_keys(“kullanıcı_adı”)
prl.send_keys(“parola”)
buton = driver.find_element_by_xpath(“//*[@id=’btnLogin’]”)
wait = WebDriverWait(driver, 600)
buton.click()
driver.switch_to_window(driver.window_handles[0])
isim = ‘Parti_grubu’
input(‘Kare Kod okuttuktan sonra Enter'a basınız.’)
grup = driver.find_element_by_xpath(‘//span[@title = “{}”]’.format(isim))
grup.click()
box = driver.find_element_by_xpath(“//*[@id=’main’]/footer/div[1]/div[2]/div/div[2]”)
box.send_keys(” Merhabalar, sandık numarasını öğrenmek istediğiniz TC kimlik numarasını giriniz.” + Keys.ENTER))


#! Daha net açıklamalar için ==> https://medium.com/@chelewy/python-ile-whatsapp-chatbot-yap%C4%B1m%C4%B1-6c3c0afcb365 adresinden bakabilirsiniz.