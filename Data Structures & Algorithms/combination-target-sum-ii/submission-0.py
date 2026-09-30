class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        out = []
        candidates = sorted(candidates)

        def recurse(index, sum, sofar):
            if sum == target:
                out.append(sofar)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if sum+candidates[i] <= target:
                    recurse(i+1, sum+candidates[i], sofar+[candidates[i]])
        recurse(0, 0, [])
        return out





        