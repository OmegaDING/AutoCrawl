import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def getVideoURL(keyword = "",num=1):
    b = webdriver.Chrome()
    #搜索界面
    b.get('http://www.bilibili.com/')
    url={}
    #
    ele = b.find_element_by_xpath("//*[@id=\"i_cecream\"]/div[1]/div[1]")
    ActionChains(b).move_to_element(ele).perform()
    ele.click()
    #
    time.sleep(5)
    try:
        search_box = b.find_element_by_xpath("//*[@id=\"nav-searchform\"]/input")
    except:
        search_box = b.find_element_by_xpath('//*[@id="nav-searchform"]/div[1]/input')

    search_box.send_keys(keyword)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(8)
    for i in range(num):

        b.switch_to.window(b.window_handles[1])
        #默认第一个视频
        video_xpath=[]
        video_xpath.append("//*[@id=\"i_cecream\"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div[%s]/div/div[2]/div/div/a/h3")
        video_xpath.append("//*[@id=\"i_cecream\"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div[%s]/div/div[2]/div/div/a/h3")
        video_xpath.append('//*[@id= "i_cecream "]/div[1]/div[1]/div[2]/div/div/div/div/div[%s]/div/div[2]/div/div/a/h3')
        video_xpath.append('//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[%s]/div/div[2]/div/div/a/h3')
        video_xpath.append('//*[@id="all-list"]/div[1]/div[2]/ul/li[%s]/div/div[1]/a')

        for xpath in video_xpath:
            try:
                ele = b.find_element_by_xpath(str(xpath)%(i+1))
                print("找到第一个视频xpath")
                break
            except:
                print("尝试下一个xpath")
        ActionChains(b).move_to_element(ele).perform()
        time.sleep(0.5)
        ele.click()

        time.sleep(0.5)
        b.switch_to.window(b.window_handles[2])
        url[i] = b.current_url
        time.sleep(5)
        b.close()




    # 关闭之前剩余的页面
    pages = b.window_handles
    for handle in pages:
        b.switch_to.window(handle)
        b.close()
    return url

def crawl_bilibili(keyword : str,num : int):
    print("正在爬取b站视频，keyword：" + keyword +" num: " +str(num))
    url = getVideoURL(keyword,num)
    print(url)
    for i in range(len(url)):
        cmd = "you-get -o %s -f "%name + str(url[i])
        print(cmd)
        try:
            os.system(cmd)
        except:
            os.system(cmd)


if __name__ == '__main__':
    print("自动下载bilibili视频".center(50,"*"))
    name = input("关键字:")
    num = int(input("数量:"))
    if not os.path.isdir(name):
        os.mkdir(name)
    #下载搜索到的视频
    crawl_bilibili(name,num)
    print("下载结束".center(50,"*"))