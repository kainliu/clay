class Node(object):
    def __init__(self, x=0, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r

# bst
tree1 = Node(
    x=12, 
    l=Node(
        x=10, 
        l=Node(
            x=7,
            l=Node(2),
            r=Node(8)
        ), 
        r=Node(11),
    ),
    r=Node(
        x=19, 
        l=Node(14),
        r=Node(21)
    )
)


class Solution:
    count = 0
    def search(self, root, k1, k2):
        
        if not root:
            # None
            return []
        
        self.count += 1
        print self.count, k1, k2

        path = []
        if k1 <= root.x:
            # go left
            path.extend(self.search(root.l, k1, k2))
        if k1 <= root.x <= k2:
            path.append(root.x)
        if root.x <= k2:
            path.extend(self.search(root.r, k1, k2))

        return path

s = Solution()
print s.search(tree1, 8, 11)
# print s.search(tree1, 2, 10)
