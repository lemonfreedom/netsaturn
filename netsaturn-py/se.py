from selenium import webdriver
from selenium.webdriver.common.by import By
import time

address = 'https://vpnse.org/'

user = "legendnode@gmail.com"
pwd = "wo123456"
sleep = 10

contents = [
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
        "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
    {"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
     "content": "官网：https://netsaturn.com/"},
]

driver = webdriver.Chrome()
driver.get(address)

# 打开登录框
driver.find_element(By.CSS_SELECTOR, '.item-logIn button').click()

time.sleep(sleep)

# 输入账户
userInputEl = driver.find_element(
    By.CSS_SELECTOR, '.Modal-body input[name="identification"]')
userInputEl.clear()
userInputEl.send_keys(user)

# 输入密码
pwdInputEl = driver.find_element(
    By.CSS_SELECTOR, '.Modal-body input[name="password"]')
pwdInputEl.clear()
pwdInputEl.send_keys(pwd)

# 提交
driver.find_element(
    By.CSS_SELECTOR, '.Modal-body button[type="submit"]').click()


def interval():
    for i in range(5):
        time.sleep(120)
        # 刷新页面
        driver.refresh()
        print('刷新第 ' + str(i) + ' 次')


def send(content):
    time.sleep(sleep)

    # 打开新增
    driver.find_element(
        By.CSS_SELECTOR, '.item-newDiscussion .IndexPage-newDiscussion').click()

    time.sleep(sleep)

    # 输入标题
    titleInputEl = driver.find_element(
        By.CSS_SELECTOR, '.item-discussionTitle input')
    titleInputEl.clear()
    titleInputEl.send_keys(content['title'])

    # 输入内容
    contentInputEl = driver.find_element(
        By.CSS_SELECTOR, '.ComposerBody-editor textarea')
    contentInputEl.clear()
    contentInputEl.send_keys(content['content'])

    # 发送
    driver.find_element(
        By.CSS_SELECTOR, '.item-submit.App-primaryControl button').click()
    time.sleep(sleep)

    # 选择分类
    driver.find_element(
        By.CSS_SELECTOR, '.TagDiscussionModal-list li[data-index="7"]').click()

    driver.find_element(
        By.CSS_SELECTOR, '.TagDiscussionModal-list li[data-index="11"]').click()

    # 发送
    driver.find_element(
        By.CSS_SELECTOR, '.TagDiscussionModal-form-submit button').click()

    time.sleep(sleep)

    # 返回首页
    driver.find_element(
        By.CSS_SELECTOR, 'a[href="https://vpnse.org"]').click()
    time.sleep(sleep)

    print('发送成功')
    # 刷新
    interval()
    time.sleep(sleep)

# for content in contents:
#     send(content)


while(True):
    send({"title": "推荐一个机场，测试全时段稳定网速，大厂高成本服务器，性价比不错",
          "content": "官网：https://netsaturn.com/"},)
