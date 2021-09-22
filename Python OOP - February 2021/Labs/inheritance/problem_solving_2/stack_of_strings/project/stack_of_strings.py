class Stack:

    def __init__(self):
        self.data = []

    def push(self, item):
        if isinstance(item, str):
            self.data.append(item)

    def pop(self):
        item = self.data.pop()
        return item

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return True
        return False

    def __str__(self):
        if self.is_empty:
            return f'[{", ".join(self.data)}]'


s = Stack()
s.push('some_stuff')
s.push(12)
s.push('gasna')
s.push('maria')
s.push('alexx')
print(s.pop())
print(s.peek())
print(s)
