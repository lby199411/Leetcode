class Solution:
    def removeVowels(self, s: str) -> str:
        ret = ''
        dic = {'a', 'e', 'i', 'o', 'u'}
        for letter in s:
            if letter not in dic:
                ret = ret + letter
        return ret
