class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1=set(s)
        word2=set(t)
        word1_list=list(s)
        word2_list=list(t)
        if len(word1)!=len(word2) or len(word1_list)!=len(word2_list):
            return False
        else:
            for char in word2:
                if char not in word1:
                    return False
            word1count=Counter(s)
            word2count=Counter(t)
            for char in word2: 
                if word2count[char]!=word1count[char]:
                    return False
            return True
    
        