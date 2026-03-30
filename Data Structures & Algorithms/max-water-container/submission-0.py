class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum =0
        
        r=0
        l=len(heights)-1
        while r<l:
            print(r,l)
            if int(heights[r])>int(heights[l]):
                if (int(heights[l])*(l-r))>=maximum:
                    maximum = (int(heights[l])*(l-r))
                l-=1
                
            if int(heights[l])>int(heights[r]):
                if (int(heights[r])*(l-r))>=maximum:
                    maximum = (int(heights[r])*(l-r))
                r+=1
            if int(heights[l])==int(heights[r]):
                if (int(heights[r])*(l-r))>=maximum:
                    maximum = (int(heights[l])*(l-r))
                r+=1
                l-=1
            print (maximum)
        return maximum
