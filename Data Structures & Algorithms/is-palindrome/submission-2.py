class Solution:
    def isPalindrome(self, s: str) -> bool:
        concat = "".join(x.lower() for x in s if x != " " and x.isalnum())
        right = len(concat) - 1
        left = 0
        print(concat)
        while left < right:
            if concat[left] != concat[right]:
                return False
            left += 1
            right -= 1
        return True
