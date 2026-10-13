class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numb = len(nums)
        count = 0

        for count1 in range(numb): 
            actuallyCount = 0 
            for count2 in range(count1, numb): 
                if nums[count2] == 0: break
                actuallyCount += 1
            count = max(count, actuallyCount)
        return count