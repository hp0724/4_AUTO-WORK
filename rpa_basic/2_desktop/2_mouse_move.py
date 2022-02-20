import pyautogui

# 절대 좌표로 마우스 이동 
#pyautogui.moveTo(100,100) # 지정한 위치(x, y) 로 마우스를 이동 
#pyautogui.moveTo(100,200,duration=0.5)
# pyautogui.moveTo(100,100,duration=0.25)
# pyautogui.moveTo(200,200,duration=0.25)
# pyautogui.moveTo(300,300,duration=0.25)

# 상대 좌표로 이동 (현재 커서가 있는 위치로 부터 )
# pyautogui.moveTo(100,200,duration=0.5)
# # 이전 위치 기준으로 이동
# print(pyautogui.position()) #point(x,y)
# pyautogui.move(100,200,duration=0.5) # 100, 200 기준으로 이동
# print(pyautogui.position()) #point(x,y)
# pyautogui.move(100,200,duration=0.5) # 200, 400 기준으로 이동
# print(pyautogui.position()) #point(x,y)

p=pyautogui.position()
print(p[0],p[1])
print(p.x,p.y)