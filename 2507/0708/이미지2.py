import PIL.Image as pilimg
import os       # 파이썬에서 os 명령어를 사용할 수 있게 해준다.
                # 디렉토리 검색해서 해당디렉토리의 파일 목록을 통째로
import matplotlib.pyplot as plt    # 모든 그래픽 출력은 모두 pyplot으로 해야 한다.
import numpy as np      # 이미지 읽어서 numpy 배열로 바꾸기

# 특정폴더의 이미지를 읽어서 전부 numpy 배열로 바꾸고 다 더해서 npz 파일로 저장하기
# 이미지(4차원, 3차원 이미지가 여러 장이라서)를 2차원 ndarray로 바꾸는 방법
path = "../data/images/animal"
fileNameList = os.listdir(path)     # 해당경로에 있는 모든 파일을 읽어서 파일 목록을 전달해준다.
# print(fileNameList)
imageList = []
for fileName in fileNameList:
    filePath = path + "/" + fileName
    temp = pilimg.open(filePath)
    # 이미지 크기 축소
    img = temp.resize( (80, 80) )   # tuple로 전달
    img = np.array(img)
    # print(img.shape)
    imageList.append(img)   # 리스트에 추가하자

np.savez("data1.npz", data=imageList)

data1 = np.load("data1.npz")["data"]
plt.figure( figsize=(20, 5) )
for i in range(1, len(data1)+1):
    plt.subplot(1, 11 , i)      # 차트의 공간을 1 by 10개로 나누고 1부터 번호 시작
    plt.imshow(data1[i-1])
plt.show()


# 해보기
path = "../data/images/mnist"
fileNameList = os.listdir(path)
imageList = []
for i in range(10):
    filePath = path + "/" + fileNameList[i]
    temp = pilimg.open(filePath)
    img = temp.resize( (80,80) )
    img = np.array(img)
    imageList.append(img)
np.savez("data2.npz", data=imageList)
data2 = np.load("data2.npz")["data"]
plt.figure(figsize=(20,5))
for i in range(1, len(data2)+1):
    plt.subplot(1, 10, i)
    plt.imshow(data2[i-1])
plt.show()


