class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse=False)
        position, speed = zip(*paired)
        position = list(position)
        speed = list(speed)
        fleets = 1

        print(position)
        print(speed)
        times = [((target - position[i]) / speed[i]) for i in range(len(position))]
        print(times)
        curr = times.pop()
        while times:
            now = times.pop()
            if now > curr:
                fleets += 1
                curr = now
        
        return fleets

