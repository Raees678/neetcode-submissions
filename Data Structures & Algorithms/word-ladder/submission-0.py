class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # wordCounts = {}
        # wordCounts[beginWord] = Counter(beginWord)
        # for word in wordList:
        #     wordCounts[word] = Counter(word)
        # wordCounts[endWord] = Counter(endWord)

        def diff(w1, w2):
            diff = 0
            i = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
            return diff
        
        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while len(q):
            w, d = q.popleft()
            if w == endWord:
                return d
            for nxt in wordList:
                if nxt not in visited and diff(w, nxt) <= 1:
                    q.append((nxt, d+1))
                    visited.add(nxt)
        
        return 0

