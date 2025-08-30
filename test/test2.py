class StockSpanner:

    def __init__(self):

        self.stack = []
        self.index = {}
        self.count = 0

    def next(self, price: int) -> int:

        if len(self.stack) == 0:

            self.stack.append(price)
            self.index[price] = self.count

            self.count +=1

            return 1

        val = price

        while self.stack and val > self.stack[-1]:

            self.stack.pop()
        
        if len(self.stack) == 0:

            return self.count + 1

        else:

            price = self.count - self.index[self.stack[-1]]

        self.stack.append(val)

        if val not in self.index:

            self.index[val] = self.count
        
        self.count +=1
        

        return price
        


s = StockSpanner()

print(s.next(100))

# print(s.stack[-1])
# print(s.index[s.stack[-1]])
print(s.next(80))