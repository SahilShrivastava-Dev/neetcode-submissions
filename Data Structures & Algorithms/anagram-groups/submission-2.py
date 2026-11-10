class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my={}
        for i in strs:
            temp=''.join(sorted(i))
            if temp in my:
                my[temp].append(i)
            else:
                my[temp]=[i]
        return list(my.values())