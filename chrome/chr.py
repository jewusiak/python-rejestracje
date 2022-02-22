import time

from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium.webdriver.remote.webelement import *

import credentials

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
driver.get("https://cas.usos.pw.edu.pl/cas/login?service=https%3A%2F%2Fusosweb.usos.pw.edu.pl%2Fkontroler.php%3F_action%3Ddla_stud%2Frejestracja%2Fbrdg2%2FgrupyPrzedmiotu%26rej_kod%3D6430-WFS-2022L%26prz_kod%3D6430-00000-000-0025%26cdyd_kod%3D2022L%26odczyt%3D0%26prgos_id%3D1249161%26callback%3Dg_ae5fb893&locale=pl")

username_input=driver.find_element_by_id('username')
username_input.clear()
username_input.send_keys(credentials.usos_login)

password_input=driver.find_element_by_id('password')
password_input.clear()
password_input.send_keys(credentials.usos_password)

driver.find_element_by_name('submit').click()

while True:

    driver.find_element_by_xpath("//input[@type='radio' and @value='1']").click()

    driver.find_element_by_xpath("//input[@type='submit' and @value='Rejestruj']").click()
    if driver.find_element_by_id("confirmation_notice").get_attribute('style')!="display: none;":
        break
    time.sleep(5)
    driver.refresh()

input("end")

