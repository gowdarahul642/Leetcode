class Solution:
    def removeStars(self, s: str) -> str:
        result=[]
        for i in s:
            if i is "*":
                result.pop()
            else:
                result.append(i)
        return "".join(result)
                
        