class BinaryTree:                                 #       2
    def __init__(self,value):                     #      / \
        self.value=value                          #     3   5  
        self.left=None                            #    / \ /  \
        self.right=None                           #   4  63    9
root=BinaryTree(2)                      
node11=BinaryTree(3)                  
node12=BinaryTree(5)                   
root.left=node11                        
root.right=node12
node21=BinaryTree(4)
node22=BinaryTree(6)
node23=BinaryTree(3)
node24=BinaryTree(9)
node11.left=node21
node11.right=node22
node12.left=node23
node12.right=node24

def maxPathSum(tree):
    _,maxSum=findMaxSum(tree)
    print(maxSum)

def findMaxSum(tree):
    if tree is None:
        return (0,0)
    
    leftMaxSumAsBranch,leftMaxSum=findMaxSum(tree.left)
    rightMaxSumAsBranch,rightMaxSum=findMaxSum(tree.right)
    maxChildSumAsBranch=max(leftMaxSum,rightMaxSum)
    value=tree.value
    maxSumAsBranch=max(maxChildSumAsBranch,maxChildSumAsBranch)
    maxSumAsRootNode=max(maxChildSumAsBranch,leftMaxSumAsBranch+rightMaxSumAsBranch+value)
    maxPathSum=max(maxSumAsRootNode,leftMaxSum,rightMaxSum)

    return (maxSumAsBranch,maxPathSum)

maxPathSum(root)