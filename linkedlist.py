class Node:
    def __init__(self,d,n=None,p=None):
        self.data = d 
        self.next_node = n
        self.prev_node = p
    
    def __str__(self):
        return ('(' + str(self.data) + ')')

class LinkedList:

    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def add(self, d):
        new_node = Node(d, self.root)
        self.root= new_node
        self.size =+1
    def find(self,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None
    
    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
            return False
        

    def show_lis(self):
        this_node = self.root
        while this_node is not None:
            print(this_node)
            this_node = this_node.next_node
        print('None')


mylist = LinkedList()
mylist.add(5)
mylist.add(6)
mylist.add(7)
mylist.add(8)
mylist.show_lis()

print("size="+str(mylist.size))
mylist.remove(6)
print("size="+str(mylist.size))
print(mylist.find(5))
print(mylist.root)