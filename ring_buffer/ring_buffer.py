class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = list()
        self.oldest = None

    def append(self, item):
        if(len(self.list) == 0):
            self.list.append(item)
            self.oldest = item
        elif(len(self.list) < self.capacity):
            self.list.append(item)
        else:
            for i in range(self.capacity):
                if (self.list[i] == self.oldest):
                    self.list[i] = item
                    if(i < self.capacity - 1):
                        self.oldest = self.list[i+1]
                        return
                    elif(i == self.capacity - 1):
                        self.oldest = self.list[0]
                        return
        
    def get(self):
        returned = []
        for i in self.list:
            if i == None:
                pass
            else:
                returned.append(i)
        return returned

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']