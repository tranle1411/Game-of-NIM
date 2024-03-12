class AlphaBeta:
    def __init__(self, n, x):
        self.x = x
        self.current = n
    
    def alphabeta(self) -> int:
        a = -1
        b = +1
        value = -1
        result = 1
        for i in range(self.x):
            if (self.current-i-1>=0):
                v = MinMax(self.x).minvalue(self.current-i-1, a, b)
                value = max(v, value)
                if value>a: result = i+1
                a = max(value, a)
        return result
    
class MinMax:
    def __init__(self, x):
        self.x = x
    
    def minvalue(self, current, a, b) -> int:
        if current == 0:
            return +1
        value = +1
        for i in range(self.x):
            if (current-i-1>=0):
                v = self.maxvalue(current-i-1, a, b)
                value = min(v, value)
                if value<=a: return value
                b = min(value, b)
        return value
    
    def maxvalue(self, current, a, b) -> int:
        if current == 0:
            return -1
        value = -1
        for i in range(self.x):
            if (current-i-1>=0):
                v = self.minvalue(current-i-1, a, b)
                value = max(v, value)
                if value>=b: return value
                a = max(value, a)
        return value