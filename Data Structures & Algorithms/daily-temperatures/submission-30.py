class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index = 1
        indices = [0]
        answer = [0] * (len(temperatures))
        for i in range(1, len(temperatures)):
            while indices and temperatures[indices[-1]] < temperatures[i]:
                num = indices.pop()
                answer[num] = i - num
            indices.append(i)
        return answer