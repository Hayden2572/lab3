listComprehension = [x**2 for x in range(1, 11)]
listComprehensionSort = [x for x in range(1, 21) if x % 2 == 0]
ogList = ["python", "Java", "c++", "Rust", "go"]
sortedList = [word for word in ogList if len(word) > 3 and word.istitle()]