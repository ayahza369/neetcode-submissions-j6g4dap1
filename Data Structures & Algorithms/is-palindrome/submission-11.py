class Solution:
    def isPalindrome(self, s: str) -> bool:
        alist =[]
        for char in s:
            if char.isalnum():
                alist.append(char.lower())
        blist =alist[:]
        return blist == alist[::-1]
        