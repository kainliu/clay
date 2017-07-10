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

def p(*args):
    debug_print = 1
    if debug_print: print args

def solution(A):

    result = []
    def walk(node, count = 0, max_x = -1):

        if node is None:
            return count


        if node.x >= max_x:
            p("- node x:", node.x)
            p("count before!:", count)
            count += 1
            result.append(node.x)
            p("count after!:", count)

        current_max = max(max_x, node.x)

        # return walk(node.r, count, current_max) + walk(node.l, count,current_max)

        if node.r is not None:
            count = walk(node.r, count, current_max)
        if node.l is not None:
            count = walk(node.l, count, current_max)

        # if node.r is not None:
        

        return count

    print walk(A, count=0)
    print result


print solution(tree1)
print solution(tree2)




