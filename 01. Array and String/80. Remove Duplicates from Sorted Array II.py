class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # For at most N duplicates, the general pattern is:
        # if k < N or num != nums[k - N]:
        #     nums[k] = num
        #     k += 1
        
        N = 2
        k = 0

        for num in nums:
            if k < N or num != nums[k - N]:
                nums[k] = num
                k += 1

        return k

