class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        arr = []
        def backtrack(i):
            print(arr)
            if len(arr) == k:
                res.append(arr.copy())
                return

            for j in range(i, n+1):
                arr.append(j)
                backtrack(j+1)
                arr.pop()
        
        backtrack(1)

        return res