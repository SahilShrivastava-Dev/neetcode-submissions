class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n_dict=dict()
        for i in range(0,len(s)):
            if s[i] not in n_dict:
                n_dict[s[i]]=1
            else:
                n_dict[s[i]]+=1
        
        for i in range(0,len(t)):
            if t[i] not in n_dict:
                return False
            else:
                n_dict[t[i]]-=1

        return all(value == 0 for value in n_dict.values())