def stringReverse(str1):
    if(len(str1)==1):
        return str1
    else:
        return stringReverse(str1[1:])+str1[0]

print(stringReverse('gaurav'))