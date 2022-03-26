class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head, None)
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        while itr:
            last = itr
            itr = itr.next     
        new_node = Node(data, None, last)
        last.next = new_node
    
    def remove_at_beginning(self):
        itr = self.head
        itr.next.prev = None
        self.head = itr.next
    
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at_end(self):
        itr = self.head
        while itr:
            last = itr
            itr = itr.next
        last.prev.next = None
    
    def remove_at(self, index: int):
        if index < 0 or index > self.get_length():
            raise("Invalid index")
        
        if index == 0:
            self.remove_at_beginning()
        elif index < self.get_length():
            itr = self.head
            count = 0
            while itr:
                if count == index:
                    itr.prev.next = itr.next
                    itr.next.prev = itr.prev
                    break
                count += 1
                itr = itr.next
        else:
            self.remove_at_end()
        
    def print(self):
        if self.head is None:
            print("The list is empty")
            return
        # Print according to forward direction
        print("Forward direction:")
        itr = self.head
        result = ""
        while itr:
            result += str(itr.data) + "-->"
            last = itr
            itr = itr.next
        print(result[:-3])
        # Print according to reverse direction
        print("Reverse direction:")
        result = ""
        while last:
            result += str(last.data) + "-->"
            last = last.prev
        print(result[:-3])