class MinStack:

    def __init__(self):
        self.intlist = []

    def push(self, val: int) -> None:
        self.intlist.append(val)

    def pop(self) -> None:
        self.intlist = self.intlist[0:len(self.intlist) - 1]

    def top(self) -> int:
        return self.intlist[len(self.intlist) - 1]

    def getMin(self) -> int:
        return min(self.intlist)
        
