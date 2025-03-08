class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Deque:
    def __init__(self):
        self.head=None
        self.tail=None
        self.sizes=0

    def is_empty(self):
        if not self.head or self.sizes==0:
            return "true"
        else:
            return "false"
        
    def size(self):
        return self.sizes
    
    def add_first(self,item):
        # if item
        new_node=Node(item)
        if not self.head:
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.sizes+=1

    def add_last(self,item):
        new_node=Node(item)
        if not self.head:
            self.head=self.tail=new_node
        else:
           self.tail.next=new_node 
           self.tail=new_node
        self.sizes+=1

    def clear(self):
        self.head=self.tail=None
        self.sizes=0

    def remove_first(self):
        temp=self.head
        if not self.head:
            return "Deque is empty"
        else:
            self.head=self.head.next
            self.sizes-=1
            return temp.data

    def remove_last(self):
        # temp=self.tail.data
        if not self.head:
            return "Deque is empty"
        if self.head==self.tail:
            removed=self.head.data
            self.head=None
            self.tail=None
            self.sizes-=1
            return removed
        current=self.head
        while current.next != self.tail:
            current=current.next
        temp=self.tail.data
        self.tail=current
        self.tail.next=None
        self.sizes-=1
        return temp

    def iterator(self):
        current=self.head
        result=[]
        for _ in range(self.sizes):
            if current.data.isdigit():
                result.append(int(current.data))
            else:
                result.append(current.data)
            current=current.next
        return result

    def toString(self):
        return self.iterator()
    
def main():
    deq=Deque()
    try:
        while True:
            command=input().split()
            if command[0]=="Deque()":
                deq.clear()
                continue
            if command[0]=="isEmpty()" and len(command)==1:
                print(deq.is_empty())
            elif command[0]=="addLast()" and len(command)==2:
                deq.add_last(command[1])
            elif command[0]=="addFirst()" and len(command)==2:
                deq.add_first(command[1])
            elif command[0]=="size()" and len(command)==1:
                print(deq.size())
            elif command[0]=="removeFirst()" and len(command)==1:
                print(deq.remove_first())
            elif command[0]=="removeLast()" and len(command)==1:
                print(deq.remove_last())
            elif command[0]=="toString()" and len(command)==1:
                r=[]
                for i in deq.iterator():
                    r.append(i)
                for j in range(len(r)-1):
                    print(r[j],end=", ")
                print(r[-1],end="")
            else:
                break
    except EOFError:
        pass
if __name__=="__main__":
    main()
