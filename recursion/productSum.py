# Time O(n) | Space O(d) 
def productSum(arr,depth=1):
    prodSum=0
    for x in range(len(arr)):
        if isinstance(arr[x],list):
            prodSum+=productSum(arr[x],depth+1)
        else:
            prodSum+=arr[x]
    return prodSum*depth

print(productSum([5,2,[7,-1],3,[6,[-13,8],4]],1))