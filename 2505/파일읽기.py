f = open("데이터파일.txt", "r")
data = f.read()    #파일을 통으로 읽는다.
print(data)
f.close()

f = open("데이터파일2.txt", "r")
data = f.read()    #파일을 통으로 읽는다. str 타입으로 반환
print(type(data))
f.close()   #파일을 연다. 파일포인터 - 파일 읽을 위치값이 맨 뒤에 가 있다.

f = open("데이터파일3.txt", "r")
data = f.readlines()     #통으로 읽고 반환값이 list타입이다.
print(type(data))
print(data)
f.close()


f = open("데이터파일3.txt", "r")
line = f.readline()     #한줄씩 읽고 str 타입으로 반환
while line != "":
    print(type(line), line, end="")     #이미 text에 \n이 있어 print의 end='\n'은 필요없다.
    line = f.readline()     # 끝날 때까지 계속 읽어야 한다.
f.close()