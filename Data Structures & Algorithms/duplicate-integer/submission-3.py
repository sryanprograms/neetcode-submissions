from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valueCounts = Counter(nums)
        
        for k,v in valueCounts.items(): 
            if v > 1:
                return True
        
        return False

        