import time
import pyautogui
import pyperclip
import pytesseract
from PIL import Image

# 等待时间到13.15
target_time = "11:55"
while time.strftime("%H:%M") != target_time:
    time.sleep(10)  # 每2秒检查一次

# 打开指定文件
file_path = r"E:\WEchat\WeChat.exe"
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write(file_path)
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(2)  # 等待打开程序

# 定位小程序图表


# 识别指定图片1.png#收藏
favorite_image = "1.png"
favorite_image2 = "收藏2.png"
favorite_position = pyautogui.locateCenterOnScreen(favorite_image)
if favorite_position:
    pyautogui.click(favorite_position)
    print("已找到收藏图标1")
elif favorite_image2:
    print("已找到收藏图标2")
else:
    print("无法找到收藏图标")

time.sleep(1)

# 识别指定图片2.png#门店二维码栏
store_image = "2.png"
store_position = pyautogui.locateCenterOnScreen(store_image)
if store_position:
    pyautogui.click(store_position)
else:
    print("无法找到门店二维码栏")

time.sleep(1)

# 模拟鼠标右键
pyautogui.rightClick()

time.sleep(1)

# 识别指定图片3.png#识别图中二维码
qr_code_image = "3.png"
qr_code_position = pyautogui.locateCenterOnScreen(qr_code_image)
if qr_code_position:
    pyautogui.click(qr_code_position)
else:
    print("无法找到二维码")

time.sleep(7)

# 识别图片搜索.png#搜索
dish1_image = "搜索.png" 
dish1_position = pyautogui.locateCenterOnScreen(dish1_image)
if dish1_position:
    pyautogui.click(dish1_position)
else:
    print("无法找到搜索")
time.sleep(3)



# 识别图片搜索框.png#搜索框
dish1_image = "搜索框.png"
dish1_position = pyautogui.locateCenterOnScreen(dish1_image)
print("已定位搜索框")
if dish1_position:
    pyautogui.doubleClick(dish1_position)
    pyautogui.doubleClick()
    print("已点击搜索框")
else:
    print("无法找到搜索框")
time.sleep(2)
pyperclip.copy("牛肚拌粉")#pyautogui无法输入中文，使用复制粘贴代替
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
print("搜索完成")
time.sleep(2)

# # 识别图片6.png#选品1、、、暂时改为输入菜品选品
# spicy_image = "拌粉.png"
# spicy_position = pyautogui.locateCenterOnScreen(spicy_image)
# if spicy_position:
#     pyautogui.click(spicy_position)
# else:
#     print("无法找到拌粉选项")
# time.sleep(1)

guige_img = "规格.png"
tianjia_img = "添加.png"
favorite_position  = pyautogui.locateCenterOnScreen(guige_img)
favorite_position1  = pyautogui.locateCenterOnScreen(tianjia_img)
if favorite_position:
    pyautogui.click(favorite_position)
    print("已点击规格")
elif favorite_position1:
    pyautogui.click(favorite_position1)
    print("已点击添加")
else:
    print("无法找到对应按钮")

time.sleep(1)
#选择口味
zhongla_img = "6.png"

favorite_position  = pyautogui.locateCenterOnScreen(zhongla_img)
if favorite_position:
    pyautogui.click(favorite_position)
    print("已点击重辣")
else:
    print("无法找到对应按钮")

time.sleep(1)

# 识别图片7.png加入购物车
cart_image = "7.png"
cart_position = pyautogui.locateCenterOnScreen(cart_image)
if cart_position:
    pyautogui.click(cart_position)
else:
    print("无法找到加入购物车按钮")

time.sleep(1)

# 识别图片8.png#选好了
finish_image = "8.png"
finish_position = pyautogui.locateCenterOnScreen(finish_image)
if finish_position:
    pyautogui.click(finish_position)
else:
    print("无法找到选好了按钮")


target_time = "12:00"
while time.strftime("%H:%M") != target_time:
    time.sleep(0.1)  # 每0.1秒检查一次
# 识别图片8.png#选好了
zhifu_image = "支付.png"
finish_position = pyautogui.locateCenterOnScreen(zhifu_image)
if finish_position:
    pyautogui.click(finish_position)
else:
    print("无法找到选好了按钮")
print("吃饭吃饭吃饭吃")

