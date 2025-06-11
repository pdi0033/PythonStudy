"""
a = [1,2,3,4,5,6,7,8,9,10]
key = 8

1. (0+9)//2중간값 = 4번방	5	값이
2. (6+9)//2 = 7번방		8	두번 비교하고 찾기

없을 때
key=13
1. (0+9)//2	-  5
2. (6+9)//2	-  7번방이 8
3. (8+9)//2	-  8번방이 9
4. (9+9)//2	-  9번방이 10
5. (10+9)//2	-  not found
 
left = 0
right = 9

mid = (left + right) // 2
만일 값이 키값보다 크면 a[mid] > key		left = mid+1
만일 값이 키값보다 작으면 a[mid] < key	right = mid-1
찾았던지 left <= right 동안만
"""

def solution(a, key, left, right):
    a.sort()
    if left > right:
        return "Not Found"
    mid = (left + right) // 2
    if a[mid] == key:
        str = f"key값 {key}는 {mid}번 방에 있습니다."
        return str
    elif a[mid] > key:
        right = mid - 1
    elif a[mid] < key:
        left = mid + 1
    
    return solution(a, key, left, right) 

# 강사님 풀이
def binearSearch(arr, key): # 배여로가 키값
    #1. 정렬
    arr.sort()
    left = 0
    right = len(arr)-1
    
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] > key:
            right = mid - 1
        elif a[mid] < key:
            left = mid + 1
        elif a[mid] == key:
            return mid
    return -1

a = [1,2,3,4,5,6,7,8,9,10]
key = 8

print(solution(a, key, 0, len(a)-1))
print(solution(a, 13, 0, len(a)-1))
print(binearSearch(a, key))
print(binearSearch(a, 13))
