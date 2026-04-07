class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        concatWord = "".join(char.lower() for char in s if char.isalnum()) 
        print(concatWord)
        right = len(concatWord) - 1
        while left < right:
            if concatWord[left] != concatWord[right]:
                return False
            left += 1
            right -= 1

        return True