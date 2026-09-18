class TimeMap:

    def __init__(self):
        self.timemaps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemaps:
            self.timemaps[key] = []
        
        self.timemaps[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timemaps:
            return ""

        l, r = 0, len(self.timemaps[key]) - 1
        res = ""

        while l <= r:

            mid = (l + r) // 2
            curr = self.timemaps[key][mid]

            if curr[1] <= timestamp:      
                res = curr[0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
            


