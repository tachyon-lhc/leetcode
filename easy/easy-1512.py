class Solution:
    def numIdenticalPairs(self, nums:list[int]) -> int:
        goodPairs = 0
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    goodPairs += 1
        return goodPairs
    
print(Solution().numIdenticalPairs([1,2,3,1,1,3]))