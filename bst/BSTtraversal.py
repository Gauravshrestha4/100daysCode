class BinaryTree:                                 #       13
    def __init__(self,value):                     #      / \
        self.value=value                          #     9   27  
        self.left=None                            #    / \ /  \
        self.right=None                           #   2  1118    49


def inorderTraversal(root):
    if root is None:
        return 
    else:
        inorderTraversal(root.left)
        print(root.value)
        inorderTraversal(root.right)

def preorderTraversal(root):
    if root is None:
        return 
    else:
        print(root.value)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def postOrderTraversal(root):
    if root is None:
        return 
    else:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.value)

inorderTraversal(root)
preorderTraversal(root)
postOrderTraversal(root)