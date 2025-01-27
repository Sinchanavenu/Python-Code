#Match the parenthesis using stack
class UnlimitedStack:
    def __init__(self):
        self.data = []
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def stackCount(self):
        return self.count

    def push(self, item):
        self.data.append(item)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.count -= 1
            return self.data.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return None

    def __str__(self):
        return str(self.data)


def testSymbol(data, stk):
    left = '{[('
    right = '}])'

    
    for ch in data:
        if ch in left:
            stk.push(ch)
        elif ch in right:
            if stk.is_empty():
                return False
            if right.index(ch) != left.index(stk.pop()):
                return False
    return stk.is_empty()


if __name__ == "__main__":
    stk = UnlimitedStack()
    data = input("Enter a string with parentheses, brackets, and braces: ")
    
    if testSymbol(data, stk):
        print("The symbols are balanced and properly nested.")
    else:
        print("The symbols are not balanced or properly nested.")