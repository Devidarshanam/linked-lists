class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def add(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1

    def add_first(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.size+=1

    def contains(self,data):
        # new_node=Node(s)
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False

    def get_first(self):
        if not self.head:
            return None
        else:
            return self.head.data

    def get_last(self):
        if not self.tail:
            return None
        else:
            return self.tail.data
        
    # def size(self):
    #     return self.size
    
    def remove(self):
        if not self.head:
            return None 
        temp=self.head.data
        self.head=self.head.next
        if not self.head:
            self.tail=None
        self.size-=1
        return temp
    
    def remove_last(self):
        if not self.head:
            return None
        if self.head==self.tail:
            removed=self.head.data
            self.head=None
            self.tail=None
            self.size-=1
            return removed
        current=self.head
        while current.next != self.tail:
            current=current.next
        temp=self.tail.data
        self.tail=current
        self.tail.next=None
        self.size-=1
        return temp
    
    def get(self,ind):
        if ind<0 or ind>=self.size:
            return None
        current=self.head
        for _ in range(ind):
            current=current.next
        return current.data
    
    def find_middle(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    # def find_middle(self):
    #     if not self.head:
    #         return None
    #     if self.size%2!=0:
    #         x=self.size//2
    #         current=self.head
    #         for _ in range(x):
    #             current=current.next
    #         return current.data
    #     else: 
    #         x=(self.size//2)-1
    #         current=self.head
    #         for _ in range(x):
    #             current=current.next
    #         return current.data
    
    def nth_from_end(self, n):
        if n>=self.size or n<0:
            return None
        current=self.head
        for _ in range(self.size-n):
            current=current.next
        return current.data
    
    def insert_at_position(self,ind,s):
        if ind<0 or ind>self.size:
            return None
        new_node=Node(s)
        if ind==0:
            self.add_first(s)
            return
        current=self.head
        for _ in range(ind-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node
        if new_node.next is None:
            self.tail=new_node
        self.size+=1


    def insert_before(self,t,s):
        if not self.head:
            return None
        if self.head.data==t:
            self.add_first(s)
            return
        current=self.head
        while current.next and current.next.data != t:
            current = current.next
        if current.next:
            new_node = Node(s)
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def delete_after(self,t):
        current=self.head
        # temp=current
        while current and current.data != t:
            current=current.next
        if current and current.next:
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            self.size -= 1

    def clear(self):
        self.head=None
        self.tail=None
        self.size=0

    def to_string(self):
        if not self.head:
            return "LinkedList is empty"
        current=self.head
        result=[]
        while current:
            result.append(f"[{current.data}]")
            current=current.next
        return "".join(result)
    
    def __str__(self):
        return self.to_string()


        


