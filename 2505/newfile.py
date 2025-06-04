file = open("데이터파일.txt", "w")  # 반환대상은 파일 객체
file.write("Hello") #출력이 파일로
file.close()

f = open("데이터파일2.txt", "w")
for i in range(1, 11):          #print 함수의 기본 출력 장치가 모니터인데,
    print(f"i={i}", file=f)     #file 객체를 주면 화면에 출력이 안 되고 파일로 출력한다.
print("작업완료")
f.close()   


f = open("데이터파일3.txt", "w")
for i in range(1, 11): 
    s = "i= %d\n" % (i)       # 파이선 2부터 있던 코드
    f.write(s)
print("작업완료")
f.close()


f = open("/doit/데이터파일4.txt", "w")
for i in range(1, 11): 
    s = "i= %d" % (i)       # 파이선 2부터 있던 코드
    f.writelines(s)         # 줄바꿈 해준다.
print("작업완료")
f.close()