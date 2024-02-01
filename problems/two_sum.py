class Solution:
    def twoSum(self,nums,target):
        prevMap = {} 
        for index , value in enumerate(nums):
            diff = target - value
            if diff in prevMap:
                return [prevMap[diff],index]
            prevMap[value] = index
        return


assert(Solution().twoSum([2,1,3,4],4)) == [1,2]