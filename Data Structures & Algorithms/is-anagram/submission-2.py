class Solution:
    def isAnagram(self, s,t):
        sSorted=sorted(s)
        tSorted=sorted(t)

        if sSorted != tSorted: return False

        return True