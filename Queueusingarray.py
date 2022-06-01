class Queue:
    def __init__(self,size=10):
        self.queue=[]
        self.size= size
        self.front=0
        self.rear=0
    
    def enqueue(self,value):
        if self.size == self.rear:
            print("Queue is Full")
        self.queue.append(value)

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is Empty")
        else:
            self.queue.pop()
    def display_queue(self):
        print(self.queue)

q=Queue()

q.enqueue(19)
q.enqueue(29)
q.enqueue(89)
q.display_queue()

q.dequeue()
q.display_queue()

