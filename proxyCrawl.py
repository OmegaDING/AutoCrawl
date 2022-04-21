## 启动代理
from browsermobproxy import Server
import time

## selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

server = Server(r'.\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()

chrome_options = Options()
print(proxy.proxy)
chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe',
                          options=chrome_options)

proxy.new_har("my_web", options={'captureHeaders': True, 'captureContent': True})

driver.get('https://wy.wxbtech.com/alarmManage/alarmRecord')

time.sleep(60)
# do some thing

result = proxy.har

maxLog=[]
for i, log in enumerate(result['log']['entries']):
    if log['response']['content']['mimeType'].find('fetch') !=-1:

        maxLog.append(log)
import pdb
pdb.set_trace()


with open('test.har', 'w', encoding='utf-8') as f:
    f.write(str(result))
    print('ok')