def findFor(arr: list[int]) -> list[tuple]:
    result = []
    for i in range(0, len(arr)-1):
        n = -1
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                n = arr[j]
                break
        result.append((arr[i], n))
    result.append((arr[len(arr)-1], -1))
    return result

from stack import MyStack
def findStack(arr: list[int]) -> list[tuple]:
    result = []
    stack = MyStack(len(arr))
    for i in range(len(arr)-1, -1, -1):
        n = -1
        while not stack.isEmpty():
            n = stack.peek()
            if arr[i] > n:
                stack.pop()
                n = -1
            if arr[i] < n:
                break

        stack.push(arr[i])
        result.append((arr[i], n))
    return result
        

if __name__ == "__main__":
    a = [4, 5, 2, 25]
    b = [13, 7, 6, 12]

    print(findFor(a))
    print(findFor(b))

    print(findStack(a))
    print(findStack(b))