class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen = {}
        # for i in range(len(numbers)):
        #     remain = target - numbers[i]
        #     if numbers[i] in seen:
        #         return [i,numbers[i]]
        #     seen[remain] = i
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum > target:
                right-=1
            else:
                left += 1
            