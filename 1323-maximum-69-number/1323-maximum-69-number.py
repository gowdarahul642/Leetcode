class Solution:
    def maximum69Number (self, num: int) -> int:
        num1=str(num)
        return int(num1.replace("6","9",1))
        