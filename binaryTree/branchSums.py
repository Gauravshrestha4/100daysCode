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
def branchSum(root):
    sumArr=[]
    calcBranchSum(root,0,sumArr)
    return sumArr
def calcBranchSum(node,runningSum,sumArr):
    if node is None:
        return
    newRunningSum=runningSum+node.value
    if node.left is None and node.right is None:
        sumArr.append(newRunningSum)
        return
    calcBranchSum(node.left,newRunningSum,sumArr)
    calcBranchSum(node.right,newRunningSum,sumArr)
print(branchSum(root))
    