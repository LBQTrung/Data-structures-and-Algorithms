class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("The list is empty")
            return

        result = ""
        itr = self.head
        while itr:
            result += str(itr.data) + "-->"
            itr = itr.next
        print(result[:-3])
    
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
    
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index: int):
        if index < 0 or index > self.get_length():
            raise("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return 

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

