'''
https://leetcode.com/problems/car-fleet/
'''

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    time = [ (target - pos) / v for pos, v in sorted(zip(position, speed))]
    count = high = 0
    
    for i in time[::-1]:
        if i > high:
            high = i
            count += 1
    return count
