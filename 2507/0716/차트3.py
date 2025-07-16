import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib import font_manager, rc
import seaborn as sns
#font_manager - 폰트를 폰트객체화 
#rc - 차트가 그려질 영역, 폰트를 지정할 영역 (차트영역)

# 상대경로지정 - 폰트를 복사해서붙여놔야 한다.
font_name = font_manager.FontProperties(fname="../fonts/Hancom Gothic Bold.ttf").get_name()
print(font_name)
#rc('font', family=font_name)

# seaborn의 스타일 설정을 rcParams 고치는 것보다 먼저 해야 한글이 안 깨진다.
sns.set_style('whitegrid')   # {darkgrid, whitegrid, dark, white, ticks}

plt.rcParams['font.family'] = font_name         # 이것만 설정하면 된다고 했는데
plt.rcParams['axes.unicode_minus']  = False     # 눈금에서 한글깨짐 문제 발생

# 히스토그램 - 분포도(통계학적으로 중요함)
# (loc: float = ..., scale: float = ..., size: None = ...) -> float
# loc : 평균          scale: 표준편차      size: 개수
# 예를 들어서 평균 70 편차가 20이다. 데이터 개수 500.
x = np.random.normal(loc=70, scale=20, size=500)
x = np.random.normal(size=1000)     # 정규분포가 되도록 데이터를 생성한다.

# 히스토그램 - seaborn의 displot 함수
sns.displot(x,
            bins=20,    # 구간개수
            kde=True,   # 커널밀도
            rug=False,  # 러그 표시 여부
            label='히스토그램'
            )
sns.utils.axlabel("value", "frequency")



plt.title('제목')
plt.xlabel('x축')
plt.ylabel('y축')
plt.legend(loc='best')  # 범주를 알아서 봐서 적당한 위치에 출력해라.
plt.show()

