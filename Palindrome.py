class Solution(object):
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
    #     暴力解法
        l = len(s)
        i = 0
        for i in range(l):
            sl = l-i
            for j in range(l-sl+1):
                sub = s[j:j+sl+1]
                # print("range=",j,"-",j+sl)
                # print("sub=",sub)
                # if self.isPalindrome(sub):
                #     return sub
                if sub == sub[::-1]:
                    return sub
        return None
    def isPalindrome(self,s):
        i = 0
        l = len(s)
        if not l:
            return False
        while i < l//2+1:
            if not s[i]==s[l-i-1]:
                return False
            i +=1
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            # i 的位置是查询中心字符的位置，以该字符为中心，向前走长度为当前最小字串的步数,主要的目的是包含前面的子串，然后前后再走一步
            start = max(i - len(res) - 1, 0)
            # print("i=",i ,"len(res)=", len(res) ,"start=",start,"\nres=",res)
            temp = s[start:i + 1]
            print("temp",temp)
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                # print("el_temp", temp)
                if temp == temp[::-1]:
                    res = temp
        return res


    def shortestFnBPalindrome(self, s):
        """
        214*. 最短回文串 优化
        :type s: str
        :rtype: str
        """
        # 思路：先找到最长的字串所在地，然后以其为中心，向前/向后添加元素
        res = ''
        idx = 0
        for i in range(len(s)):
            # i 的位置是查询中心字符的位置，以该字符为中心，向前走长度为当前最小字串的步数,主要的目的是包含前面的子串，然后前后再走一步
            start = max(i - len(res) - 1, 0)
            # print("i=",i ,"len(res)=", len(res) ,"start=",start,"\nres=",res)
            temp = s[start:i + 1]
            # print("temp", temp)
            if temp == temp[::-1]:
                res = temp
                idx = i
            else:
                temp = temp[1:]
                # print("el_temp", temp)
                if temp == temp[::-1]:
                    res = temp
                    idx = i
            # idx = idx-len(res)//2
        if len(res)==len(s):
            return s
        print(res,idx)
        # 然后确定向前还是向后添加
        # 理解错题意了，无论如何都只能往前添加
        # 大于零则往前，小于零则往后
        if (idx//2<len(s)//2)>0:
            print("forward")
            tmp = s[len(res):]
            s = tmp[::-1]+ s
        else:
            print("backward")
            tmp = s[:len(res)//2]
            s = s + tmp[::-1]
        return s

    def shortestPalindrome(self, s):
        """
        214. 最短回文串
        :type s: str
        :rtype: str
        """
        # 思路：找到前面的最短回文串
        res = ''
        idx = 0
        for i in reversed(range(len(s))):
        # for i in range(len(s)):
            # i 的位置是查询字符最后的位置，
            # print(i)
            temp = s[0:i+1]
            # print("temp", temp)
            if temp == temp[::-1]:
                res = temp
                idx = i
                break

        if len(res) == len(s):
            return s
        print(res, idx)
        tmp = s[idx+1:]
        s = tmp[::-1] + s

        return s

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
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

        # 思路：
        # 首先，第一遍遍历是肯定不能省的。有没有可能一次多匹配几个字串？
        for i in range(len(words)):
            pass
        # return list
        return 0
s = Solution()
# str = "abbb"
# str = "aacecaaa"
# ans = s.isPalindrome(str)
# ans = s.longestPalindrome(str)
# ans = s.shortestPalindrome(str)

# words = ["abcd","dcba","lls","s","sssll"]
# words = ["bat","tab","cat"]
words = ["a",""]
ans = s.palindromePairs(words)
print("The original string is:",words,"\n the answer is",ans)