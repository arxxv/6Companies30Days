class Solution:
    def Anagrams(self, words, n):
        wordmap = {}
        for word in words:
            wsorted = ''.join(sorted(word))
            if wsorted not in wordmap:
                wordmap[wsorted] = []
            wordmap[wsorted].append(word)
        return list(wordmap.values())

sol = Solution()
words = ["act","god","cat","dog","tac"]
print(sol.Anagrams(words, len(words)))
