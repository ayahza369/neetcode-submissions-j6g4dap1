class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap=defaultdict(set)
        res=[]
        tri=[]
        count=0
        for i in nums:
            count=0
            for j in nums: 
                if i==j:
                    count+=1
            if count in mymap: 
                mymap[count].add(i)
            else:
                mymap[count]={i}
        print(mymap)
        sorted_map=sorted(mymap)
        for i in range(1,len(nums)+1):
          
            if i in mymap:
                value=mymap[i]
                print(value)
                for val in value:
                    tri+=[val]
        print(tri)
        return tri[len(tri)-k:len(tri)]
         
