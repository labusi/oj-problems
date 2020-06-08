#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start

class Node(object):
    green, black = 1, 0

    def __init__(self, val=None, color=0):
        self.val = val
        self.child = []
        self.child_val = ''
        self.color = color

    def insert(self, ch, color):
        '''
        在当前节点插入一个字符.    
        '''
        idx = self.child_val.find(ch)
        if idx == -1:
            self.child_val += ch
            self.child.append(Node(ch, color))
            return self.child[-1]
        else:
            if self.child[idx].color == Node.black:
                self.child[idx].color = color
            return self.child[idx]

    def search(self, word):
        node = self
        for ch in word:
            idx = node.child_val.find(ch)
            if idx != -1:
                node = node.child[idx]
            else:
                return False
        return node.color == Node.green
    
    def startsWith(self, word):
        node = self
        for ch in word:
            idx = node.child_val.find(ch)
            if idx == -1:
                return False
            else:
                node = node.child[idx]
        return True

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = len(word)
        node = self.root
        for i, ch in enumerate(word):
            if i == n-1:
                node.insert(ch, Node.green)
            else:
                node = node.insert(ch, Node.black)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.root.search(word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.root.startsWith(prefix)


# if __name__ == '__main__':
#     trie = Trie()
#     trie.insert('apple')
#     print(trie.search('app')) # False
#     trie.insert('app')
#     print(trie.search('app')) # True
#     trie.insert('apps')
#     print(trie.search('app')) # True
#     print(trie.search('apple')) # True
#     print(trie.startsWith('ap')) # True
#     print(trie.startsWith('apP')) # False
#     trie.insert('apP')
#     print(trie.search('apP')) # True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
