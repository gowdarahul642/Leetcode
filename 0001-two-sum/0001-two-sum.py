class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i ,num in enumerate(nums):
            dif=target-num
            if dif in mp:
                return mp[dif],i
            mp[num]=i