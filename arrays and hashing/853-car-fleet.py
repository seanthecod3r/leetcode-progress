from ast import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        numFleets = 0
        cars = sorted(zip(position, speed), reverse=True)
        slowestTime = 0
        
        for carPos, carSpeed in cars:
            timeToDestination = (target - carPos) / carSpeed
            if timeToDestination > slowestTime:
                numFleets += 1
                slowestTime = timeToDestination
        
        return numFleets