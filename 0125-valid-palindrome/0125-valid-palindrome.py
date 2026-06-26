class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s=s.lower()
    
        result=""
        for i in s:
            if i.isalnum():
                result+=i
        return result==result[::-1]
           

