from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.myMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        myList = self.myMap.get(key, [])
        l, r = 0, len(myList) - 1

        if not myList:
            return ""

        while l <= r:
            mid = (l + r) // 2
            if myList[mid][1] == timestamp:
                return myList[mid][0]
            elif myList[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return myList[r][0] if r >= 0 else ""
