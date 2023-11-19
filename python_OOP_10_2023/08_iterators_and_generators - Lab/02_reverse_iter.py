class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.start_index = len(self.iter_obj) - 1
        self.end_index = -1

    # ти се итерирай
    def __iter__(self):
        return self

    # как да се итерираш
    def __next__(self):
        if self.start_index <= self.end_index:
            raise StopIteration()
        index = self.start_index
        self.start_index -= 1
        return self.iter_obj[index]


reversed_obj = reverse_iter([1, 2, 3, 4])
for item in reversed_obj:
    print(item)

