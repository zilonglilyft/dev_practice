class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


def parenthesis_match(li):
    s = Stack()
    match = {
        ')':'(',
        ']':'[',
        '}':'{',
    }
    for i in li:
        if i in match.values():
            s.push(i)
        else:
            if s.get_top() == match[i]:
                s.pop()
            else:
                return False
    return s.is_empty()

print(parenthesis_match('{[]()})[]'))

