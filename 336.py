"""
// 336. 回文对：

"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 思路：
        # 构造前缀树，用类似 unordered_map 的字典来实现。实现添加单词，查找单词，判断回文字符
        result = []
        n = len(words)
        # 初始化根节点
        root = Trie()
        # 构造前缀树
        for i in range(n):
            self.addWord(root,words[i],i)
        # return root

        word_serch = ""
        for i in range(n):
            # 跳过根节点
            if (words[i]==""):continue
            # 将当前单词的反序存储下来用于查找
            word_serch = words[i][::-1]
            # 目的是查找：对于当前word_search，前缀树中有没有能够与其构成回文序列的单词

            num = root.search(word_serch)
            if num != -1:
                result.append([i,int(num)])
        return result

    def addWord(self,root,word,i):
        # 计数，当前所存储的字母量
        root.insert(word,i)

    def isPalindrome(self,word_search,word):
        tmp = word_search+word
        return tmp == tmp[::-1]

    def matchWord(self,node,i,word,list):
        # 首先排除根节点为空,且单词本身是回文的情况
        if (not "isEnd" in node) and word == word[::-1]:
            list.append(node["isEnd"],i)
            list.append( i,node["isEnd"])
        # 由于传入的本身就是反序的，所以只要从头开始
        # flag = True
        count = 0
        if len(word)<=150:
            flag = node.search(word)
        print(flag)


class Trie(object):
    def __init__(self):
        self.root = {}
        self.leaf = {}
    def insert(self, word,index):
        """
        :type word: str
        :rtype: None
        """
        count = 0
        node = self.root
        for char in word:
            if not char in node:
                node[char] = {}
            node = node[char]
            count += 1
            if count == 150:
                node["isEnd"] = 5005
                node["leaf_info"] = (index, word)
                return
        # isEnd 对应的值就是当前单词在words中所对应的下标
        node["isEnd"] = index
        node["word"] = word

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

        # return "isEnd" in node
        suc =  "isEnd" in node
        print("suc=",suc)
        if suc:
            return node["isEnd"]
        return -1
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





# words = ["abcd","dcba","lls","s","sssll"]
words = ["bat","tab","cat","bat","tab","cat"]
# words = ["a",""]
s = Solution()
ans = s.palindromePairs(words)
print("The original string is:",words,"\n the answer is",ans)
# print(ans.search('batt'))


# 思路：分别匹配每个字串，然后判断是否是回文
# i 在前，j 在后
# =============== 复杂度太高，不能用 ================
# list = []
# for i in range(len(words)):
#     for j in range(len(words)):
#         if i != j:
#             tmp = words[i]+words[j]
#             if tmp == tmp[::-1]:
#                 list.append([i,j])
# ==================================================