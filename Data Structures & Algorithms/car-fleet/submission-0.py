class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort()
        prev_time = 0
        fleet = 0
        for pos,sp in reversed(cars):
            time = (target-pos)/sp
            if time> prev_time:
                fleet+=1
                prev_time = time
        return fleet
            