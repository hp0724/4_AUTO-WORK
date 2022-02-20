from faulthandler import dump_traceback
import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 
# print(fw.title) #창의 제목 정보 
# print(fw.size) # 창의 크기 정보 
# print(fw.left,fw.top,fw.right,fw.bottom)
# pyautogui.click(fw.left+10,fw.top+20,duration=1)

# for w in pyautogui.getAllWindows():
#     print(w)

w=pyautogui.getWindowsWithTitle("설정")[0]
print(w)

if w.isActive == False: # 현재 활성화가 되지 않았다면 
    w.activate()

if w.isMaximized == False : # 현재 최대화가 되지 않았다면 
    w.maximize()

if w.isMinimized == False:
    w.minimize()

w.restore() # 화면 원복 

w.close() # 윈도우 닫기 
