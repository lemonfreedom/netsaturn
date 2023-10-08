# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

driver = webdriver.Chrome()
driver.get('https://v.qq.com/channel/movie/list?filter_params=sort%3D75&page_id=channel_list_second_page')
driver.maximize_window()

file = open('C:\\Users\\zhangguoqing\\Documents\\Workspace\\netsaturn\\netsaturn-py\\电影资源.txt',
            'w', encoding='utf-8')


def download(file_path, picture_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 			(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE",
    }
    r = requests.get(picture_url, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(r.content)


def z():
    n1 = driver.find_elements(By.CSS_SELECTOR, '.card-list-wrap .card')
    for e in n1:
        n2 = e.find_element(By.CLASS_NAME, 'title')
        imgEl = e.find_element(By.CLASS_NAME, 'poster-img')

        n3 = e.find_element(By.CLASS_NAME, 'sub-title')
        file.write('标题：'+n2.text + '\n')
        file.write('副标题：'+n3.text + '\n')
        file.write('播放地址：'+e.get_attribute('href') + '\n')
        imgUrl = imgEl.get_attribute('data-src')
        file.write('背景：'+imgUrl + '\n')

        file.write('\n')
        # download(
        #     'C:\\Users\\zhangguoqing\\Documents\\Workspace\\netsaturn\\netsaturn-py\\images\\'+n2.text+'.jpg',
        #     'https:' + imgUrl)

        print("《"+n2.text + '》爬取成功')


for i in range(9999999):
    top = i*2160
    script = "document.querySelector('.list-page-wrap').scrollTop=" + str(top)
    driver.execute_script(script)
    time.sleep(0.1)
    z()
