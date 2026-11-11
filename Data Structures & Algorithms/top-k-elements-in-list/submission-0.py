class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my=defaultdict(int)
        for i in nums:
            my[i]+=1
        arr=[]
        for j in range(0,k):
            value=max(list(my.values()))
            x=next(key for key, val in my.items() if val == value)
            arr.append(x)
            print(arr)
            del my[x]
        return arr