import pyautogui
# pyautogui.sleep(3) # 3초 대기 
# print(pyautogui.position())

# pyautogui.click(38,132,duration=1) # 64 ,17 좌표 클릭 
#pyautogui.click()
# mouse click 이 아래의 두개를 합친것 
# pyautogui.mouseDown()
# pyautogui.mouseUp()

#pyautogui.doubleClick()
#pyautogui.click(clicks=10)

# pyautogui.moveTo(100,100)
# pyautogui.mouseDown()
# pyautogui.moveTo(400,400)
# pyautogui.mouseUp()

# pyautogui.sleep(3) 
# pyautogui.rightClick() # 마우스 오른쪽 클릭 
# pyautogui.middleClick() # 마우스휠 

# pyautogui.sleep(3)
# print(pyautogui.position())
# # 상대좌표
# pyautogui.moveTo(869,152)
# #pyautogui.drag(100,0,duration=1) # 너무 빠른동작일경우 duration 설정 
# # 절대좌표
# pyautogui.dragTo(1269,152,duration=1)

pyautogui.sleep(3)
pyautogui.scroll(300) # 양수이면 위 방향으로 음수이면 아래방향 만큼 스크롤 



