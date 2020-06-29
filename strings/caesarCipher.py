# O(n) space | O(n) Time
def caeserCipherEncryptor(string,key):
    newletters=[]
    newKey=key%26
    for letter in string:
        newletters.append(getNewLetter(letter,key))
    
    return "".join(newletters)

def getNewLetter(letter,key):
    newLetter=ord(letter)+key

    return chr(newLetter) if newLetter<=122 else chr(96+newLetter%122)

print(caeserCipherEncryptor("xyz",2))