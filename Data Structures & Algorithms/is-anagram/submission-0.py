class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = 26 * [0]
        for char in s:
            num = ord(char) - ord('a')
            s_hash[num] += 1
        t_hash = 26 * [0]
        for char in t:
            num = ord(char) - ord('a')
            t_hash[num] += 1
        for i in range(26):
            if s_hash[i] != t_hash[i]:
                return False
        return True


        
        