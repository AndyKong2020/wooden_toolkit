# 作者:明月清风我
# 时间:2022/5/19 22:22
# 说明:
# 请先安装pyautogui包，把要用来刷时长的视频放在屏幕中央，然后运行程序
# 请确保你的视频覆盖了屏幕中心1/10的区域，你可以按住ctrl然后滚动鼠标滚轮来放大视频，让它真的覆盖到了
# 鼠标会在这个区域内模拟人手随机操作
# 为了减少出错的概率，这个程序的效率并不高，不过你挂几个晚上肯定没问题
# 如果你想提高刷时长效率(现在大概在33.3%，也就是挂一小时时长增加20分钟)，针对你自己的电脑稍作优化就能接近100%，这个程序相当易于优化
# 遇到问题请反馈到QQ:243604572

import pyautogui
import time
import random

pyautogui.FAILSAFE = False # 这个操作防止程序卡死
manual_rot = (750, 582, 955, 695)
width, hight = pyautogui.size()
auto_rot = (0.45*width, 0.45*hight, 0.55*width, 0.55*hight)
rot = auto_rot
# 如果你不想倒腾这些代码，这个参数用auto就行
# 如果你想读读这些代码，改变manual_rot中的参数就能自己决定操作区域
escape = 1  # 在click被打印出后，你有escape秒的自由操作时间，你可以在这时停止运行

while True:
    start = time.clock()
    while True:
        #print(pyautogui.position())   # 得到当前鼠标位置，输出
        rdnum = random.random()
        target = (rot[0] + (rot[2] - rot[0])*rdnum, rot[1] + (rot[3] - rot[1])*rdnum)
        pyautogui.moveTo(target[0], target[1], duration = rdnum + 1)
        end = time.clock()
        if (end - start) > 5:
            #print(end - start)
            break
    pyautogui.click()
    print('click!')
    time.sleep(escape)
    #time.sleep(2835 + 5*rdnum)