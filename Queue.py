from collections import deque
class queue():
    def __init__(self):
        self.queue=deque()
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return None
    def __str__(self):
        return str(self.queue)
my_queue = queue()
my_queue.push(4)
print(my_queue)