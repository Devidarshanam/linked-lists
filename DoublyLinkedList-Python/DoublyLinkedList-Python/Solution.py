class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizee = 0

    def add(self, s):
        new_node = Node(s)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.sizee += 1

    def add_first(self, s):
        new_node = Node(s)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.sizee += 1

    def contains(self, s):
        current = self.head
        while current:
            if current.data == s:
                return True
            current = current.next
        return False

    def get_first(self):
        if self.head:
            return self.head.data
        return None


    def get_last(self):
        if self.tail:
            return self.tail.data
        return None
    
    def size(self):
        return self.sizee
    
    def remove(self):
        if not self.head:
            return None  
        temp = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.sizee -= 1
        return temp

    def remove_last(self):
        if not self.tail:
            return None
        temp = self.tail.data
        if self.head == self.tail: 
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.sizee -= 1
        return temp

    def get(self, ind):
        if ind < 0 or ind >= self.sizee:
            return None
        
        temp = self.head
        count = 0
        while count < ind:
            temp = temp.next
            count += 1
        return temp.data

    def clear(self):
        self.head = self.tail = None
        self.sizee = 0

    def __str__(self):
        if not self.head:
            return "DoublyLinkedList is empty"
        result = ""
        temp = self.head
        while temp:
            result += f"[{temp.data}]"
            if temp.next:
                result += "<->"
            temp = temp.next
        return result