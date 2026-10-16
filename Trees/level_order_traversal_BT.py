import json
from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def build_tree(values):
    if not values or values[0] is None:
        return None
    root=TreeNode(values[0])
    q=deque([root])
    i=1
    while q and i<len(values):
        cur=q.popleft()
        if i<len(values) and values[i] is not None:
            cur.left=TreeNode(values[i])
            q.append(cur.left)
        i+=1
        if i<len(values) and values[i] is not None:
            cur.right=TreeNode(values[i])
            q.append(cur.right)
        i+=1
    return root

class solution:
    def level_order(self,root):
        if not root:
            return None
        res=[]
        q=deque([root])
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

def main():
    values=json.loads(input())
    root=build_tree(values)

    sol=solution()
    print(sol.level_order(root))

if __name__ == '__main__':
    main()