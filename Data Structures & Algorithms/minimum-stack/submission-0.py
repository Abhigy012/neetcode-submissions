class MinStack:
    st = []
    currmin = (2**31) - 1

    def __init__(self):
        self.st.clear()
        

    def push(self, val: int) -> None:
        self.currmin = min(self.currmin , val)
        self.st.append([val , self.currmin])

    def pop(self) -> None:
        self.st.pop()
        if len(self.st) != 0:
            self.currmin = self.st[-1][1]
        else:
            self.currmin = (2**31) - 1

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
        
