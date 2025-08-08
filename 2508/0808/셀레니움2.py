# conda install selenium
# 이전에는 드라이브 파일을 다운 받아서 연결하는 방식

from selenium import webdriver
from selenium.webdriver.chrome.options import Options   # 브라우저를 처음 작동시킬 때 옵션을 줄 수 있다.
from selenium.webdriver.common.by import By     # 파싱도구
from selenium.webdriver.common.keys import Keys # 키값 제어 라이브러리
import time
from bs4 import BeautifulSoup

# 1. Options 객체를 만들어서 크롬드라이버의 기본 설정을 관리한다.
chrome_options = Options()
# chrome_options.add_argument("--window-size=1920,1000")  # 윈도우 크기 지정
chrome_options.headless = False     # 옵션은 챗GPT한테 물어보기
# 브라우저가 켜지고 작업완료를 하면 자동으로 닫힌다. - 그걸 막고 싶을 때 사용하는 옵션
chrome_options.add_experimental_option("detach", True)
# detach: 분리. attech: 접속.

# 2. 크롬 드라이버를 실행하고 옵션을 적용한다
driver = webdriver.Chrome(options=chrome_options)
# driver 객체가 브라우저를 지칭함
driver.implicitly_wait(3)       # 페이지가 열릴 때까지 3초쯤 기다려라. 페이지가 없어도.
# driver.get("http://www.daum.net")
driver.get("http://www.python.org")

# assert 디버깅 툴. 타이틀 안에 파이썬이 있는지 묻고 있따.
assert "Python" in driver.title

input_box = driver.find_element(By.NAME, "q")   # 내가 name 속성을 이용해서 찾을 거다. name이 q다.
time.sleep(2)   # 프로세스가 cpu를 2초간 뺏긴다.

# input_box에 키값을 보냄
input_box.send_keys("python")   # 키보드 이벤트를 발생시킴
time.sleep(3)   # 프로세스가 cpu를 2초간 뺏긴다.
# input_box.submit()      # 서버로 정보를 전송
# 웹개발자들이 커서가 있는 곳에서 엔터키를 누르면 서버로 전송한다.
input_box.send_keys(Keys.RETURN)    # Keys 엔터키를 누른다.
# 내부적으로 엔터키를 누르면 => submit 함수가 호출되게 해 놓았을 때 동작함.

# 셀레니움도 문서를 불러올 수 있다. page_source: html 페이지
doc = driver.page_source    # 불러온 웹페이지 정보가 여기에 있다.
# print(doc)
soup = BeautifulSoup(doc, "html.parser")

ul = soup.find("ul", {"class": "list-recent-events menu"})
if ul == None:
    print("못 찾았습니다.")
    driver.quit()
    exit()      # 프로그램 종료

liList = ul.find_all("li")
for item in liList:
    print(item.text)

# driver.quit()       # 종료


