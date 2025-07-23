# 뷰티플스프를 이용해서 html파싱
# 로컬에 있는 문서를 읽어서 파싱하는 것만 진행한다.
# weather_table
import requests
import json     # 지금 오는 데이터는 json 형태의 문자열이다.
import pandas as pd
# 서버한테 정보를 보낼 때 get, post 방식이 있다.
# 누구한테나 허용됨.
url = "https://finance.daum.net/api/search/ranks?limit=10"
# 권한없이 남의 사이트 가서 데이터 퍼오면 안됨, 살짝 속이기 가능

# 마치 내가 브라우저를 통해 접근한 것처럼 속이기 - 다 먹히는 거 아님
custom_header = {
    "referer":"https://finance.daum.net/",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
df = pd.DataFrame(columns=["rank", "name", "tradePrice"])

text = ""
response = requests.get(url, headers=custom_header)     # 그래도 못가져오면 api 찾아봐야 한다.
if response.status_code == 200:
    text = json.loads(response.text)    # json.loads 함수를 써서 dict 타입으로 바꿔야 한다.
    print(text)
    print(type(text))

    dataList = text["data"]
    for item in dataList:
        data = dict()
        data["rank"] = item["rank"]
        data["name"] = item["name"]
        data["tradePrice"] = item["tradePrice"]
        df.loc[len(df)] = data

print("인기 검색")
print(df)


df2 = pd.DataFrame(columns=["sectorName", "name", "changeRate"])
url = "https://finance.daum.net/api/sector/wics?perPage=5&order=desc"
response = requests.get(url, headers=custom_header)     # 그래도 못가져오면 api 찾아봐야 한다.
if response.status_code == 200:
    text = json.loads(response.text)    # json.loads 함수를 써서 dict 타입으로 바꿔야 한다.
    print(text)
    print(type(text))

    dataList = text["data"]
    for item in dataList:
        data = dict()
        data["sectorName"] = item["sectorName"]
        data["name"] = item["includedStocks"][0]["name"]
        data["changeRate"] = item["changeRate"]
        df2.loc[len(df2)] = data

print("업종 상위")
print(df2)

df2.to_csv("업종상위.csv", encoding='utf-8-sig', index=False)