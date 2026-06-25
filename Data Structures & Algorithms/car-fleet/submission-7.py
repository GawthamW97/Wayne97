import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in sorted(zip(position,speed),reverse=True):
            calc = (target - p) / s
            if stack and calc <= stack[-1]:
                continue
            stack.append(calc)
        return len(stack) 

# target=12
# position=[10,8,5,3,0]
# speed=[2,4,3,1,1]
'''
[] 
'''