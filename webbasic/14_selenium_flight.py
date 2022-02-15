from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) # url로 이동



# 검색하기 출발 (서울)

browser.find_element_by_class_name("select_code__d6PLz").click()
browser.find_element_by_class_name("autocomplete_input__1vVkF").send_keys("서울")
time.sleep(1)
browser.find_element_by_class_name("autocomplete_locations__1lh0C").click()

# 검색하기 도착 (제주)
browser.find_element_by_css_selector("#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div.tabContent_routes__laamB > button.tabContent_route__1GI8F.select_City__2NOOZ.end > b").click()
browser.find_element_by_class_name("autocomplete_input__1vVkF").send_keys("제주")
time.sleep(1)
browser.find_element_by_class_name("autocomplete_locations__1lh0C").click()
# 가는 날 선택 클릭

# 가는 날 클릭
browser.find_element_by_class_name('tabContent_option__2y4c6').click()
month=browser.find_elements_by_css_selector('div.sc-jrsJWt.dJdFwe.awesome-calendar div.sc-kEqXSa.bAVzgZ.month') # 11월 ~ 2022년 12월까지의 month 데이터 추출[12월추출[]] 
go_weeks=month[1].find_elements_by_css_selector('table tbody tr') # 각 주차 별 데이터  [12월 데이터 추출] 
go_days=go_weeks[3].find_elements_by_css_selector('td')           # 각 일 별 데이터 추출(2주차의 일요일 ~ 월요일 데이터추출) 
go_days[4].click()   # 2주차의 3번째 일 클릭 
# day=days[1].find_element_by_css_selector('button')
 
#오는 날 클릭
back_weeks=month[1].find_elements_by_css_selector('table tbody tr') # 2022년 1월 1주 ~ 5주차 데이터 추출 
back_days=back_weeks[4].find_elements_by_css_selector('td') # 2022년 5주차의 일요일~월요일 데이터 추출
back_days[1].click()

# 항공권 검색
browser.find_element_by_css_selector("#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > button").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div[2]/div[2]")))
    # 성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()
# time.sleep(10)
# elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div[2]/div[2]/div/button")
# print(elem.text)
# browser.find_element_by_css_selector("#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div:nth-child(2) > button:nth-child(1)").click()

# time.sleep(1)
# browser.find_element_by_css_selector("#__next > div > div.container.as_main > div.modal_modal__1rTeN > div.modal_content__3hldE.modal_as_calendar__1jTVm > div.calendar_calendar__2OzxE > div.calendar_content__1Xc5a > div > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(4) > button")[15].click()
# time.sleep(1)
# browser.find_elements_by_link_text("16")[1].click()

# browser.find_element_by_link_text("가는 날").click()

# # 이번달 27일 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달