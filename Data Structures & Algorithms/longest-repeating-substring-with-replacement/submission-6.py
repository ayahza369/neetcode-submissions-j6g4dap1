class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=dict()
        print(freq)
        res=0
        l,r=0,0
        maximum=0
        while r<len(s):
            res+=1
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            f=sorted(freq.values(), reverse=True)
            print(res)
            check=res-f[0]
            print('this is check', check)
            if check>k:
                while check>k:
                    
                    freq[s[l]]-=1
                    res-=1
                    f=sorted(freq.values(), reverse=True)
            
                    check=res-f[0]
                    l+=1
            maximum=max(res,maximum)
            r+=1
        print(maximum)
        return(maximum)
            



            
                

