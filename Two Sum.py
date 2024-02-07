nums = [2,7,11,15] 
target = 9



class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for b in range(i+1,len(nums)):
                if nums[i]+nums[b] == target:
                    return [i,b]
        
