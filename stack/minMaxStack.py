class MinMaxStack:
    def __init__(self):
        self.stack=[]
        self.minMaxStack=[]
        
    # O(1) time | O(1) space
    def push(ele):
        newmMinMax={'min':ele,'max':ele}
        if len(self.minMaxStack):
            lastMinMax=self.minMaxStack[len(self.minMaxStack)-1]
            newmMinMax['min']=min(lastMinMax['min'],ele)
            newmMinMax['max']=min(lastMinMax['max'],ele)
        self.minMaxStack.append(newmMinMax)
        self.stack.append(ele)

    # O(1) time | O(1) space
    def pop():
        self.minMaxStack.pop()
        return self.stack.pop()
    
    # O(1) time | O(1) space
    def peek():
        return self.stack[len(self.stack)-1]

    # O(1) time | O(1) space
    def getMin():
        return self.minMaxStack[len(self.minMaxStack)-1]['min']

    # O(1) time | O(1) space
    def getMax():
        return self.minMaxStack[len(self.minMaxStack)-1]['max']
