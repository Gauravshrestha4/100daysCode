# method 1 by bilding reversed string O(n^2) time | O(n) space  
def isPalindrome(str1):
    new_str=""
    for i in reversed(range(len(str1))):
        new_str+=str1[i]
    return new_str==str1

# method 2 by using array  O(n) time | O(n) space
def isPalindrome2(str1):
    new_str=[]
    for i in reversed(range(len(str1))):
        new_str.append(str1[i])
    return ''.join(new_str)==str1

# method 3 by using recursion  O(n) time | O(n) space
def isPalindrome3(str1):
    return str1[0]==str1[len(str1)-1] and isPalindrome(str1[1:len(str1)-1])

 
# method 4 by using two pointers O(n) time | O(1) space
def isPalindrome4(str1):
    ptr1=0
    ptr2=len(str1)-1
    while ptr1<ptr2:
        if(str1[ptr1]!=str1[ptr2]):
            return False
        ptr1+=1
        ptr2-=1
    return True

print(isPalindrome3("abccba"))