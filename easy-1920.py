class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        Anums = [0] * len(nums)
        for i in range(len(nums)):
            Anums[i] = nums[nums[i]]
        return Anums

print(Solution().buildArray([5,0,1,2,3,4]))
