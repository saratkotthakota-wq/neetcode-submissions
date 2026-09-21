class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word))
            output += "#"
            output += word
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        pointer = 0
        numstr = ""
        while pointer < len(s):
            if ord(s[pointer]) <= 57 and ord(s[pointer]) >= 48:
                numstr += s[pointer]
                pointer += 1
            if ord(s[pointer]) == 35:
                num = int(numstr)
                word = s[pointer+1:pointer+num+1]
                output.append(word)
                pointer += num + 1
                numstr = ""
        return output