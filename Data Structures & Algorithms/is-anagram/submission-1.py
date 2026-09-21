class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}

        for i in range(len(s)):
            if s[i] in hashs:
                hashs[s[i]] += 1
            else:
                hashs[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in hasht:
                hasht[t[i]] += 1
            else:
                hasht[t[i]] = 1

        for l in hashs:
            if l not in hasht or hashs[l] != hasht[l]:
                return False
        
        for l in hasht:
            if l not in hashs or hashs[l] != hasht[l]:
                return False
        return True
        
        

        
        