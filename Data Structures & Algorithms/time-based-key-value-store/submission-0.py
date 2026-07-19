class TimeMap:

    def __init__(self):
        self.d  = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamped_values = self.d[key]
        l = 0
        r = len(timestamped_values) - 1

        while l <= r:
            mid = (l + r) // 2
            if timestamped_values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        if r >= 0:
            return timestamped_values[r][1]
        else:
            return ""
        
