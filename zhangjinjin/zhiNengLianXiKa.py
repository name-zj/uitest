# -*- coding:utf-8 -*-

# 备课系统智能练习卡

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
import time


# 显示等待 & 点击
def obvious_wait_click(driver, xpath, prompt):
    locat = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    driver.execute_script("arguments[0].click();", locat)


# 创建驱动实例
driver = webdriver.Chrome()
# 设置浏览器运行位置
# driver.set_window_position(600, 0)
driver.get("https://t3.learnta.cn/__api/wechat/public/qRcode/library/iSfAt8akJl1HyItK73905")
print("----->输入用户名")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[1]/input").send_keys("test")
print("----->输入账号")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[2]/input").send_keys("18301010101")
print("----->输入验证码")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[3]/input").send_keys("1111")
print("----->点击登录按钮")
obvious_wait_click(driver, "//*[@id='root']/div/form/a/span", "无法点击登录按钮")
print("----->登录")
# 记录题目数量
num = 0


# 判断是否是小结页
def small_knot_page(driver):
    fnext = 1
    try:
        print("----->不是题目页面")
        print("----->检测是否是小结页")
        obvious_wait_click(driver, "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div[2]/div/a[2]", "小结页下一题按钮")
        print("----->是小结页")
        # 是小结页则点击确定弹窗
        obvious_wait_click(driver, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button[2]", "无法点击小结页确认弹窗按钮")

        print("----->下一题")
    except:
        print("----->找不到下一题按钮")
        print("----->报告页")
        fnext = 0
    finally:
        return fnext


# 定义查询下一题按钮方法，1表示出现，0表示不出现
def find_next(driver):
    fnext = 1
    print("----->检测是否出现题目")
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/a[2]")), "该页面不是题目页面")
        print("----->检测是第 %d 题" % (num + 1))
    except:
        # 判断是否是小结页
        fnext = small_knot_page(driver)
    finally:
        return fnext
    # time.sleep(2)
    # s = driver.find_elements_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/a[2]")
    # if len(s) == 1:
    #     print("----->找到下一题按钮")
    #     return 1
    # elif len(s) == 0:
    #     print("----->判断是否是小结页")
    #     time.sleep(2)
    #     s1 = driver.find_elements_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/div/div/div[2]/div/a[2]")
    #     if len(s1) == 1:
    #         print("----->是小结页")
    #         obvious_wait_click(driver, "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div[2]/div/a[2]", "小结页下一题按钮")
    #         obvious_wait_click(driver, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button[2]", "无法点击确认弹窗按钮")
    #     elif len(s1) == 0:
    #         print("----->不是小结页")
    #         return 0


# 循环做题
while find_next(driver):
    try:
        print("----->点击第 %d 题提交按钮" % (num+1))
        obvious_wait_click(driver, "//*[@id='root']/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/a[2]", "无法点击提交按钮")

        print("----->点击确认弹窗按钮")
        obvious_wait_click(driver, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button[2]", "无法点击题目确认弹窗按钮")

        num = num +1
        print("----->第 %d 道题完成" % (num))

        time.sleep(1)
        print("----->点击下一题按钮")
        obvious_wait_click(driver, "//*[@id='root']/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/a[2]", "无法点击题目下一题按钮")
        time.sleep(1)
    except:
        traceback.print_exc()
        break


time.sleep(2)
driver.quit()
