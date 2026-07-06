class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def get_tree(self, words):
        res = TrieNode()
        for word in words:
            curr = res
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True
        return res

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = self.get_tree(words)
        R, C = len(board), len(board[0])
        res = set()
        visited = set()

        def valid(r, c):
            if r >= 0 and r < R and c >= 0 and c < C:
                return True
            return False
        
        def dfs(r, c, word, node):
            if valid(r, c) and node.end:
                res.add(word)

            visited.add((r, c))
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if (new_r, new_c) not in visited and valid(new_r, new_c) and board[new_r][new_c] in node.children:
                    w = board[new_r][new_c]
                    dfs(new_r, new_c, word + w, node.children[w])
            
            visited.remove((r, c))
        
        for r in range(R):
            for c in range(C):
                ch = board[r][c]
                if ch in tree.children:
                    dfs(r, c, ch, tree.children[ch])
        return list(res)
        