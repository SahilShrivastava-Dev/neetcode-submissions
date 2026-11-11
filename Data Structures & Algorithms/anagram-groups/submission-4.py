class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr=[0]*26
        my=defaultdict(list)
        for i in strs:
            for j in i:
                change=ord(j)-ord('a')
                arr[change]+=1 #Important to add += because then the count of characters will not be there
            my[str(arr)].append(i)
            arr=[0]*26
        return list(my.values())
                
