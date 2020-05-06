
# pip install binarytree
from binarytree import bst

tree = bst()  # generates random binary trees
print(" - generate a random tree from python lib-")
print(tree)

'''Method:
Using Depth first search we traverse the tree, the preorder 
is the desired method because it traverses 
the root or parent node -> left -> right  
In contrast inorder and postorder start from the leafs.

**Time complexity:
Traverses each element one time = O(n)
In detail:
T(n) = 2*T(n/2) + f(1) = O(n) + O(1) = O(n) where n = number of nodes
	T(n/2) = each subproblem size (left and right subtree) 
	O(1) for other operations no participating in the recursion: 
	comparison between left,right,parent and other operations like printing.

**Space complexity:  
	AVG:
	  2^0 = 1 Total nodes = 1
	+ 2^1 = 2 Total nodes = 3
	+ 2^2 = 4 Total nodes = 7
	+ 2^3 = 8 Total nodes = 15
	----
	log_2(2^(depth)) = log_2(Total nodes)
	=>  height = depth - 1 = log_2(total nodes)-1 = log_2(15)-1 = 3.9-1 = 2.9 

	**
	Space = O(2^height) = O(2^log_2(n)-1) = O(2^3) = O(16) = O(n)

	Worst case where the the tree flattened to a list: 
	O(n), n= number of nodes
'''

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums_ls = []
    branchSumsHelper(root, 0, sums_ls)
    return print("final array sums_ls:", sums_ls)


def branchSumsHelper(node, currentSum, sums_ls):
    print("node=", node)
    if node is None:
        print("node is None")
        return

    newCurrentSum = node.value + currentSum
    print("node.value=", node.value)
    print("currentSum=", currentSum)
    print("newCurrentSum=", newCurrentSum)
    if node.left is None and node.right is None:
        print('leaf->', node.value)
        sums_ls.append(newCurrentSum)
        print('sums_ls :', sums_ls)
    print('node.value=', node.value)
    print("node.left=", node.left)
    print("node.right=", node.right)
    preorder(node, newCurrentSum, sums_ls)

# *Import*:
# Recursion creates Subroutines and this stores EVERY variable's state in stack frame, so in every node the currentSum is saved.
def preorder(node, newCurrentSum, sums_ls):
    branchSumsHelper(node.left, newCurrentSum, sums_ls)
    print("i turn right...")
    branchSumsHelper(node.right, newCurrentSum, sums_ls)
    return

branchSums(tree)