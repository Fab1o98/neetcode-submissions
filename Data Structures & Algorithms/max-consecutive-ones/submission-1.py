class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numb = len(nums)
        count = 0 

        for countt in range(numb): 
            actuallyCount = 0 
            for countt1 in range(countt, numb): 
                if nums[countt1] == 0 : break
                actuallyCount += 1
            count = max(count, actuallyCount)
        return count
            
