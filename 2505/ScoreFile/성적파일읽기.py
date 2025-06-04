# 한글처리 cp949 - 윈도우방식, 표준: utf-8, vscode: utf-8
f = open("score.txt", "r", encoding="utf-8")
lines = f.readlines()

# 뒤의 \n 삭제
for line in lines:
    if '\n' in line:
        line = line[:len(line)-1]
    words = line.split(",")
    name = words[0]
    kor = words[1]
    eng = words[2]
    mat = words[3]
    total = int(kor) + int(eng) + int(mat)
    avg = total / 3
    print(name, kor, eng, mat, total, avg, sep='\t')