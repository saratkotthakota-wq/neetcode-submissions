class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            buckets[count].append(num)
        output = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                output.append(num)
                if len(output) == k:
                    return output
        return output


        
        