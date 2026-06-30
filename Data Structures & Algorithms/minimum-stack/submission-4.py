class MinStack:

    def __init__(self):
        self.st = deque()
        self.minst = deque()

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minst:
            self.minst.append(val)
        else:
            temp = min(val, self.minst[-1])
            self.minst.append(temp)

    def pop(self) -> None:
        self.st.pop()
        self.minst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
        
