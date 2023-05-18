from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
service = Service(executable_path=ChromeDriverManager().install())
apps = webdriver.ChromeOptions()
apps.add_extension("metamask_10_12_2_0.crx")
apps.add_argument('--lang=en')
#apps.add_extension("kepler_0_10_0_0.crx")
#apps.add_argument("user-data-dir=Test1")  # Save Profile
#apps.add_argument("--profile-directory=Test1")  # Choose witch profile you would like to use

#apps.add_argument('--allow-profiles-outside-user-dir')
#apps.add_argument('--enable-profile-shortcut-manager')
apps.add_argument(r"user-data-dir=C:\Users\mask\User2")
apps.add_argument(r'--profile-directory=C:\Users\mask\Profile_122')
driver = webdriver.Chrome(service=service, options=apps) #осталась лишь ошибка по поводу пат

############################
time.sleep(1)
handle = driver.window_handles


time.sleep(1)
driver.switch_to.window(handle[0])
time.sleep(1)
#CTRL + / всё, что ниже, для проверки
eth_seed = 'announce cry benefit sleep fortune dial clutch space cry gesture video orphan'
kosh = eth_seed.split()
print(kosh)
time.sleep(1)
driver.find_element_by_xpath("//*[contains(@class,'button')]").click()
time.sleep(1)

#umee_wallet = driver.find_element_by_xpath('//*[contains(@title, "umee1")]').get_attribute("title")

driver.find_element_by_xpath("//button[contains(text(), 'Import')]").click()
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(), 'Agree')]").click()
time.sleep(1)

for i in range(12):
    k = str(i)
    driver.find_element_by_xpath('//*[@id="import-srp__srp-word-'+k+'"]').send_keys(kosh[i])
time.sleep(1)
pswrd = "DDBVT_2022"
driver.find_element_by_xpath("//input[contains(@id, 'password')]").send_keys(pswrd)
driver.find_element_by_xpath("//input[contains(@id, 'confirm-password')]").send_keys(pswrd)
driver.find_element_by_xpath("//input[contains(@class, 'check-box')]").click()
driver.find_element_by_xpath("//button[contains(text(), 'Import')]").click()
time.sleep(3)
driver.find_element_by_xpath("//button[contains(text(), 'All')]").click()
time.sleep(1)
driver.find_element_by_xpath("//button[contains(@title, 'Close')]").click()
time.sleep(1)

driver.get("https://vk.com")
time.sleep(4)
driver.close()
driver.quit()
