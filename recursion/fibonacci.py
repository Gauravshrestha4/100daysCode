# using recursion without memoization | O(2^n) Time | O(n) Space
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(37))

# using recursion with memoization | O(2^n) Time | O(n) Space
def fibonacciMemo(n,memoizedFibo):
    
    if n in memoizedFibo:
        return memoizedFibo[n]
    else:
        memoizedFibo[n]=fibonacciMemo(n-1,memoizedFibo)+fibonacciMemo(n-2,memoizedFibo)
        return memoizedFibo[n] 

# print(fibonacciMemo(37,{1:0,2:1}))

def fibo(n):
    lastTwo=[0,1]
    counter=3
    while counter<=n:
        nextFibo=lastTwo[0]+lastTwo[1]
        lastTwo[0],lastTwo[1]=lastTwo[1],nextFibo
        counter+=1
    return lastTwo[1] if n>1 else lastTwo[0]

print(fibo(37))
