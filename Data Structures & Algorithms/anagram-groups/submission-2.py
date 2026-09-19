class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            counts = [0 for _ in range(26)]
            for c in s:
                counts[ord(c) - ord('a')] += 1
            hashmap[tuple(counts)].append(s)
        return list(hashmap.values())
        