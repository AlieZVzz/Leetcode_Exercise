def MirrorRecursively(self, root):
    root.left, root.right = root.right, root.left
    while root:
        MirrorRecursively(root=root.left)
        MirrorRecursively(root=root.right)
    
