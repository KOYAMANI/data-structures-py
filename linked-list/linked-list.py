class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
    
    def append_at_start(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        elements = [] 
        cur = self.head
        while cur is not None:
            elements.push(cur.data)
            cur = cur.next
        print(elements)
         