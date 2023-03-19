from collections import deque
def PrintTreeFromTopToBottom(root):
    queue = deque([root])
    ans = []
    while queue:
        tree = queue.popleft()
        if tree:
            ans.append(tree.val)
            queue.append(tree.left)
            queue.append(tree.right)
    return ans
