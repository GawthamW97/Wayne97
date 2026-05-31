class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can maintain hashmap for seen elements
        # we store the element as the key and its index as the value
        # we return the indexes only when the remaining num is found in the the hashmap
        seen = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in seen:
                return [seen[val],i]
            seen[nums[i]] = i