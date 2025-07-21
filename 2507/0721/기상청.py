# 뷰티플스프를 이용해서 html파싱
# 로컬에 있는 문서를 읽어서 파싱하는 것만 진행한다.
# weather_table
import requests
# 서버한테 정보를 보낼 때 get, post 방식이 있따.
url = "https://www.weather.go.kr/w/observation/land/city-obs.do"
response = requests.get(url)
if response.status_code == 200:
    text = response.text
    # print(text)

# 파싱하기
from bs4 import BeautifulSoup
import pandas as pd
doc = BeautifulSoup(text, "html.parser")
table = doc.find("table", {"id":"weather_table"})
trList = table.find_all("tr")   # tr 태그는 여러 개라서 find_all로 가져오자

df = pd.DataFrame(columns=["cityName", "nowWeather", "temperature", "humidity"])
i = 0
for tr in trList:
    mydic = {}
    if len(tr.find_all("td")) > 0:
        th = tr.find("th")      # find 쓴 이유는 한 개밖에 없어서 굳이 배열로 가져올 필요가 없다.
        mydic["cityName"] = th.text
        tdList = tr.find_all("td")  # 이 경우에는 index를 이용한 접근이 가능하다.
        mydic["nowWeather"] = tdList[0].text
        mydic["temperature"] = tdList[4].text
        mydic["humidity"] = tdList[8].text
        # print(mydic)

        df.loc[len(df)] = mydic

print(df)



