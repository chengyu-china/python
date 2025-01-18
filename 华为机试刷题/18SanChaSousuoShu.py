## 这一题用的全是递归大的方法。理解起来比较用容易。
## 创建类的操作是我不曾知道的。

# class Student():
#     def __init__(self,username, subject,score):
#         self.userName = username
#         self.subject = subject
#         self.score = score



import sys

N=int(input())
q=[]

for line in sys.stdin:
    for x in line.split():
        q.append(int(x))

class Node:
    def __init__(self,val):
        self.v=val
        self.mid=self.lchild=self.rchild=None


def create(node,v):
    if node==None:
        return Node(v)
    if node.v-500>v:
        node.lchild=create(node.lchild,v)
    elif node.v+500<v:
        node.rchild=create(node.rchild,v)
    else:
        node.mid=create(node.mid,v)
    return node
 
root=Node(q[0])

for i in range(1,len(q)):
    create(root,q[i])
 
def height(root):
    if root==None:
        return 0
    else:
        return max(height(root.lchild),height(root.rchild),height(root.mid))+1
 
print(height(root))
 