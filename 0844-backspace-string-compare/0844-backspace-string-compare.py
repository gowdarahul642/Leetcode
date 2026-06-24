class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        stack2=[]
        for i in s:
            if "#" == i:
                if stack:
                 stack.pop()
            else:
                stack.append(i)
        for j in t:
            if "#" == j:
                if stack2:
                 stack2.pop()
            else:
                stack2.append(j)
        if stack==stack2:
            return True
        return False
        

