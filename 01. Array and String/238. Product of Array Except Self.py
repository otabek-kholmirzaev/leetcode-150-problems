class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [1]*(n+1)
        for i in range(n):
            arr[i+1] = arr[i] * nums[i]
        
        p = 1
        for j in range(n-1, -1, -1):
            temp = nums[j]
            nums[j] = p * arr[j]
            p *= temp
        
        return nums