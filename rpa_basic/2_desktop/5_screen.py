import pyautogui
# 스크린샷 찍기 
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장 

#pyautogui.mouseInfo()

#34,61 68,173,243 #44ADF3
pixel =pyautogui.pixel(34,61)
print(pixel)

#print(pyautogui.pixelMatchesColor(34,61,(68,173,243)))
print(pyautogui.pixelMatchesColor(34,61,pixel))