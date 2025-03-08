class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.sizes=0

    def add(self,s):
        new_node=Node(s)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            # new_node.prev=self.tail
            self.tail=new_node
            self.tail.next=self.head
            self.head.prev=self.tail
        self.sizes+=1

    def add_first(self,s):
        new_node=Node(s)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.tail.next=self.head
            self.head.prev=self.tail
        self.sizes+=1

    def contains(self,s):
        current=self.head
        for _ in range(self.sizes):
            if current.data==s:
                return True
            current=current.next
        return False
    
    def get_first(self):
        if self.sizes>0:
            return self.head.data
        else:
            return None
        
    def get_last(self):
        if self.sizes>0:
            return self.tail.data
        else:
            return None
        
    def size(self):
        return self.sizes
    
    def remove(self):
        if not self.head:
            return None
        temp=self.head.data
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            new_node=self.head.next
            self.head=new_node
            self.head.prev=None
            self.sizes-=1
            return temp
    
    def remove_last(self):
        if not self.head:
            return None
        temp=self.tail.data
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            self.sizes-=1
            return temp
        
    def get(self,ind):
        if ind<0 or ind>=self.sizes:
            return None
        current=self.head
        for _ in range(ind-1):
            current=current.next
        return current.data
    
    def clear(self):
        self.head=None
        self.tail=None
        self.sizes=0

    def __str__(self):
        if not self.head:
            return "CircularLinkedList is empty"
        result = ""
        temp = self.head
        for _ in range(self.sizes):
            result += f"[{temp.data}]"
            result+="<->"
            temp = temp.next
        return result.strip("<->")
    
    def is_circular(self):
        slow= self.head
        fast= self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

