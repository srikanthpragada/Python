class StackFullError(Exception):
    def __init__(self):
        self.message = "Stack is full"


class StackEmptyError(Exception):
    def __init__(self):
        self.message = "Stack is empty"


class Stack:
    def __init__(self, limit=10):
        self.data = []
        self.limit = limit

    def push(self, value):
        if len(self.data) == self.limit:
            raise StackFullError()

        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            raise StackEmptyError()

        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None

        return self.data[-1]

    @property
    def length(self):
        return len(self.data)


s = Stack(5)

while (True):
    print("\nMenu")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Length")
    print("5. Exit")
    choice = int(input("Enter choice : "))

    if choice == 1:
        value = input("Enter a value :")
        try:
            s.push(value)
        except StackFullError:
            print("Sorry! Stack is already full!")

    elif choice == 2:
        try:
            print("Value = ", s.pop())
        except StackEmptyError:
            print("Sorry! Stack is empty!")
    elif choice == 3:
        value = s.peek()
        if value is None:
            print("Sorry! Stack is empty!")
        else:
            print("Value = ", value)
    elif choice == 4:
        print("Length = ", s.length)
    else:
        break
