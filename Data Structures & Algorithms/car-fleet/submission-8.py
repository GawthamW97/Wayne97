class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p,s in sorted(zip(position,speed), reverse=True):
            dist = (target - p) / s 
            if stack and dist <= stack[-1]:
                continue
            stack.append(dist)
        return len(stack)