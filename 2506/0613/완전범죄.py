from functools import lru_cache

def solution(info, n, m):
    answer = 0
    length = len(info)
    
    @lru_cache(maxsize=None)
    def find(n, m, i, aSum=0, bSum=0, who=""):
        if who == "A":
            aSum += info[i][0]
        elif who == "B":
            bSum += info[i][1]

        if aSum >= n or bSum >= m:  # 들킴
            return float('inf')
        if i >= (length-1):  #전부 돎
            return aSum
        
        # A가 가짐
        afind = find(n, m, i+1, aSum, bSum, "A")

        # B가 가짐
        bfind = find(n, m, i+1, aSum, bSum, "B")

        return min(afind, bfind)

    afind = find(n, m, 0, 0, 0, "A")
    bfind = find(n, m, 0, 0, 0, "B")
    
    SumList = [afind, bfind]
    print(SumList)
    answer = min(afind, bfind)
    if answer == float('inf'):
        return -1
    else:
        return answer

    
if __name__ == "__main__":
    print("결과값:", solution( [[1, 2], [2, 3], [2, 1]], 4, 4 ))
    print("기대값:", 2)
    aSumList = []
    print("결과값:", solution( [[1, 2], [2, 3], [2, 1]], 1, 7 ))
    print("기대값:", 0)
    aSumList = []
    print("결과값:", solution( [[3, 3], [3, 3]], 7, 1 ))
    print("기대값:", 6)
    aSumList = []
    print("결과값:", solution( [[3, 3], [3, 3]], 6, 1 ))
    print("기대값:", -1)
    aSumList = []
    print("결과값:", solution( [[2, 1], [1, 3], [3, 2]], 5, 5 ))
    print("기대값:", 1)