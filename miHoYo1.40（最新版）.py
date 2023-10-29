import math
import os
import pyautogui
import time
import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
#设置文件位置
miHoYo_path = r"E:\Star Rail\Game\StarRail.exe"
#启动
os.startfile(miHoYo_path)
#等待60秒
time.sleep(60)
# 点击屏幕坐标（进入）
pyautogui.click(960,500)
#等待15秒
time.sleep(15)
#按下F4键（调出第四个）
pyautogui.press('F4')
#等待2秒
time.sleep(2)
#点击屏幕坐标（体力）
pyautogui.click(620,265)
#等待2秒
time.sleep(2)
# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()
# 获取屏幕截图
screenshot = pyautogui.screenshot()
# 将截图转为OpenCV图像格式
image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
# 裁剪出感兴趣区域
roi = image[85:110, 1405:1445]
# 将裁剪后的图像转为灰度图
gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
# 对图像进行二值化处理
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 使用Tesseract进行数字识别
math1 = pytesseract.image_to_string(binary, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
#等待2秒
time.sleep(2)
if math1.strip() == "":
    # 获取屏幕分辨率
    screen_width, screen_height = pyautogui.size()
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()
    # 将截图转为OpenCV图像格式
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    # 裁剪出感兴趣区域
    roi = image[85:110, 1415:1445]
    # 将裁剪后的图像转为灰度图
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # 对图像进行二值化处理
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # 使用Tesseract进行数字识别
    math1 = pytesseract.image_to_string(binary, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
#等待2秒
time.sleep(2)
# 截取屏幕指定区域
screenshot = ImageGrab.grab(bbox=(1585, 85, 1615, 110))
# 将截图保存为临时文件
screenshot.save('screenshot.png')
# 使用pytesseract进行OCR识别
math2 = pytesseract.image_to_string('screenshot.png', config='--psm 7')
# 等待2秒
time.sleep(2)
#点击屏幕坐标（赤）
pyautogui.click(520,620)
#等待2秒
time.sleep(2)
current_position = pyautogui.position()
# 设置起始点和目标点的坐标
start_x, start_y = 1200, 850
end_x, end_y = 1200, 180
# 移动鼠标到起始点
pyautogui.moveTo(start_x, start_y)
# 拖动鼠标到目标点
pyautogui.dragTo(end_x, end_y, duration=1.5)
#等待2秒
time.sleep(2)
#点击屏幕（传送）
pyautogui.click(1470,840)
#等待10秒
time.sleep(10)
#判断体力多少，做到全部清除
math = int(math1)
math3=int(4)
if math3==4:
    if math >=70:
        # 计算a的值
        a = int((math / 60)-1)
        #点击屏幕（+）循环点击5次
        for _ in range(5):
            pyautogui.click(1730,910)
            time.sleep(1)
        #等待2秒
        time.sleep(2)
        #点击屏幕（开始挑战）
        pyautogui.click(1530,980)
        #等待5秒
        time.sleep(5)
        #点击屏幕（开始挑战）
        pyautogui.click(1580,980)
        #等待200秒
        time.sleep(200)
        #点击屏幕（再来）a次
        for _ in range(a):
            pyautogui.click(1200,960)
            time.sleep(250)
        #等待5秒
        time.sleep(5)
        #点击屏幕（关闭）
        pyautogui.click(750,960)
        #等待10秒
        time.sleep(10)
        #按下F4键（调出第四个）
        pyautogui.press('F4')
        #等待2秒
        time.sleep(2)
        #点击屏幕坐标（体力）
        pyautogui.click(620,265)
        #等待2秒
        time.sleep(2)
        #点击屏幕坐标（赤）
        pyautogui.click(520,620)
        #等待2秒
        time.sleep(2)
        current_position = pyautogui.position()
        # 设置起始点和目标点的坐标
        start_x, start_y = 1200, 850
        end_x, end_y = 1200, 180
        # 移动鼠标到起始点
        pyautogui.moveTo(start_x, start_y)
        # 拖动鼠标到目标点
        pyautogui.dragTo(end_x, end_y, duration=1.5)
        #等待2秒
        time.sleep(2)
        #点击屏幕（传送）
        pyautogui.click(1470,840)
        #等待10秒
        time.sleep(10)
        #计算c的值
        c=int((math%60/10)-1)
        #点击屏幕（+）循环点击c次
        for _ in range(c):
            pyautogui.click(1730,910)
            time.sleep(1)
        #等待2秒
        time.sleep(2)
        #点击屏幕（开始挑战）
        pyautogui.click(1530,980)
        #等待5秒
        time.sleep(5)
        #点击屏幕（开始挑战）
        pyautogui.click(1580,980)
        #等待t秒
        t=int((c+1)*30)
        time.sleep(t) 
    else:
        if math>=10:
            b = int((math / 10)-1)
            #点击屏幕（+）循环点击b次
            for _ in range(b):
                pyautogui.click(1730,910)
                time.sleep(1)
            #等待2秒
            time.sleep(2)
            #点击屏幕（开始挑战）
            pyautogui.click(1530,980)
            #等待5秒
            time.sleep(5)
            #点击屏幕（开始挑战）
            pyautogui.click(1580,980)
            #等待s秒
            s=int((b+1)*30)
            time.sleep(s)
        else:
            #按下esc键
            pyautogui.press('Esc')
            #等待3秒
            time.sleep(3)
else:
    math4=int(4-math3)
    #等待2秒
    time.sleep(2)
    if math>=40:
        f=int((math/40)-math4)
        if f>=0:
            #按下esc键
            pyautogui.press('Esc')
            #等待3秒
            time.sleep(3)
            #按下F4键（调出第四个）
            pyautogui.press('F4')
            #等待2秒
            time.sleep(2)
            #点击屏幕坐标（体力）
            pyautogui.click(620,265)
            #等待2秒
            time.sleep(2)
            #点击屏幕（+）循环点击math4次
            for _ in range(math4):
                pyautogui.click(1660,100)
                time.sleep(1)
                pyautogui.click(1120,720)
                time.sleep(1)
                pyautogui.click(950,870)
                time.sleep(2)
            #点击屏幕坐标（赤）
            pyautogui.click(520,620)
            #等待2秒
            time.sleep(2)
            current_position = pyautogui.position()
            # 设置起始点和目标点的坐标
            start_x, start_y = 1200, 850
            end_x, end_y = 1200, 180
            # 移动鼠标到起始点
            pyautogui.moveTo(start_x, start_y)
            # 拖动鼠标到目标点
            pyautogui.dragTo(end_x, end_y, duration=1.5)
            #等待2秒
            time.sleep(2)
            #点击屏幕（传送）
            pyautogui.click(1470,840)
            #等待10秒
            time.sleep(10)
            math=int(math-40*math4)
            if math >=70:
                # 计算a的值
                a = int((math / 60)-1)
                #点击屏幕（+）循环点击5次
                for _ in range(5):
                    pyautogui.click(1730,910)
                    time.sleep(1)
                #等待2秒
                time.sleep(2)
                #点击屏幕（开始挑战）
                pyautogui.click(1530,980)
                #等待5秒
                time.sleep(5)
                #点击屏幕（开始挑战）
                pyautogui.click(1580,980)
                #等待200秒
                time.sleep(200)
                #点击屏幕（再来）a次
                for _ in range(a):
                    pyautogui.click(1200,960)
                    time.sleep(250)
                #等待5秒
                time.sleep(5)
                #点击屏幕（关闭）
                pyautogui.click(750,960)
                #等待10秒
                time.sleep(10)
                #按下F4键（调出第四个）
                pyautogui.press('F4')
                #等待2秒
                time.sleep(2)
                #点击屏幕坐标（体力）
                pyautogui.click(620,265)
                #等待2秒
                time.sleep(2)
                #点击屏幕坐标（赤）
                pyautogui.click(520,620)
                #等待2秒
                time.sleep(2)
                current_position = pyautogui.position()
                # 设置起始点和目标点的坐标
                start_x, start_y = 1200, 850
                end_x, end_y = 1200, 180
                # 移动鼠标到起始点
                pyautogui.moveTo(start_x, start_y)
                # 拖动鼠标到目标点
                pyautogui.dragTo(end_x, end_y, duration=1.5)
                #等待2秒
                time.sleep(2)
                #点击屏幕（传送）
                pyautogui.click(1470,840)
                #等待10秒
                time.sleep(10)
                #计算c的值
                c=int((math%60/10)-1)
                #点击屏幕（+）循环点击c次
                for _ in range(c):
                    pyautogui.click(1730,910)
                    time.sleep(1)
                #等待2秒
                time.sleep(2)
                #点击屏幕（开始挑战）
                pyautogui.click(1530,980)
                #等待5秒
                time.sleep(5)
                #点击屏幕（开始挑战）
                pyautogui.click(1580,980)
                #等待t秒
                t=int((c+1)*30)
                time.sleep(t) 
            else:
                b = int((math / 10)-1)
                #点击屏幕（+）循环点击b次
                for _ in range(b):
                    pyautogui.click(1730,910)
                    time.sleep(1)
                #等待2秒
                time.sleep(2)
                #点击屏幕（开始挑战）
                pyautogui.click(1530,980)
                #等待5秒
                time.sleep(5)
                #点击屏幕（开始挑战）
                pyautogui.click(1580,980)
                #等待s秒
                s=int((b+1)*30)
                time.sleep(s)
        else:
            g=int(math/40)
            #点击屏幕（+）循环点击g次
            for _ in range(g):
                pyautogui.click(1660,100)
                time.sleep(1)
                pyautogui.click(1120,720)
                time.sleep(1)
                pyautogui.click(950,870)
                time.sleep(2)
            h=int((math-40*g)/10)   
            #点击屏幕（+）循环点击h次
            for _ in range(h):
                pyautogui.click(1730,910)
                time.sleep(1)
            #等待2秒
            time.sleep(2)
            #点击屏幕（开始挑战）
            pyautogui.click(1530,980)
            #等待5秒
            time.sleep(5)
            #点击屏幕（开始挑战）
            pyautogui.click(1580,980)
            #等待250秒
            time.sleep(250)
    else:
        if math>=10:
            b = int((math / 10)-1)
            #点击屏幕（+）循环点击b次
            for _ in range(b):
                pyautogui.click(1730,910)
                time.sleep(1)
            #等待2秒
            time.sleep(2)
            #点击屏幕（开始挑战）
            pyautogui.click(1530,980)
            #等待5秒
            time.sleep(5)
            #点击屏幕（开始挑战）
            pyautogui.click(1580,980)
            #等待250秒
            time.sleep(250)
        else:
            #按下esc键
            pyautogui.press('Esc')
            #等待3秒
            time.sleep(3)
#等待5秒
time.sleep(5)
#点击屏幕（关闭）
pyautogui.click(750,960)
#等待10秒
time.sleep(10)
#按下esc键
pyautogui.press('Esc')
#等待3秒
time.sleep(3)
#点击屏幕（委托）
pyautogui.click(1640,350)
#等待2秒
time.sleep(2)
#点击屏幕（领取）
pyautogui.click(1400,870)
#等待2秒
time.sleep(2)
#点击屏幕（派遣）
pyautogui.click(1170,960)
#等待2秒
time.sleep(2)
#点击屏幕（选择）
pyautogui.click(680,380)
#等待2秒
time.sleep(2)
#点击屏幕（领取）
pyautogui.click(1400,870)
#等待2秒
time.sleep(2)
#点击屏幕（派遣）
pyautogui.click(1170,960)
#等待2秒
time.sleep(2)
#点击屏幕（切换）
pyautogui.click(740,290)
#等待2秒
time.sleep(2)
#点击屏幕（领取）
pyautogui.click(1400,870)
#等待2秒
time.sleep(2)
#点击屏幕（派遣）
pyautogui.click(1170,960)
#等待2秒
time.sleep(2)
#点击屏幕（选择）
pyautogui.click(680,380)
#等待2秒
time.sleep(2)
#点击屏幕（领取）
pyautogui.click(1400,870)
#等待2秒
time.sleep(2)
#点击屏幕（派遣）
pyautogui.click(1170,960)
#等待2秒
time.sleep(2)
#点击屏幕（关闭）
pyautogui.click(1750,65)
#等待2秒
time.sleep(2)
#点击屏幕（关闭）
pyautogui.click(1750,65)
#等待5秒
time.sleep(5)
#按下F2键（调出第2个）
pyautogui.press('F2')
#等待3秒
time.sleep(3)
#点击屏幕（切换）
pyautogui.click(960,95)
#等待2秒
time.sleep(2)
#点击屏幕（一键领取）
pyautogui.click(1590,885)
#等待2秒
time.sleep(2)
#点击屏幕（关闭）
pyautogui.click(1750,95)
#等待5秒
time.sleep(5)
#关闭应用程序
os.system("taskkill /im StarRail.exe /f")
#著作权归不吃鱼の喵所有


