class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            # We can't reach this index
            if i > max_reach:
                return False

            # Update the farthest position we can reach
            max_reach = max(max_reach, i + nums[i])

        return True