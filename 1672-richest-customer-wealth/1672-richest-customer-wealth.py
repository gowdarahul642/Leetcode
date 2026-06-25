class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max1=0
        for i in accounts:
            num=sum(i)
            max1=max(max1,num)
        return max1