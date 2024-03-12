"""
看力扣上的题解，看上去很厉害，但实际上感觉写的又臭又长，可读性太差了，自己再写一遍：
"""
# 首先，构造一个基本的前缀树
class Trie(object):
    def __init__(self):
        self.root = {}
        self.leaf = {}
    def insert(self, word):
        node = self.root
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node["isEnd"] = True
        node["word"] = word

    def search(self, word):
        node = self.root
        for ch in word:
            if not ch in node:
                return False
            node = node[ch]

        return "isEnd" in node
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not ch in node:
                return False
            node = node[ch]
        return True
# 然后，通过继承来实现比较具体的新要求
class plTrie(Trie):
    def insert(self, word,index):
        node = self.root
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node["isEnd"] = index
        node["word"] = word
    def search(self, word,index,result):
        # 成功则返回index，失败则啥也没有
        node = self.root
        for ch in word:
            if not ch in node:
                # if "isEnd" in node & node["isEnd"]!= index & isPalindrome(word+node["word"]):
                if "isEnd" in node and node["isEnd"] != index and isPalindrome(word+node["word"]):
                    # print(word+node["word"])
                    result.append([index,node["isEnd"]])
                    break

                else:
                    pass
            else:
                node = node[ch]
        # 单词被包含在前缀树中，则判断相加是否是回文
        # if node["isEnd"]!=index:


        return
def isPalindrome(word):
    return word==word[::-1]
class Solution(object):
    def matchWord(self,node,word,index,result):
        # print(node.root["isEnd"])

        if ("isEnd" in node.root) and word == word[::-1]:
            result.append(node["isEnd"], index)
            result.append(index, node["isEnd"])
        # 分两种情况，如果匹配成功，则直接判断是否是回文
        # 如果匹配失败，则判断是不是当前的word太长，
        node.search(word,index,result)

    def palindromePairs(self, words):
        result = []
        n = len(words)
        # 初始化根节点
        root = plTrie()
        # 构造前缀树,并记录当前单词的index i
        for i in range(n):
            # self.addWord(root,words[i],i)
            root.insert(words[i],i)
        for i in range(n):
            # 跳过根节点
            if (words[i]==""):continue
            # 将当前单词的反序存储下来用于查找
            word_serch = words[i][::-1]
            self.matchWord(root,word_serch,i,result)
        return result
words = ["abcd","dcba","lls","s","sssll"]
# 预期结果：[[0,1],[1,0],[3,2],[2,4]]
# words = ["bat","tab","cat","bat","tab","cat"]
# words = ["a",""]
s = Solution()
ans = s.palindromePairs(words)
print("The original string is:",words,"\n the answer is",ans)