import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = open('../data/data/alice.txt', encoding='utf-8')
text = file.read()

wordcloud = WordCloud().generate(text)
# 이미지 정보를 리턴
plt.imshow(wordcloud, interpolation='bilinear')     # 이미지 좀 예쁘게 보간
plt.axis("off")     # x, y축 안 보이게
plt.show()



