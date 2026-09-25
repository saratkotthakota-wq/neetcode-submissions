class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = []
            self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        times = self.timemap[key]
        l, r = 0, len(times)-1
        while l<=r:
            mid = (l+r)//2
            if times[mid][0] == timestamp:
                return times[mid][1]
            elif times[mid][0] > timestamp:
                r = mid-1
            else:
                l = mid+1
        return times[r][1] if r >= 0 else ""