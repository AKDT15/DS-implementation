# Python 3 program to find the number 
# of nodes in looop in a linked list  
# if loop is present 
  
# Python Code to detect a loop and  
# find the length of the loop 
# Node defining class 
class Node: 
      
    # Function to make a node 
    def __init__(self, val): 
        self.data = val 
        self.next = None
      
# Linked List defining and loop  
# length finding class  
class LinkedList: 
      
    # Function to initialize the  
    # head of the linked list 
    def __init__(self): 
        self.head = None        
          
    # Function to insert a new  
    # node at the end  
    def AddNode(self, val): 
        if self.head is None: 
            self.head = Node(val) 
        else: 
            curr = self.head 
            while(curr.next): 
                curr = curr.next
            curr.next = Node(val) 
      
    def partition(self):
        pindex = self.head
        temp = self.head
        pivot = self.head
        count = 1
        while (pivot.next):
           pivot = pivot.next
           count += 1
        for i in range(1,count):
           if temp.data >= pivot.data:
              pivot_prev = temp
              a = temp.data
              temp.data = pindex.data
              pindex.data = a
              temp = temp.next
        b = pivot.data
        pivot.data = pindex.data
        pindex.data = b          
      

myLL = LinkedList() 
myLL.AddNode(10) 
myLL.AddNode(9) 
myLL.AddNode(7) 
myLL.AddNode(2) 
myLL.AddNode(8) 
myLL.partition()