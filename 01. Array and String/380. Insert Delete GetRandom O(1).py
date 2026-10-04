class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        
        self.nums.append(val)
        self.index[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:
        if not val in self.index:
            return False
        
        last_val = self.nums[-1]

        i = self.index[val]
        self.nums[i] = last_val
        self.index[last_val] = i

        self.nums.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)