class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s1=s+s
        if len(s)==len(goal):
           return  goal in s1
        return False
          