class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=""
        for i in digits:
            sum+=str(i)
        sum=str(int(sum)+1)
        return [int(i) for i in sum]