def validateBST(tree):
    return validateBSTHelper(tree,float('-inf'),float('inf'))

def validateBSTHelper(node,minValue,maxValue):
    if node is None:
        return True
    if node.value<minValue or node.value>=maxValue:
        return False
    isLeftValid=validateBSTHelper(node.left,minValue,node.value)
    isRightValid=validateBSTHelper(node.right,node.value,maxValue)
    return isLeftValid and isRightValid
    