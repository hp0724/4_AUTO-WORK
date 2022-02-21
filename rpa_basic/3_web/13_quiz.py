'''
1.https://www.w3schools.com 접속
2.화면 중간 LEARN HTML 클릭 
3.상단 메뉴중 HOW TO 클릭
4. 좌측 메뉴중 Contact form 메뉴 클릭 
5. 입력란에 아래 값 입력 
    first name : 황
    last name: 수하
    country :korea
    subject =퀴즈 완료 
    *위 값들은 변수로 미리설정 
6. 5초 대기후 submit 클릭
7. 5초 대기후 브라우저 종료 
'''

from itertools import count
import time
from selenium import webdriver

#1.https://www.w3schools.com 접속
browser=webdriver.Chrome()
browser.get('https://www.w3schools.com')


# 2.화면 중간 LEARN HTML 클릭 
browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

#3.상단 메뉴중 HOW TO 클릭
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()

#4. 좌측 메뉴중 Contact form 메뉴 클릭 
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[117]').click()

firstname="황"
lastname="수하"
country="Canada"
subject="퀴즈완료"


#5.입력란에 아래 값 입력 

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(firstname)

browser.find_element_by_xpath('//*[@id="lname"]').send_keys(lastname)

browser.find_element_by_xpath('//*[@id="country"]/option[2]').click()
#browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}]'.format(country)).click()

browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)


#6.5초 대기후 submit 클릭
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()


#7. 5초 대기후 브라우저 종료 
time.sleep(5)
browser.quit()