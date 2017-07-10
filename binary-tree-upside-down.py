"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
"""

class Node(object):
    def __init__(self, val=0, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

Tree1 = Node(
    val = 1,
    l = Node(
        val = 2,
        l = Node(4),
        r = Node(5)
        ),
    r = Node(3)
    )

def printTree(T):
    # print 'T', T.val if T is not None else -1
    if T is not None:
        print 'Node:', T.val
        printTree(T.l)
        printTree(T.r)

def solution(A):

    # scan and build, two graphs
    def build(root, newRoot = None):
        # print 'root', root.val if root is not None else -1
        # print 'newRoot', newRoot.val if newRoot is not None else -1
        if root is None: # the end
            return newRoot

        if newRoot is None: # init
            newRoot = Node(root.val)
1/
        if root.l is None:
            return newRoot

        tmp = Node(
            val = root.l.val,
            l = root.r,
            r = newRoot
            )
        # print 'tmp', tmp.val if tmp is not None else -1
        # print 'tmp.l', tmp.l.val if tmp.l is not None else -1
        # print 'tmp.r', tmp.r.val if tmp.l is not None else -1
        newRoot = tmp
        return build(root.l, newRoot)

    return build(A)

printTree(Tree1)
print '---'
Tree2 = solution(Tree1)
printTree(Tree2)



### BFS PRINT TREE





