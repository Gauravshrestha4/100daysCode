
# Time complexity O(nlogn + mlogm)  | space complexity O(1)
def smallestDiff(arr1,arr2):
    arr1.sort()
    arr2.sort()
    i=0
    j=0
    smallestDiff=float('inf')
    currentDiff=float('inf')
    smallestPair=[]
    while i<len(arr1) and j<len(arr2):
        firstNum=arr1[i]
        secondNum=arr2[j]
        if firstNum<secondNum:
            currentDiff=secondNum-firstNum
            i+=1
        elif secondNum<firstNum:
            currentDiff=firstNum-secondNum
            j+=1
        else:
            return [firstNum,secondNum]
        if smallestDiff>currentDiff:
            smallestDiff=currentDiff
            smallestPair=[firstNum,secondNum]
        
    return smallestPair


print(smallestDiff([-3,15,7,12,8],[19,15,16,11,22]))