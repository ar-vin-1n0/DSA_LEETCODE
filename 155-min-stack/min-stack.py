class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []        

    def push(self, value):
        self.stack.append(value)

        if not self.minstack:
            self.minstack.append(value)
        else:    
            new = min(value,self.minstack[-1])
            self.minstack.append(new)


    def pop(self):
        self.minstack.pop(),self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()