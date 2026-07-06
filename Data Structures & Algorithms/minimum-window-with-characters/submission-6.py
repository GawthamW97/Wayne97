from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT = Counter(t) # the frequency of character in t
        window = {} # current frequency of character in substring s[l : r + 1]

        have = 0 # number of distinct characters required whose frequency requirement has been satisfied
        need = len(countT) # number of distinct required character that must satisfy.
        res = [-1,-1] # l and r pointers of the response window
        resLen = float("infinity") # len of the res window

        l = 0

        for r in range(len(s)): # loop the s string
            c = s[r]
            window[c] = window.get(c,0) + 1 # add the characters count from right pointer to the window
            
            if c in countT and countT[c] == window[c]: # if the curent character is in countT and
                have += 1   # the count of the current character in window is equal to it in countT
                            # we increase the have value.
            while have == need:     # while we have the required number of characters in the window
                if (r - l + 1) < resLen:    # if the current window len is lesser than the previous window
                    res = [l,r] #   we update the res variable with new left and right pointer
                    resLen = r - l + 1 # we also update the resLen variable
                
                window[s[l]] -= 1 #we need move the left pointer to the right, hence we decrease the counter of the element at left pointer by 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: # if the left pointer char is in conuntT and the char count is lower in window than countT 
                    have -=1 # it indicates that the required chars is less, which mean we need to decrease the 'have' by 1
                l += 1 # we move the pointer towards the right, (shrinking the window)
        
        l , r = res # after for loop ends we get the l and r pointer 

        return s[l : r + 1] if resLen != float("infinity") else "" # and return the minimum window substring