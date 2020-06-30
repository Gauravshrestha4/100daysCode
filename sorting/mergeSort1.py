def mergeSort(arr):
    if len(arr)==1:
        return arr
    middleIndex=len(arr)//2
    leftSection=arr[:middleIndex]
    rightSection=arr[middleIndex:]
    return mergeSortedArrays(mergeSort(leftSection),mergeSort(rightSection))

def mergeSortedArrays(leftSection,rightSection):
    sortedArr=[None]*(len(leftSection)+len(rightSection))
    i=j=k=0
    while i<len(leftSection) and j <len(rightSection):
        if(leftSection[i]<rightSection[j]):
            sortedArr[k]=leftSection[i]
            i+=1
        else:
            sortedArr[k]=rightSection[j]
            j+=1
        k+=1
    while i<len(leftSection):
        sortedArr[k]=leftSection[i]
        i+=1
        k+=1
    while j<len(rightSection):
        sortedArr[k]=rightSection[j]
        j+=1
        k+=1
    return sortedArr

print(mergeSort([9,4,2,6,3,1,7]))

