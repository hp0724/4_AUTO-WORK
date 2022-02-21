from selenium import webdriver
import time
browser =webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult') #iframe 전환 

# cars 에 해당하는 element 찾고 드롭다운 내부에 있는 4번째옵션을 선택
# index 로 검색 

#elem =browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
#option[1] :첫번째 항목 
#option[2] :두번째 항목 

#elem.click()

# 완전 일치 텍스트 값을 통해서 검색 
# 옵션 중에서 텍스트가 audi인 항목 검색 
#elem =browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
#elem.click()

# 텍스트 값이 부분 일치하는 항목 선택 

elem =browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(),"Au")]')
elem.click()


time.sleep(2)

browser.quit()


