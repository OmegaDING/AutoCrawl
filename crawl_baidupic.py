import os.path


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import requests

def getnamepage(name):
    b.get('http://image.baidu.com/')
    search_box=b.find_element_by_id('kw')
    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

def download(name,num,size):
    #选取大尺寸
    ele=b.find_element_by_id('sizeFilter')
    ActionChains(b).move_to_element(ele).perform()
    time.sleep(0.5)
    # 选定指定的大小
    if(size == 'super'):
        ele4=b.find_element_by_xpath('//*[@id="sizeFilter"]/div/div[2]/ul/li[2]')
    elif(size == 'big'):
        ele4 = b.find_element_by_xpath('//*[@id="sizeFilter"]/div/div[2]/ul/li[3]')
    elif(size == 'mid'):
        ele4 = b.find_element_by_xpath('//*[@id="sizeFilter"]/div/div[2]/ul/li[4]')
    elif(size == 'small'):
        ele4 = b.find_element_by_xpath('//*[@id="sizeFilter"]/div/div[2]/ul/li[5]')
    else:
        ele4 = b.find_element_by_xpath('//*[@id="sizeFilter"]/div/div[2]/ul/li[2]')

    ActionChains(b).move_to_element(ele4).perform()
    time.sleep(0.5)
    ele4.click()
    time.sleep(8)

    #打开第一张图片，在此界面中点击左右切换图片
    ele1=b.find_element_by_xpath('//*[@id="imgid"]/div[1]/ul/li[5]/div/div[2]/a/img')
    ele1.click()
    b.switch_to.window(b.window_handles[1])#很重要的一步，切换窗口，否则页面找不到元素,python shell里面是b.switch_to_window
    x=1
    for i in range(1,num+1):
        ele2=b.find_element_by_xpath('//*[@id="currentImg"]')
        img=ele2.get_attribute('src')#获取当前图片的url链接

        #下载img
        r=requests.get(img)
        if r.status_code==200:
            path = './'+str(name)+'/%d.jpg'%x
            print('正在爬取第'+str(x)+'张 '+name)
            with open(path,'wb') as f:
                f.write(r.content)
                time.sleep(0.8)
                f.close()
                print('爬取成功')
                x+=1
            ele3=b.find_element_by_xpath('/html/body/div[1]/div[2]/div/span[2]/span')
            ele3.click()
        #跳到下一张
        else:
            print('正在重试')
            ele3=b.find_element_by_xpath('/html/body/div[1]/div[2]/div/span[2]/span')
            ele3.click()
            time.sleep(3)
            continue
        



def run(name,num,size):

    if not os.path.isdir(name):
        os.makedirs(name)

    getnamepage(name)

    download(name,num,size)
    b.close()
    #关闭第一个窗口
    b.switch_to.window(b.window_handles[0])
    b.close()

def again(name,num,size):

    try:
        run(name,num,size)
    except:
        print("爬取出错，正在重试".center(50,"^"))
        again(name,num,size)
    finally:
        print("结束爬取")


if __name__ == "__main__":
    print("自动爬取百度图片".center(50,"*"))
    name=input("爬取关键字:")
    num=int(input("数量:"))
    print("输入图片大小，请输入：")
    print("默认super大小")
    size=input("super,big,mid,small？\n")
    b = webdriver.Chrome('.\chromedriver')

    again(name,num,size)
    b.close()
    print("爬取完毕".center(50,"*"))
