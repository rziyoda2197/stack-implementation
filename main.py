class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
```

```python
# Misollar
stack = Stack()
print(stack.is_empty())  # True

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size())  # 3

print(stack.peek())  # 3

print(stack.pop())  # 3
print(stack.size())  # 2

print(stack.is_empty())  # False
