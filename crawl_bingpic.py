import os

import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_img(keyword, num):
    b = webdriver.Chrome()
    #搜索界面
    b.get('https://www.bing.com/?scope=images&nr=1&FORM=NOFORM')
    time.sleep(3)
    search_box=b.find_element(by=By.XPATH,
                              value='//*[@id="sb_form_q"]')
    search_box.send_keys(keyword)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)


    time.sleep(8)
    ele = b.find_element(by=By.XPATH,
                         value='//*[@id="mmComponent_images_2_list_1"]/li[1]/div/div[1]/a/div/img')
    ele.click()

    time.sleep(10)

    import pdb
    pdb.set_trace()
    # ele = b.find_element(by=By.XPATH,value='//*[@id="mainImageWindow"]')
    '//*[@id="mainImageWindow"]/div[1]/div/div/div/img'

    ele = b.find_element(by=By.XPATH,
                         value='//*[@id="mainImageContainer"]')
    ActionChains(b).move_to_element(ele).perform()
    try:
        ele = b.find_element(by=By.XPATH,
                         value='//*[@id="mainImageWindow"]/div[1]/div/div/div/img')
    except:
        ele = b.find_element(by=By.XPATH,
                         value='//*[@id="mainImageWindow"]/div[1]/div/div/div/img')



    url = ele.get_attribute('src')
    download(url, './1.jpg')
    ele = b.find_element(by=By.XPATH,
                         value='//*[@id="navr"]/span')
    ele.click()


    input("press any button after finished the verify")


def download(url, path):
    # 下载
    proxies = {
        "http": 'http://127.0.0.1:4201',
        "https": 'https://127.0.0.1:4201'
    }
    r = requests.get(url,proxies)

    if r.status_code == 200:
        print('正在下载' + str(url))
        with open(path, 'wb') as f:
            f.write(r.content)
            time.sleep(0.8)
            f.close()
            print('下载成功'.center(50, "*"))
    #
    else:
        print('下载出错')

if __name__ =='__main__':
    get_img("Diana", 5)