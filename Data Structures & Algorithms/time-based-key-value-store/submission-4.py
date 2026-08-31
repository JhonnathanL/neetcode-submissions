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

        l, r = 0, len(self.timestamps[key]) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            value = self.timestamps[key][mid][0]
            curr_timestamp = self.timestamps[key][mid][1]

            if curr_timestamp <= timestamp:
                result = value
                l = mid + 1
            else:
                r = mid - 1

        return result