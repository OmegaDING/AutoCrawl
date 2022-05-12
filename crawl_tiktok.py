import os

import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_video(keyword, num):
    b = webdriver.Chrome()
    #搜索界面
    b.get('https://www.tiktok.com/')
    time.sleep(3)
    search_box=b.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/form/input')
    search_box.send_keys(keyword)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    input("press any button after finished the verify")

    try:

        ele = b.find_element(by=By.XPATH,
                             value='//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/div/div/a/div/div[1]/img')
        ele.click()
    except:
        ele = b.find_element(by= By.XPATH,
                             value='//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/div/div/a/div/div[1]/img')
        ele.click()

    time.sleep(5)
    ele = b.find_element(by=By.XPATH,
                         value='//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/video')
    url = ele.get_attribute('src')  # 获取当前url链接
    download(url,"./a.mp4")

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
    get_video("Diana", 5)