from threading import current_thread
from selenium import webdriver
import time
browser =webdriver.Chrome()
browser.maximize_window()
browser.get('https://shopping.naver.com/home/p/index.naver')

# 무선 마우스 입력 
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys("무선마우스")

time.sleep(1)

# 검색 버튼 클릭 
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# 스크롤 내리기 

# 지정한 위치로 스크롤 내리기 
# 모니터 높이인 1080 위치로 스크롤 내리기 
#browser.execute_script('window,scrollTo(0,1080)') # 1920 *1080

#화면 가장 아래로 스크롤 내리기 
#browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 동적 페이지 제일 마지막까지 내리기 

interval =2 # 2초에 한번씩 스크롤 내리기 

# 현재 문서 높이 가져와서 저장 
prev_height = browser.execute_script('return document.body.scrollHeight')

#반복 수행 
while True:
    #스크롤을 화면 가장아래로 내림 
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # 페이지 로딩 대기(2초)
    time.sleep(interval)

    #현재 문서 높이 
    curr_height =browser.execute_script('return document.body.scrollHeight')

    if curr_height == prev_height: #직전과 같으면 반복문 탈출 
        break
    
    prev_height = curr_height


# 맨위로 올리기
browser.execute_script('window,scrollTo(0,0)')

time.sleep(3)
browser.quit()