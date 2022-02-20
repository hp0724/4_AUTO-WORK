'''
1.그림판 실행 (단축키 win+r 입력값 :mspaint) 및 최대화
2. 상단의 텍스트 기능을 이용하여 흰 영역 아무곳에다가 글자입력
 입력 :참 잘했어요 
3. 5 초 대기후 그림판 종료 
 이때 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료 

'''

import sys
import pyautogui
import pyperclip


pyautogui.hotkey("win","r") # 단축키 :win +r 입력 
pyautogui.write("mspaint")
pyautogui.press("enter") # 엔터 키 입력 
# 그림판 나타날 때까지 2초대기\
pyautogui.sleep(2)
fw = pyautogui.getWindowsWithTitle("제목 없음")[0]
if fw.isMaximized == False : # 현재 최대화가 되지 않았다면 
    fw.maximize()

pyautogui.sleep(1)
# 글자 버튼클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text,duration=0.5)
    
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
pyautogui.click(200,200,duration= 0.5)


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("참 잘했어요.")


# 5 초 대기후 그림판 종료 

pyautogui.sleep(5)

# 종료 
fw.close()
pyautogui.sleep(2)
pyautogui.press("n") #  저장하지 않음 


