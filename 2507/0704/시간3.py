import pandas as pd
import numpy as np

d = pd.date_range(start="2025-07-04", end="2025-09-23")
print(d)

# period 필드와 freq 둘이 결합해서 일, 시간, 초 등으로 지정된다.
d = pd.date_range(start="2025-07-04", periods=30, freq='T')   # periods=기간, freq='D'
print(d)

d = pd.date_range(start="2025-07-04", periods=30, freq='W')   # periods=기간
print(d)

# 가짜데이터 생성방법
# np.random.randn 함수는 가우스 분포를 따르는 값을 랜덤하게 생성한다.
# 가운스분포를 따르는 실수값이 중요한 이유
# 통계학자 => 자연계에서 얻어지는 모든 값을 분석을 했다.
np.random.seed(0)       # 랜덤값이 일정하게 시트가 같으면 같은 랜덤값이 나온다. (0) ~ (2^16 - 1)
ts = pd.Series(np.random.randn(12), index=pd.date_range(start="2025-01-01", periods=12, freq='M'))
print(ts)
# 12 개의 가짜 데이터를 만들었음
# 날짜가 인덱스임

# resample 연산
ts = pd.Series(np.random.randn(100), index=pd.date_range("2025-07-04", periods=100, freq='D'))
print(ts.tail)      # 마지막 20개만 출력

print(ts.resample('W').mean())      # D(일일) -> W(주)형식으로 전환

