class Stack(object):
    top = 0
    container = []

    def __init__(self):
        pass

    def is_empty(self):
        return self.top == 0

    def push(self, value):
        if self.top > len(self.container) - 1:
            self.container.append(value)
        else:
            self.container[self.top] = value
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception('stack underflow')
        else:
            self.top -= 1
            return self.container[self.top]

test_stack = Stack()
# test_stack.pop()
test_stack.push(1)
test_stack.push(2)
test_stack.push(3)
print(test_stack.pop())
test_stack.push(4)
print(test_stack.pop())
