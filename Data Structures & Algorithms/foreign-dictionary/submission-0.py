class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {c: set() for w in words for c in w}
        for i in range(1, len(words)):
            curr, prev = words[i], words[i-1]
            minlen = min(len(curr), len(prev))
            if len(prev) > len(curr) and prev[:minlen] == curr[:minlen]:
                return ""
            for j in range(minlen):
                if prev[j] != curr[j]:
                    adj[prev[j]].add(curr[j])
                    break
        
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)

        