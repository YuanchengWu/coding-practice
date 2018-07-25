class Queue:
    container = []
    head = 0
    tail = 0

    def __init__(self):
        pass

    def enqueue(self, value):
        self.container.append(value)
        self.tail += 1

    def dequeue(self):
        if self.head == 0 and self.tail == 0:
            raise Exception('queue underflow')
        else:
            value = self.container[self.head]
            self.head += 1
            return value