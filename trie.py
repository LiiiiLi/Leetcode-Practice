"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
"""
# 所需要的元素：
# 根节点：不包含值，用于指示不同prefix
# 每个节点包含： children：char，isEnd: bool, val:str
# 需要实现的功能：searchPrefix，insert，search，startwith
class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
    def insert(self, word:str)->None:
        # 从当前节点开始
        node = self
        # 遍历 word中的 char
        for ch in word:
            # 计算当前字符的编号（以ASCII码辅助）
            ch = ord(ch)-ord("a")
            # 如果当前节点的对应子节点不存在，那么添加对应的Trie节点
            if not node.children[ch]:
                node.children[ch] = Trie()
            # 如果存在，则进入下一个节点，继续遍历剩下的char
            node = node.children[ch]
        # 遍历完成之后，单词插入完毕
        node.isEnd = True

    def searchPrefix(self,prefix:str)->"Trie":
        node = self
        for ch in prefix:
            ch = ord(ch)-ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self,word:str)->bool:
        # 调用查找前缀的方法
        node = self.searchPrefix(word)
        # 如果找到了，并且当前节点是一个完整的单词，那么查找成功，否则查找失败
        return node is not None and node.isEnd

    def startsWith(self,prefix:str) -> bool:
        # 只要查找前缀可以返回值，那就说明存在以前缀为开头的单词
        return self.searchPrefix(prefix) is not None

class Trie(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node["isEnd"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if not ch in node:
                return False
            node = node[ch]

        return "isEnd" in node
    """
    return node["isEnd"]：
    这一行代码假定 node 是一个字典，其中包含一个键为 "isEnd" 的条目。它直接返回该键对应的值。如果在 node 中找不到 "isEnd" 这个键，这行代码可能会引发 KeyError 异常。这种方式直接检查是否存在 "isEnd" 键，并返回其对应的值。
    
    return 'isEnd' in node：
    这一行代码使用 in 运算符来检查字典 node 中是否存在键 "isEnd"。如果存在，则返回 True，否则返回 False。不会引发 KeyError 异常，因为它只检查键的存在性而不试图获取键的值。
    """
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if not ch in node:
                return False
            node = node[ch]
        return True