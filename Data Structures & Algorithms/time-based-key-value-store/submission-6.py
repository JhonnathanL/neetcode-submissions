class TimeMap:

    def __init__(self):
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []

        self.timestamps[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""

        use_value = ""
        
        l, r = 0, len(self.timestamps[key]) - 1

        while l <= r:
            mid = (l + r) // 2
            curr = self.timestamps[key][mid][1]

            if curr <= timestamp:
                use_value = self.timestamps[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return use_value