class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dict_s={}
        for i in s:
            if i in dict_s:
                dict_s[i]+=1
            else:
                dict_s[i]=1
        
        print(dict_s)
        for i in t:
            if i in dict_s:
                dict_s[i]-=1
            else:
                return False
                
        return all(value==0 for value in dict_s.values())
            