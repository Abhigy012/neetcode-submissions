class TimeMap:

    def __init__(self):
        self.mpp = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mpp[key] = self.mpp.get(key, [])
        print(self.mpp[key])
        self.mpp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        x = self.mpp.get(key , [])
        low , high =0, len(x) - 1
        res = ""
        while low <= high:
            mid = int(low + (high-low)/2)
            if x[mid][0] == timestamp:
                res = x[mid][1]
                break
            elif x[mid][0] > timestamp:
                high = mid-1
            else:
                res = x[mid][1]
                low = mid+1
        return res
        
