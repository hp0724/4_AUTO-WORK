import pyautogui
# 이미지 위치 찾기 
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)
# # 윈도우 shift s

# plus_menu = pyautogui.locateOnScreen("plus.png")
# pyautogui.moveTo(plus_menu,duration=1)
# 윈도우 shift s

# screen =pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 똑같이 생긴게 두개 이상일경우 

# for i in pyautogui.locateAllOnScreen("checkBox.png"):
#     print(i)
#     pyautogui.click(i,duration=0.5)

# checkbox = pyautogui.locateOnScreen("checkBox.png")
# pyautogui.click(checkbox)





# 속도 개선 
# 1. grayScale  rgb 값을 gray 로 다 바꾸기 때문에 속도 향상 

# plus_menu = pyautogui.locateOnScreen("plus.png",grayscale=True)
# pyautogui.moveTo(plus_menu,duration=0.25)

# 2 . 범위 지정 


# plus_menu = pyautogui.locateOnScreen("plus.png",region=(1465,65,200,100))
# pyautogui.moveTo(plus_menu,duration=0.25)
#pyautogui.mouseInfo()
#1465,65
#1485,118

# 3. 정확도 조정 
# plus_menu = pyautogui.locateOnScreen("plus.png",confidence=0.7)
# pyautogui.moveTo(plus_menu)

# 자동화 대상이 바로 보여지지 않는 경우 
#file_menu_notepad =pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("실패 ")


# 1 계속 기다리기 
# while file_menu_notepad is None:
#     file_menu_notepad=pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_notepad)


# 2. 일정 시간동안 기다리기 (timeout)
import time
import sys 

# timeout = 5  # 5초 대기 
# start=time.time() # 시작 시간 설정 
# file_menu_notepad =None
# while file_menu_notepad is None:
#     file_menu_notepad=pyautogui.locateOnScreen("file_menu_notepad.png")
#     end= time.time() # 종료 시간 설정 
#     if end - start > timeout : # 지정한 5초를 초과하면
#         print("시간 종료 ")
#         sys.exit()

# pyautogui.click(file_menu_notepad)
def find_target(img_file,timeout=30):
    start = time.time()
    target=None 
    while target is None:
        target= pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start >timeout:
            break
    return target

def my_click(img_file, timeout=30): 
    target = find_target(img_file,timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f" [Time out: {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png",5)
