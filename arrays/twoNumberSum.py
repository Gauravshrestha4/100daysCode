# method 1 using 2 for loops Time complexity O(n^2) | Space complexity O(1)
def twoNumberSum(arr,targetSum):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==targetSum:
                return [arr[i],arr[j]]
    return []
# method 2 using hash function Time complexity O(n) | Space complexity O(n)
def twoNumberSum2(arr,targetSum):
    hashMap={}
    for num in arr:
        if targetSum-num in hashMap:
            return [num,targetSum-num]
        else:
            hashMap[num]=True
    return []
# method 3 using sortTime complexity O(nlogn) | Space complexity O(n)
def twoNumberSum3(arr,targetSum):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        currentSum=arr[left]+arr[right]
        if currentSum==targetSum:
            return [arr[left],arr[right]]
        elif currentSum>targetSum:
            right-=1
        else:
            left+=1
    return []
print(twoNumberSum3([5,3,-2,6,-1,11],2))

