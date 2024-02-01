class Solution:
    def isDuplicate(self,nums):
        unique_set = set()
        for i in nums:
            if i in unique_set:
                return True
            unique_set.add(i)
        return False
    
assert(Solution().isDuplicate([1,2,3,4,1])) == True
assert(Solution().isDuplicate([1,2,3,4,5])) == False