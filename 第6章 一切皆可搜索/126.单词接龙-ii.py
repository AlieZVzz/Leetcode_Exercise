#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start

import string
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_bag = set(wordList)
        if endWord not in word_bag:
            return []
        word_bag.add(beginWord)
        distance = self.bfs(endWord, word_bag,beginWord)
        results = []
        self.dfs(beginWord, endWord, word_bag, distance, [beginWord], results)
        return results
    
    def bfs(self, begin_word, word_bag,endWord):
        queue = [begin_word]
        distance = {}
        distance[begin_word] = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_word = queue.pop(0)
                for next_word in self.get_next_words(curr_word, word_bag):
                    if next_word not in distance:
                        distance[next_word] = distance[curr_word] + 1
                        queue.append(next_word)
            if endWord in distance:
                break 
        return distance
    
    def dfs(self, curr_word, target, word_bag, distance, path, results):
        if curr_word == target:
            results.append(list(path))
            return
        for next_word in self.get_next_words(curr_word, word_bag):
            if next_word not in distance  or  distance[next_word] != distance[curr_word] - 1:
                continue
            path.append(next_word)
            self.dfs(next_word, target, word_bag, distance, path, results)
            path.pop() #回溯
    
    def get_next_words(self, curr_word, word_bag):
        next_words = []
        for i in range(len(curr_word)):
            for c in list(string.ascii_lowercase):
                next_word = curr_word[:i] + c + curr_word[i + 1:]
                if next_word != curr_word and next_word in word_bag:
                    next_words.append(next_word)
        return next_words





# @lc code=end
