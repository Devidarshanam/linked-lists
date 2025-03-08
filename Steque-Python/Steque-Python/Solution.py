class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Steque:
    def __init__(self):
        self.head=None
        self.tail=None
        self.sizes=0

    def push(self, s):
        new_node=Node(s)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.sizes+=1

    def pop(self):
        temp=self.head.data
        if not self.head:
            return None
        else:
            self.head=self.head.next
            self.sizes-=1
            return temp
        
    def enqueue(self, s):
        new_node=Node(s)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.sizes+=1

    def size(self):
        return self.sizes
    
    def is_empty(self):
        if not self.head or self.sizes==0:
            return True
        return False
    
    def __str__(self):
        if not self.head:
            return "Steque is empty"
        result=""
        current=self.head
        while current:
            result+=f"[{current.data}]"
            current=current.next
        return "".join(result)
    
# *******************************

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Steque:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def push(self, s):
#         """Insert an element at the front."""
#         new_node = Node(s)
#         if self.isEmpty():
#             self.head = self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.size += 1

#     def pop(self):
#         """Remove and return the front element."""
#         if self.isEmpty():
#             return None
#         popped_data = self.head.data
#         self.head = self.head.next
#         self.size -= 1
#         if self.isEmpty():
#             self.tail = None
#         return popped_data

#     def enqueue(self, s):
#         """Insert an element at the end."""
#         new_node = Node(s)
#         if self.isEmpty():
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.size += 1

#     def peek(self):
#         """Return the front element without removing it."""
#         return None if self.isEmpty() else self.head.data

#     def getTail(self):
#         """Return the last element without removing it."""
#         return None if self.isEmpty() else self.tail.data

#     def contains(self, s):
#         """Check if the element exists in the steque."""
#         current = self.head
#         while current:
#             if current.data == s:
#                 return True
#             current = current.next
#         return False

#     def remove(self, s):
#         """Remove the first occurrence of the element."""
#         if self.isEmpty():
#             return False
#         if self.head.data == s:
#             self.pop()
#             return True
#         current = self.head
#         while current.next:
#             if current.next.data == s:
#                 if current.next == self.tail:
#                     self.tail = current
#                 current.next = current.next.next
#                 self.size -= 1
#                 return True
#             current = current.next
#         return False

#     def reverse(self):
#         """Reverse the steque."""
#         prev = None
#         current = self.head
#         self.tail = self.head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev

#     def clear(self):
#         """Remove all elements from the steque."""
#         self.head = self.tail = None
#         self.size = 0

#     def merge(self, another_steque):
#         """Merge another steque at the end."""
#         if another_steque.isEmpty():
#             return
#         if self.isEmpty():
#             self.head = another_steque.head
#         else:
#             self.tail.next = another_steque.head
#         self.tail = another_steque.tail
#         self.size += another_steque.size

#     def copy(self):
#         """Return a copy of the current steque."""
#         new_steque = Steque()
#         current = self.head
#         while current:
#             new_steque.enqueue(current.data)
#             current = current.next
#         return new_steque

#     def size(self):
#         """Return the number of elements."""
#         return self.size

#     def isEmpty(self):
#         """Check if the steque is empty."""
#         return self.size == 0

#     def toList(self):
#         """Convert steque into a list."""
#         elements = []
#         current = self.head
#         while current:
#             elements.append(current.data)
#             current = current.next
#         return elements

#     def __str__(self):
#         """Return string representation of the steque."""
#         if self.isEmpty():
#             return "Steque is empty"
#         result = ""
#         current = self.head
#         while current:
#             result += f"[{current.data}]"
#             current = current.next
#         return result

# # User Interaction
# def menu():
#     steque = Steque()
#     while True:
#         print("\n--- Steque Operations ---")
#         print("1. Push")
#         print("2. Pop")
#         print("3. Enqueue")
#         print("4. Peek")
#         print("5. Get Tail")
#         print("6. Contains")
#         print("7. Remove")
#         print("8. Reverse")
#         print("9. Clear")
#         print("10. Merge (Enter values for new Steque)")
#         print("11. Copy")
#         print("12. Convert to List")
#         print("13. Display")
#         print("14. Exit")
#         choice = input("Enter choice: ")

#         if choice == '1':
#             val = input("Enter value to push: ")
#             steque.push(val)
#         elif choice == '2':
#             print("Popped:", steque.pop())
#         elif choice == '3':
#             val = input("Enter value to enqueue: ")
#             steque.enqueue(val)
#         elif choice == '4':
#             print("Front Element:", steque.peek())
#         elif choice == '5':
#             print("Last Element:", steque.getTail())
#         elif choice == '6':
#             val = input("Enter value to check: ")
#             print("Exists:", steque.contains(val))
#         elif choice == '7':
#             val = input("Enter value to remove: ")
#             print("Removed:", steque.remove(val))
#         elif choice == '8':
#             steque.reverse()
#             print("Steque Reversed")
#         elif choice == '9':
#             steque.clear()
#             print("Steque Cleared")
#         elif choice == '10':
#             new_steque = Steque()
#             values = input("Enter values for new steque (comma separated): ").split(',')
#             for v in values:
#                 new_steque.enqueue(v.strip())
#             steque.merge(new_steque)
#             print("Merged new Steque")
#         elif choice == '11':
#             new_copy = steque.copy()
#             print("Copied Steque:", new_copy)
#         elif choice == '12':
#             print("Steque as List:", steque.toList())
#         elif choice == '13':
#             print("Current Steque:", steque)
#         elif choice == '14':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice, try again.")

# # Run the menu for user interaction
# menu()
