class Node(object):
    def __init__(self, x=0, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r


tree1 = Node(x=8, 
    l=Node(x=2, l=Node(x=8), r=Node(x=5)), 
    r=Node(x=0, l=Node(x=1), r=Node(x=3))
    )

tree2 = Node(x=5,
    l=Node(x=8,
        l=Node(x=10,
            l=Node(x=12),
            r=Node(x=7)
            ),
        r=Node(x=6,
            l=Node(x=2),
            r=Node(x=9)
            )
        ),
    r=Node(x=7,
        l=Node(x=6),
        r=Node(x=9)
        )
    )


import sys


def solution(A):
    
    def walk(v, _max = -sys.maxint):
        if not v: 
            return 0
        count = 0
        if v.x >= _max: 
            count += 1
        _max = max(v.x, _max)    
        count += walk(v.l, _max)
        count += walk(v.r, _max)
        return count

    return walk(A)
    

print solution(tree1)
print solution(tree2)
