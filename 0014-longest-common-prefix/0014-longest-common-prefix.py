class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        for i in range(len(strs[0])):
            ch=strs[0][i]
            for word in strs[1:]:
                if  i>=len(word) or ch!=word[i] or i>=len(word):
                    return result
            result+=ch
        return result