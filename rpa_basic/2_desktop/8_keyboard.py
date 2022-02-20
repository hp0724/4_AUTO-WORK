import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] #메모장 1개 띄운상태에서 정보 가져옴
w.activate()
# pyautogui.write("hello world")
# pyautogui.write("\n")
# pyautogui.write("12345",interval=1)
# pyautogui.write("수하")

#pyautogui.write(["t","e","s","left","left","right","l","a","enter"],interval=1)
# left right 로 위치 조정 interval로 시간조정 


# 특수 문자 
# shift 4 ->$   

# pyautogui.keyDown("shift") # shift 키를 누를 상태에서 
# pyautogui.press("4") # 숫자 4 입력하고 
# pyautogui.keyUp("shift") # shift 키를 뗀다

# w조합키 (hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
#pyautogui.hotkey("ctrl","a")
# ctrl 누르고 a 누르고 -> a 떼고 ctrl 떼고 

import pyperclip
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("수하")

# win = ctrl +alt +del 
