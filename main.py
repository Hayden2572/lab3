listComprehension = [x**2 for x in range(1, 11)]
listComprehensionSort = [x for x in range(1, 21) if x % 2 == 0]
ogList = ["python", "Java", "c++", "Rust", "go"]
sortedList = [word for word in ogList if len(word) > 3 and word.istitle()]

class Countdown:
    def __init__(self, n):
        self.current = n
        self.end = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

for x in Countdown(5):
    print(x)

def Phibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, b+a
        print(a, b)

for x in Phibonacci(5):
    print(x)