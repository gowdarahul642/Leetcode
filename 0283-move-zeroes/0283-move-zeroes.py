class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z=[]
        for i in range (len(nums)):
            if nums[i]!=0:
                z.append(nums[i])
        while len(z)<len(nums):
                z.append(0)
                
        for i in range(len(z)):
            nums[i]=z[i]


                