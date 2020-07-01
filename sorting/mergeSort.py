def mergeSort(arr):
    if len(arr)<=1:
        return arr
    auxillaryArr=arr[:]
    mergeSortHelper(arr,0,len(arr)-1,auxillaryArr)

def mergeSortHelper(mainArray,start,end,auxillaryArr):
    if start==end:
        return
    middle=(start+end)//2
    mergeSortHelper(auxillaryArr,start,middle,mainArray)
    mergeSortHelper(auxillaryArr,middle+1,end,mainArray)
    doMerge(mainArray,start,middle,end,auxillaryArr)
    
def doMerge(mainArray,start,middle,end,auxillaryArr):
    i=start
    j=middle+1
    k=start
    while i<=middle and j<=end:
        if auxillaryArr[i]<=auxillaryArr[j]:
            mainArray[k]=auxillaryArr[i]
            i+=1
        else:
            mainArray[k]=auxillaryArr[j]
            j+=1
        k+=1
    while i<=middle:
        mainArray[k]=auxillaryArr[i]
        i+=1
        k+=1
    while j<=end:
        mainArray[k]=auxillaryArr[j]
        j+=1
        k+=1

mergeSort([9,4,2,6,3,1,7])

        