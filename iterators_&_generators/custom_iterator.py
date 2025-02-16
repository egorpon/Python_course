class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        print("StopIteration")
        raise StopIteration


counter = Counter(0, 10)
for x in counter:
    print(x)
for x in counter:
    print(x)
