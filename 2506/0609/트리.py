class TreeNode:
    def __init__(self, data=None):
        self.data = data 
        #self.edge=[]
        self.left=None 
        self.right=None 

def inorder(node):
    if node: #None이 아니면의 의미 
        inorder(node.left) 
        print(node.data, end="\t")
        inorder(node.right) 

def preorder(node):
    if node: #None이 아니면의 의미 
        print(node.data, end="\t")
        preorder(node.left) 
        preorder(node.right)

def postorder(node):
    if node: #None이 아니면의 의미 
        postorder(node.left) 
        postorder(node.right)   
        print(node.data, end="\t")     
#클래스를 안만들면 
  
def insertNode(data=None):
    #트리에 추가되기 위해서 노드를 하나 만든다. 
    newNode = TreeNode(data)
    if root ==None:
        root = newNode
    # ABCDEFGHIJKLMN  <--------------- 
    # queue에 root 를 (parent입력하고)
    # queue에서 첫번째 root 가 나오면 root.left 가 None이면 추가 아니면 root.left를 큐에추가 
    # root.right 도 확인 None이면 여리가 붙이면 다시 root.right 를 큐에 넣는다 
    #          
    #내가 루트노드
    #내가 어디에 끼어들어갈지 
     
""" 
큐를 이용한 레벨order - 너비우선탐색 
1.큐를 초기화한다.데큐를 써도 된다. 
2.  무조건 큐에 node하 넣고 
3. 큐가 비어 있지 않은 동안 반복한다. 
    3-1 큐로부터 무조건 하나 가져온다 
    3-2 데이터를 출력한다
    3-3 가지고 온 노드의 left가 None이 아니면 큐에 넣는다 
    3-4 가지고 온 노드의 right가 None이 아니면 큐에 넣는다 
"""
from collections import deque

def levelorder(node): #너비 탐색 
    queue = deque() #큐를 하나 만든다. 
    queue.appendleft( node ) #root 
    while len(queue)!=0: #큐가 empty 때까지
        current = queue.pop() 
        print(current.data, end="\t")
        if current.left != None:
            queue.appendleft( current.left )
        if current.right !=None:
            queue.appendleft( current.right )

#addNode : 부모 노드와 원하는 방향을 부여하고 데이터를 주면 그 위치에 노드를 추가하는 함수
#bLeft 값이 True이면 왼쪽으로 붙이고 False면 오른쪽으로 붙이려고 한다
root = None # list, dict 은 가능 
def addNode(parent=None, left=True, data=None):
    global root #전역변수, 함수 외부에서 변수에 접근 불가능  

    temp = TreeNode(data)
    if parent == None:
        root = temp 
    else:
        if left:
            parent.left = temp 
        else:
            parent.right = temp 

    return temp 

def makeTree1():
    root = addNode(None, True, data="A")#parent를 값을 안주면 디폴트로 None 이 들어감 

    level1 = addNode(root, True, "B")
    level2 = addNode(root, False, "C")

    addNode(level1, True, "D")
    addNode(level1, False, "E")

    addNode(level2, True, "F")
    addNode(level2, False, "G")
    
"""
    1.큐만들기 
    2.큐에 root 노드 추가 
        3. 추가될 위치 찾기 - 낑겨들어갈 위치찾기, 추가될때까지 
            3-1. 큐에서 하나 가져온다 
            3-2  가져온 노드의 left 가 None이면 여기에 추가하고 종료 
                None이 아니면 left값을 다시 큐에 넣는다 
            3-3  가져온 노드의 right 가 None이면 여기에 추가하고 종료 
                None이 아니면 right값을 다시 큐에 넣는다 
            
4. 모든 요소가 추가될때까지 1,2,3 을 반복한다. 

"""
# makeTree2("ABCDEFGHIK")
def makeTree2(simbol):
    global root 
    
    for c in simbol: #
        q = deque() #큐만들기 
        if root == None:
            root = TreeNode(c)
            continue  #반복구조에서 continue 아래 문장 건너뛰고, 다시 조건식으로 이동
                      #else 구문 쓰기 싫음 
        q.appendleft(root)
        #내가추가될때까지 
        append = False 
        while not append:
            node = q.pop() 
            if node.left ==None:
                addNode(node, True, c)
                append = True 
            elif node.right ==None:
                addNode(node, False, c)
                append = True   
            else:
                q.appendleft(node.left)
                q.appendleft(node.right) 

if __name__ == "__main__":
    # root = TreeNode("A")
    # root.left = TreeNode("B")
    # root.right = TreeNode("C")
    # root.left.left=TreeNode("D")
    # root.left.right=TreeNode("E")
    # root.right.left=TreeNode("F")
    # root.right.right=TreeNode("G")
    #makeTree("ABCDEFGHIJKL")
    #makeTree1()
    makeTree2("ABCDEFGHIK")

    print("inorder : ", end="\t")
    inorder(root)
    print() 

    print("preorder : ", end="\t")
    preorder(root)
    print() 
    
    print("postorder : ", end="\t")
    postorder(root)
    print() 
    
    print("levelorder : ", end="\t")
    levelorder(root)
    print() 
    
    #스택이나 큐, 시스템이 제공하는 큐를 쓰자 - 재귀호출 

# from collections  import deque 
# q = deque()
# q.appendleft('A')
# q.appendleft('B')
# q.appendleft('C')
# q.appendleft('D')

# print(len(q) )
# print(q.pop())
# print(len(q) )
# print(q.pop())
# print(len(q) )
# print(q.pop())
# print(len(q) )