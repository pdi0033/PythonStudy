from itertools import combinations

def solution(nums):
    answer = 0
    numList = list(combinations(nums, 3))
    for tNum in numList:
        n = sum(tNum)
        isPrime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                isPrime = False
                break
        if isPrime == True:
            print(f"{tNum}으로 소수가 됩니다.")
            answer += 1
    return answer

def isPrime(num):
    i = 2
    while i <= num/2:
        if num % i == 0:
            return False
        i += 1
    return True

def solution1(nums):
    answer = 0
    
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):   # 중복 허용 안 함
            for k in range(j+1, len(nums)):
                if isPrime(nums[i]+nums[j]+nums[k]):
                    answer += 1

    return answer

print(solution([1,2,3,4]))
print(1)
print()
print(solution([1,2,7,6,4]))
print(4)