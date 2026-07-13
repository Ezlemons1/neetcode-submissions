class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
        print(self.timeMap)

    def get(self, key: str, timestamp: int) -> str:
        timeValues = self.timeMap[key]
        left = 0
        right = len(timeValues) - 1
        if right < 0:
            return ""

        while left <= right:
            mid = (left + right) // 2
            word, num = timeValues[mid]

            if num == timestamp:
                print(word)
                return word
            
            if timestamp <= num:
                right = mid - 1
            else:
                left = mid + 1

        maxword, maxnum = timeValues[right]
        if timestamp >= maxnum:
            print(maxword)
            return maxword
        else:
            print("")
            return ""