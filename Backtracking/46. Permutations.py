class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        s = set()
        arr = []
        res = [] 
        def backtrack():
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for num in nums:
                if not num in s:
                    arr.append(num)
                    s.add(num)

                    backtrack()

                    arr.pop()
                    s.remove(num)
        
        backtrack()
        
        return res