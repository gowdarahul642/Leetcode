class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=sorted(nums)
        for i in range(len(num)):
            if i not in num:
                return i
        return i+1