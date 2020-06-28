
# method 1 using BFS | O(n) Time | O(n) Space
def invertBinaryTree(root):
    queue=[root]
    while len(queue):
        node=queue.pop(0)
        if node is None:
            continue
        swapLeftAndRightNode(node);
        queue.append(node.left)
        queue.append(node.right)

# methood 2 uisng recursion | O(n) Time | O(d) Space
def invertBinaryTree2(root):
    if root is None:
        return 
    swapLeftAndRightNode(root)
    invertBinaryTree2(root.left)
    invertBinaryTree2(root.right)

def swapLeftAndRightNode(node):
    node.right,node.left=node.left,node.right