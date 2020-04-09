'''
Traversal
A universal way to do all three traversal iteratively (only one line change)
1. Since the visit of left is always before right in all three orders, right child is always added
    to stack earlier than left child
2. Adding cur to the stack for the second time is just to know when to add its value to res
'''

# Preorder Traversal: root -> L -> R
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(root, False)]
        res = []
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
                    stack.append((cur, True))
        return res

# Inorder Traversal: L -> root -> R
        stack = [(root, False)]
        res = []
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return res

# Postorder Traversal: L -> R -> root
        stack = [(root, False)]
        res = []
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
        return res
