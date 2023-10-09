from selenium import webdriver
from selenium.webdriver.common.by import By
import os

address = 'https://so.tv.sohu.com/list_p1101_p2_p3_p4_p5_p6_p77_p80_p92_p10_p11_p12_p13_p14.html'

driver = webdriver.Chrome()
driver.get(address)

resultPath = os.path.dirname(os.path.abspath(__file__)) + '\\sohu.txt'
print(resultPath)
file = open(resultPath, 'w', encoding='utf-8')


def parse():
    cards = driver.find_elements(By.CSS_SELECTOR, '.st-list>li')
    for card in cards:
        titleEl = card.find_element(By.CSS_SELECTOR, 'strong>a')
        title = titleEl.text
        url = titleEl.get_attribute('href')
        file.write(title + ',' + url + '\n')
        deep(url)


def deep(url):
    deepDriver = webdriver.Chrome()
    deepDriver.get(url)
    series = deepDriver.find_elements(By.CSS_SELECTOR, '.series2 .sera2')
    for serie in series:
        titleEl = serie.find_element(By.CSS_SELECTOR, '.sera')
        title = titleEl.text
        url = titleEl.get_attribute('href')
        file.write(title + ',' + url + '\n')


nextEl = driver.find_element(By.CSS_SELECTOR, '[title="下一页"]')
while (nextEl):
    parse()
    nextEl.click()
    nextEl = driver.find_element(By.CSS_SELECTOR, '[title="下一页"]')
