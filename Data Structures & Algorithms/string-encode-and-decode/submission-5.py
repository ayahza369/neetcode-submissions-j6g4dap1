class Solution:

    def encode(self, strs: List[str]) -> str:
        final=''
        for s in strs:
            final+=str(len(s))+'#'+s
        print(final)
        return (final)

        

    def decode(self, s: str) -> List[str]:
        
        l=0
        final=[]
        while l<len(s):
            word=''
            n=''
            while s[l]!='#':
                n+=s[l]
                l+=1
            n=int(n)
            
            word=s[l+1:l+n+1]
            final.append(word)
            l+=n
            l+=1
                
        return(final)      

