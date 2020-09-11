class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def remove_head(self):
        if self.head is None:
            return None
        if self.head.get_next() is None:
            head = self.head

            self.head = None

            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def reverse_list(self, node, prev):
        nodes = list()
        nose = list()
        if(not self.head):
            return "Nothing to reverse"
        elif(self.head.next_node == None):
            return self.head
        else:
            current = self.head
            while(current):
                if(current != None):
                    nodes.append(current.value)
                current = current.get_next()
            print(f"Nodes List: {nodes}")
            
            
            for i in nodes:
                self.remove_head()
            for i in nodes:
                self.add_to_head(i)
            current = self.head
            while(current):
                if(current != None):
                    nose.append(current.value)
                current = current.get_next()
            print(f"Reversed Nodes: {nose}")
            return

# pork = LinkedList()

# pork.add_to_head(1)
# pork.add_to_head(2)
# pork.add_to_head(3)
# pork.add_to_head(4)
# pork.add_to_head(5)
# pork.reverse_list(pork.head, None)