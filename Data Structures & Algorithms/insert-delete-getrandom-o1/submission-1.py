class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hashmap = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            self.arr[idx] = self.arr[-1]
            self.hashmap[self.arr[-1]] = idx

            self.arr.pop()
            del self.hashmap[val]

            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()