class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-1] or nums[i] != nums[k-2]:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return k