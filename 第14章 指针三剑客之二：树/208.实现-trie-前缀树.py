#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.child = [None]*26
        self.isEnd = False

    def searchPrefix(self, prefix:str)->"Trie":
        node = self
        for ch in prefix:
            ch = ord(ch)-ord('a')
            if not node.child[ch]:
                return None
            node = node.child[ch]
        return node
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch)-ord("a")
            if not node.child[ch]:
                node.child[ch]=Trie()
            node = node.child[ch]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd


    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

