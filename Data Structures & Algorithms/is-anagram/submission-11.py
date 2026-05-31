from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter will create dictionary for both the strings
        # These dictionaries will have the same count values 
        # for each of the letters in the strings the number of occurances within that string will be stored
        return Counter(s) == Counter(t)