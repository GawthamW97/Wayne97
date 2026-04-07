class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        concatWord = "".join(char.lower() for char in s if char!= " ") 
        right = len(concatWord) - 1
        while left < right:
            if not concatWord[left].isalnum():
                left+=1
                continue
            if not concatWord[right].isalnum():
                right-=1
                continue
            if concatWord[left] != concatWord[right]:
                return False
            left += 1
            right -= 1

        return True