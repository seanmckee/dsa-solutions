class MinStack:

    def __init__(self):
        self.stack = []
        self.currentMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.currentMin:
            if val < self.currentMin[-1]:
                self.currentMin.append(val)
            else:
                self.currentMin.append(self.currentMin[-1])
        else:
            self.currentMin.append(val)

    def pop(self) -> None:
        # if self.stack[-1] == self.currentMin[-1]:
        #     self.currentMin.pop()
        self.currentMin.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.currentMin:
            return self.currentMin[-1]
