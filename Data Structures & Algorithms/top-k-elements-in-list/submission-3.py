class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my=defaultdict(int)
        for i in nums:
            my[i]+=1
        arr=[]
        for j in range(0,k):
            x = max(my, key=my.get)
            arr.append(x)
            del my[x]
        return arr