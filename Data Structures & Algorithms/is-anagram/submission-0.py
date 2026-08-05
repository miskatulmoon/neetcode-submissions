class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two strings cannot be anagrams if they are different lengths
        if len(s) != len(t): 
            return False


        #create two hashmaps to store character frequencies for each string
        countS = {}
        countT = {}

        #iterate
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) #Set the count for character s[i] to its current count plus one. If it doesn’t exist yet, start from 0.
            countT[t[i]] = 1 + countT.get(t[i],0)

        return countS == countT    


        

