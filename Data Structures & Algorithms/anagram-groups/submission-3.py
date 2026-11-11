class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my=defaultdict(list)
        for i in strs:
            temp=''.join(sorted(i))
            my[temp].append(i)
            
        return list(my.values())