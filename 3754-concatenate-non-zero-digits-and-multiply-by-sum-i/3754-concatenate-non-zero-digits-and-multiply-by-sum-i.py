class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n1=str(n)
        n2=list(n1)
        new=""
        sum1=0
        for ch in n1:
            if ch not in "0":
                new+=ch
        for i in n2:
            sum1+=int(i)
        if new == "":
            return 0
        return int(new)*sum1
