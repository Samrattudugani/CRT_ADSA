class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span


# LeetCode Example
operations = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
values = [[], [100], [80], [60], [70], [60], [75], [85]]

obj = None
output = []

for op, value in zip(operations, values):
    if op == "StockSpanner":
        obj = StockSpanner()
        output.append(None)
    else:
        output.append(obj.next(value[0]))

print(output)