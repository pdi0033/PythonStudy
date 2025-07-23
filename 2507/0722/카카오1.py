# 키값: 123
# requests.get로 갖고 오는데
# KakaoAK 키값
# 커스텀헤터 키값은 "Authorization": "KakaoAK 키값"
"""
curl -v -G GET "https://dapi.kakao.com/v2/local/search/keyword.json?y=37.514322572335935&x=127.06283102249932&radius=20000" \
  -H "Authorization: KakaoAK ${REST_API_KEY}" \
  --data-urlencode "query=카카오프렌즈" 
"""

url = "https://dapi.kakao.com/v2/local/search/keyword.json?y=37.514322572335935&x=127.06283102249932&radius=20000"
url = url + "&query=카카오프렌즈"
custom_header = {"Authorization": "KakaoAK "}
import requests
import json
response = requests.get(url, headers=custom_header)
if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print(response)
    print("error")


