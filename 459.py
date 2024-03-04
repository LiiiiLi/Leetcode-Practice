"""
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
"""
class Solution(object):
    # def repeatedSubstringPattern(self, s) -> bool:
    #     def kmp(query: str, pattern: str) -> bool:
    #         n, m = len(query), len(pattern)
    #         print("n",n,"m",m)
    #         # 这个fail就是字串的 next序列
    #         fail = [-1] * m
    #         print("fail",fail)
    #         for i in range(1, m):
    #
    #             j = fail[i - 1]
    #             print("j = fail[i - 1]:", j, "=", fail[i - 1])
    #             while j != -1 and pattern[j + 1] != pattern[i]:
    #                 j = fail[j]
    #             #如果当前的字符和前面的指针所指的字符相同，那么next在这个位置的数字+1
    #             if pattern[j + 1] == pattern[i]:
    #                 fail[i] = j + 1
    #         print("fail", fail)
    #         match = -1
    #         for i in range(1, n - 1):
    #             while match != -1 and pattern[match + 1] != query[i]:
    #                 match = fail[match]
    #             if pattern[match + 1] == query[i]:
    #                 match += 1
    #                 if match == m - 1:
    #                     return True
    #         return False
    #
    #     return kmp(s + s, s)

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # kmp算法：
        def kmp_search(string, patt):
            # 算出 next 数组(马上讲到)
            string = string[1:-1]
            next = build_next(patt)
            print("string=",string,"patt=",patt)

            # 主串中的指针
            i =0
            #子串中的指针
            j=0
            while i< len(string):
                # print("i",i,"j",j)
                if string[i]== patt[j]: # 字符匹配，指针后移
                    i += 1
                    j += 1
                elif j >0: # 字符失配，根据 next 跳过子串前面的一些字符
                    j= next[j-1]
                else: #子串第一个字符就失配
                    i += 1
                if j == len(patt):  # 匹配成功
                    # return i-j
                    return True
            return False
        def build_next(patt):
            next = [0]# next 数组(初值元素一个 0)
            prefix_len = 0#当前共同前后缀的长度
            i = 1
            while i < len(patt):
                if patt[prefix_len]==patt[i]:
                    prefix_len += 1
                    next.append(prefix_len)
                    i += 1

                else:
                    if prefix_len == 0:
                        next.append(0)
                        i += 1
                    else:
                        prefix_len = next[prefix_len - 1]
            print("next=",next)
            return next

        return kmp_search(s + s, s)
        # return build_next(s)




s = Solution()
# str = "abac"
str = "abaababaab"
# str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
ans = s.repeatedSubstringPattern(str)

print(ans)

