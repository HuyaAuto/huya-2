# coding = utf-8
import random

from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome(executable_path="D:\Python\PythonTools\chromedriver.exe")
try:
    dr.get("https://www.huya.com/tonghua")
    # dr.get("https://www.huya.com/12214")
    dr.maximize_window()
    dr.implicitly_wait(10)
    print(dr.title)
    dr.find_element_by_id("nav-login").click()
    # wait = WebDriverWait(dr, 10)
    # element = wait.until(EC.alert_is_present)
    # if element:
    #     print("有")
    # else:
    #     print("没有")
    time.sleep(15)
    dr.find_element_by_id('J-room-chat-shield').click()
    while (1):
        BarrageList = dr.find_elements_by_xpath("(//ul[@class='chat-room__list']/li)")
        BarrageMsg = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                        "(//ul[@class='chat-room__list']/li)[" + str(
                                                                                            random.randint(0, len(
                                                                                                BarrageList))) + "]/div/span[@class='msg']")))
        dr.find_element_by_id('pub_msg_input').send_keys(BarrageMsg.text)
        time.sleep(10)
        dr.find_element_by_id('msg_send_bt').click()
        # 清空缓冲
        dr.find_element_by_id('pub_msg_input').clear()
        time.sleep(3)
        dr.find_element_by_id('pub_msg_input').send_keys("6666")
        time.sleep(10)
        dr.find_element_by_id('msg_send_bt').click()
        # 清空缓冲
        dr.find_element_by_id('pub_msg_input').clear()
        time.sleep(3)
        dr.find_element_by_id('pub_msg_input').send_keys("强啊")
        time.sleep(10)
        dr.find_element_by_id('msg_send_bt').click()
        # 清空缓冲
        dr.find_element_by_id('pub_msg_input').clear()
        time.sleep(3)
    dr.quit()
except Exception as e:
    print(e)
