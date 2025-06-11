"""
각 아이템은 무게 w, 가치 v를 가진다. 배낭에 담을 수 있는 최대 무게는 W
아이템은 쪼개서 담을 수 있다. 최대 가치를 구하시오. (그리디)

w = 50 : 이 배낭은 50kg까지 담을 수 있다
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)

당신은 무게 제한이 W인 배낭을 하나 가지고 있고,
N개의 아이템이 있다. 각 아이템은 다음과 같은 속성을 가진다:
value (가치): 아이템을 배낭에 넣었을 때 얻게 되는 이익
weight (무게): 아이템의 무게

이때, 각 아이템은 분할해서 넣을 수 있다.
가치를 최대로 담았을때 어느 정도 까지 담을 수 있는지?

목적: 배낭에 담을 수 있는 아이템들의 조합 중 총 가치(value)의 합을 최대화하는 것
가치/무게 비율로 아이템 정렬 (내림차순)
하나씩 넣되, 전체를 다 넣을 수 없으면 남은 용량만큼 비례해서 담는다.
누적 가치 합산 → 최종 정답
"""

def solution(items: list):
    w = 50
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    bag = []
    for item in items:
        if w > item[1]:
            bag.append(item)
            w -= item[1]
        else:
            temp = ((item[0]/item[1]*w), w)
            bag.append(temp)
            break
    value = 0
    for item in bag:
        value += item[0]
    print(f"가방에는 {bag}가 들어있고")
    print(f"가치는 총 {value}만큼 넣었습니다.")

def knapsack(items, w):
    # 가치밀도 기준 내림차순 정렬
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    #차례대로 배낭에 담기
    value = 0
    for i in range(0, len(items)):
        if items[i][1] < w:
            value += items[i][0]
            w -= items[i][1]
        else:
            # kg당 가치는 가치/무게
            kg = items[i][0] / items[i][1]
            value += kg * w
            w -= w
            break
    return value

items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
solution(items)
print()
print(knapsack(items, 50))