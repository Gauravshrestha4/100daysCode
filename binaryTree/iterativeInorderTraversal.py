def iterativeInorderTraversal(tree):
    currentNode=tree
    prevNode=None
    while tree is not None:
        if prevNode is None or prevNode==currentNode.parent:
            if currentNode.left is not None:
                nextNode=currentNode.left
            else:
                print(currentNode.value)
                nextNode=currentNode.right if currentNode.right is not None else currentNode.parent

        elif prevNode==currentNode.left:
            print(currentNode.value)
            nextNode=currentNode.right if currentNode.right is not None else currentNode.parent
        else:
            nextNode=currentNode.parent

        prevNode=currentNode
        currentNode=nextNode

