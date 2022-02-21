from selenium import webdriver
import time
browser =webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
browser.switch_to.frame('iframeResult') #iframe 전환 

elem=browser.find_element_by_xpath('//*[@id="html"]') # 성공
elem.click()

elem2=browser.find_element_by_xpath('//*[@id="css"]') # 성공
elem2.click()

elem3=browser.find_element_by_xpath('//*[@id="javascript"]') # 성공
elem3.click()

browser.switch_to.default_content() #상위로 빠져 나옴

elem=browser.find_element_by_xpath('//*[@id="html"]') #실패

time.sleep(5)

browser.quit()