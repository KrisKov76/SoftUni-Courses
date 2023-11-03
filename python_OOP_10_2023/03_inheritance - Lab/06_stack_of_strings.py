class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise TypeError("Element must be a string")
        self.data.append(element)

    def pop(self):
        element = self.data.pop()
        return element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


stack = Stack()
print(stack)
print(stack.push("ddd"))
print(stack.push("Hello"))
print(stack.push("Babiniii i Vangini"))

print(stack)