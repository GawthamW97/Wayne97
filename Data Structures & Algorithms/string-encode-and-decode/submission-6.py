class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        returnString = ""
        for s in strs:
            strEncode = str(len(s)) + "$" + s
            returnString += strEncode
        
        return returnString
            
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        i=0
        returnList = []
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            decodeStr = s[j+1 : j+1 + length]
            returnList.append(decodeStr)
            i = j + 1 + length

        return returnList



        