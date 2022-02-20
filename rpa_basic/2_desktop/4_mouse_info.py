import pyautogui
#pyautogui.FAILSAFE =False
pyautogui.PAUSE = 1  #모든 동작에 1초씩 sleep 적용 
#pyautogui.mouseInfo()

# 자동화 작업을 끌려면 마우스를 모서리 쪽으로 가져가라 
for i in range(5):
    pyautogui.move(100,100)
    pyautogui.sleep(1)