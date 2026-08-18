class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.hashmap:
            return res
        l, r = 0, len(self.hashmap[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.hashmap[key][m][0] <= timestamp:
                l = m + 1
                res = self.hashmap[key][m][1]
            else:
                r = m - 1
        return res
        
