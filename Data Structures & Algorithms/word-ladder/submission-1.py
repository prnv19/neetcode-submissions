class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        hashmap = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                target = word[:i] + '*' + word[i + 1:]
                hashmap[target].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for j in hashmap[pattern]:
                        if j not in visited:
                            visited.add(j)
                            q.append(j)
            res += 1

        return 0
                    
    



