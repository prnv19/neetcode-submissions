class TimeMap:

    def __init__(self):
        self.log = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.log.keys():
            self.log[key] = [[timestamp, value]]
        else:
            self.log[key].append([timestamp, value])        

    def get(self, key: str, timestamp: int) -> str:
        # print(self.log)
        if key not in self.log:
            return ""
        time_arr = self.log[key]
        l, r = 0, len(time_arr) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            # print(f"l : {l} , m: {m}, r: {r}")
            if time_arr[m][0] <= timestamp:
                res = time_arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

        
