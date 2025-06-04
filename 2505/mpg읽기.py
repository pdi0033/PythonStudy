# mpg.csv 파일 가져와서 실린더 개수 8 4 2 종류별 카운트하기
f = open("../mpg.csv", 'r')
lines = f.readlines()
f.close()

# 첫 줄은 타이틀이다.
titles = lines[0].strip().split(',')
lines = lines[1:]

cylinder_count = {}
for i in range(0, len(lines)):
    line = lines[i].strip().split(',')
    if line[1] not in cylinder_count.keys():
        cylinder_count[line[1]] = 1
    else:
        cylinder_count[line[1]] += 1

cylinder_count = dict(sorted(cylinder_count.items(), key=lambda item: item[0]))
for key in cylinder_count.keys():
    print(f"cylinders {key}: {cylinder_count[key]}")