"""
Problem (from Leetcode website):

Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, _sum):
	"""
	type root: TreeNode
	type _sum: int
	return type: boolean
	"""
	
	inLeftSide = False
	inRightSide = False
	
	if root.left != None:
		inLeftSide = hasPathSum(root.left, _sum - root.val) 
	
	if root.right is not None:
		inRightSide = hasPathSum(root.right, _sum - root.val)
	
	if root.left is None and root.right is None: # this is a leaf node
		if _sum == root.val:
			return True
	
	if inLeftSide or inRightSide:
		return True
		
	return False
	
##Testing

a = TreeNode(7)
b = TreeNode(2)
c = TreeNode(11)
c.left = a
c.right = b

d = TreeNode(4)
d.left = c

e = TreeNode(1)
f = TreeNode(4)
f.right = e

g = TreeNode(13)
h = TreeNode(8)
h.left = g
h.right = f

_root = TreeNode(5)
_root.left = d
_root.right = h

print hasPathSum(_root, 22) # should return True
print hasPathSum(_root, 7) # should return False
print hasPathSum(_root, 26) # should return True
print hasPathSum(_root, 5) # should return False

