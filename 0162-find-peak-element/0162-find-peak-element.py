class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        num1= max(nums)
        for i ,num in enumerate(nums):
            if num==num1:
                return i
