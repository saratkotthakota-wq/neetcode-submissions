class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKeyStr(word):
            key = [0 for _ in range(26)]
            for i in range(len(word)):
                charVal = ord(word[i])-97
                key[charVal] += 1
            keystr = [str(key[i]) for i in range(len(key))]
            keyout = ",".join(keystr)
            return keyout
        keyMap = {}
        for word in strs:
            key = getKeyStr(word)
            if key not in keyMap:
                keyMap[key] = [word]
            else:
                keyMap[key].append(word)
        output = []
        for key in keyMap:
            output.append(keyMap[key])
        return output



        