class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        def diff(w1, w2):
            diff = 0
            i = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
            return diff
        
        allWords = []
        allWords.append(beginWord)
        allWords.extend(wordList)
        for i in range(len(allWords)):
            for j in range(i+1, len(allWords)):
                w1, w2 = allWords[i], allWords[j]
                if diff(w1, w2) == 1:
                    g[w1].append(w2)
                    g[w2].append(w1)

        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while len(q):
            w, d = q.popleft()
            if w == endWord:
                return d
            for nxt in g[w]:
                if nxt not in visited:
                    q.append((nxt, d+1))
                    visited.add(nxt)
        
        return 0

