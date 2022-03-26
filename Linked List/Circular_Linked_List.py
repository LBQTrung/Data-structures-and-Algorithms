class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        
        itr = self.head
        while itr:
            itr = itr.next
            if (itr.next == self.head):
                break
        new_node.next = self.head
        self.head = new_node
        itr.next = self.head
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        while itr:
            itr = itr.next
            if (itr.next == self.head):
                itr.next = new_node
                new_node.next = self.head
                break

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
            if (itr.next == self.head):
                count += 1
                break
        return count

    def remove_at_beginning(self):
        itr = self.head
        second = itr.next
        while itr:
            itr = itr.next
            if (itr.next == self.head):
                break
        itr.next = second
        self.head = second
    
    def remove_at_end(self):
        itr = self.head
        while itr:
            itr = itr.next
            if (itr.next.next == self.head):
                break
        itr.next = self.head
    
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise("Invalid index")
        
        if index == 0:
            self.remove_at_beginning()
        elif index < self.get_length():
            itr = self.head
            count = 0
            while itr:
                if (count == index - 1):
                    itr.next = itr.next.next
                    break
                itr = itr.next
        else:
            self.remove_at_end()
        
    def print(self):
        if self.head is None:
            print("The list is empty")
            return
        
        if self.head.next == self.head:
            print(self.head.data)
            return

        itr = self.head
        result = ''
        while itr:
            result += str(itr.data) + "-->"
            itr = itr.next
            if (itr.next == self.head):
                result += str(itr.data)
                break
        print(result)