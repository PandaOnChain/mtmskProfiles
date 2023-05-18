from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import pickle
from multiprocessing import Pool


#подключаем файлы с кошелями
mtmsku: list = open('eth.txt', 'r', encoding='utf-8').read().splitlines()
kplru: list = open('cos.txt', 'r', encoding='utf-8').read().splitlines()
sloj = []

for i in range(len(mtmsku)):
    slo = [mtmsku[i], kplru[i]]
    sloj.append(slo)


def poshla_zhara(kshlk):
    try:
        chop = webdriver.ChromeOptions()
        chop.add_extension("metamask-chrome-10.6.4.crx")
        chop.add_extension("kepler_0_10_0_0.crx")

        #отключение режима WebDriver
        chop.add_argument("--disable-blink-features=AutomationControlled")
        #смена useragentoв
        #option.add_argument("user-agent=...")


        driver = webdriver.Chrome(chrome_options=chop)

        time.sleep(3)
        handle = driver.window_handles
        time.sleep(1)
        driver.switch_to.window(handle[0])
        time.sleep(1)

        driver.find_element_by_xpath("//*[contains(@class,'button')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(text(), 'Импорт')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(text(), 'Я согласен')]").click()
        time.sleep(1)
        # kosh = kshlk[0]#'announce cry benefit sleep fortune dial clutch space cry gesture video orphan'
        
        # comman = 'echo ' + kosh.strip() + '| clip'
        # os.system(comman)
        # driver.find_element_by_xpath("//input[contains(@class, 'MuiInput')]").send_keys(Keys.CONTROL, 'v')
        driver.find_element_by_xpath("//input[contains(@class, 'MuiInput')]").send_keys(kshlk[0])
        time.sleep(1)
        pswrd = "##"
        driver.find_element_by_xpath("//input[contains(@id, 'password')]").send_keys(pswrd)
        driver.find_element_by_xpath("//input[contains(@id, 'confirm-password')]").send_keys(pswrd)
        driver.find_element_by_xpath("//input[contains(@class, 'check-box')]").click()
        driver.find_element_by_xpath("//button[contains(text(), 'Импорт')]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[contains(text(), 'Все')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(@title, 'Закрыть')]").click()
        time.sleep(1)

        driver.find_element_by_xpath("//div[contains(@class, 'identicon__address-wrapper')]").click()
        driver.find_element_by_xpath("//div[contains(text(), 'Настройки')]").click()
        driver.find_element_by_xpath("//div[contains(text(), 'Дополнительно')]").click()

        #двигаю переключатель.
        driver.find_element_by_xpath("//*[@id='app-content']/div/div[3]/div/div[2]/div[2]/div[2]/div[7]/div[2]/div/div/div[1]").click()
        time.sleep(1)
        #переключение сети
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/li[5]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[1]').click()


        #открытие новой вкладки для кеплера

        kplrkosh = kshlk[1]#'police travel obey youth tone beyond gossip pact wood faculty siren north'

        driver.get('chrome-extension://dmkamcknogkgcdfhhbddcghachkejeap/popup.html#')
        time.sleep(4)
        ##надо переключиться на вкладку
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/button[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[contains(@name, 'words')]").send_keys(kplrkosh)
        driver.find_element_by_xpath("//input[contains(@name, 'name')]").send_keys(pswrd)
        driver.find_element_by_xpath("//input[contains(@name, 'password')]").send_keys(pswrd)
        driver.find_element_by_xpath("//input[contains(@name, 'confirmPassword')]").send_keys(pswrd)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/button[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/button').click()



        #переходим на сайт
        driver.switch_to.window(driver.window_handles[0])
        driver.get('https://app.umee.cc/')
        time.sleep(3)
        #подключение кошелька
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div/button/div').click()
        time.sleep(1)
        #metamask
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        #kplr
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/button[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/button[2]').click()
        try:
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/button[2]').click()
        except:
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        time.sleep(5)





        #save_cookie
        potoky = "kosh_" + process_count
        pickle.dump(driver.get_cookies(), open(f"{potoky}_cookiesssy", "wb"))


        #driver.execute_script('window.open("chrome-extension://dmkamcknogkgcdfhhbddcghachkejeap/popup.html#","_blank");')
        print("Красаучик, ска!")
    except Exception as ex:
        print(ex)    
    finally:    
        driver.close()
        driver.quit()

if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    p = Pool(processes=process_count)
    p.map(poshla_zhara, sloj)


# driver.window_handles - выводит список хэндлов (уникальный строковый идентификатор) всех открытых в данной сессии окон
# driver.current_window_handle - выводит хэндл текущего окона, с которым работает драйвер (то окно, в которое идут все команды, в том числе и driver.close())
# Для работы с другим окном, надо в него сначала переключиться - driver.switch_to.window(handle)
