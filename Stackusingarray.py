class stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,value):
        self.top=+1
        self.stack.append(value)
    
    def pop(self):
        if self.top == - 1:
            print("Stack is Underflow")
        self.stack.pop()
    def peek(self):
        return self.stack[self.top]
    
    def print_stack(self):
        print(self.stack)



s=stack()
s.push(5)
s.push(6)
s.push(8)
s.push(9)
s.print_stack()