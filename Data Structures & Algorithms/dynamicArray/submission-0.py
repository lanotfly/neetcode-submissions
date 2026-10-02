class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()

        self.array[self.len] = n
        self.len += 1

    def popback(self) -> int:
        if self.len > 0:
            self.len -= 1

        return self.array[self.len]
        
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for i in range(self.len):
            new_arr[i] = self.array[i]
        self.array = new_arr

    def getSize(self) -> int:
        return self.len
    
    def getCapacity(self) -> int:
        return self.capacity
