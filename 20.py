"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

        # 分析：当前判断的括号只有被消除掉的时候才能够消除前一个括号，所以需要一个序列来存储
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cont = {'(': 1, '[': 1, '{': 1, ')': 0, ']': 0, '}': 0}
        dic = {'(':1,'[':2,'{':3,')':-1,']':-2,'}':-3}
        l = len(s)
        # 指示当前输入位数
        # i = 0
        q = []
        # while(cont[s[i]]and i<l):
        #     q += str(dic[s[i]])
        #     i += 1
        for i in range(l):
            # 如果遇到了正数,则添加进q
            if cont[s[i]]:
                q.append(str(dic[s[i]]))
                # print("current query is :",q)
            else:
                if q==[]:
                    return False
                if not dic[s[i]]+int(q[-1]):
                    q.pop()
                else:
                    return False
            i += 1
        if q==[]:
            return True
        else:
            return False

a =Solution()

s = "()"
print(a.isValid(s))
s = "()[]{}"
print(a.isValid(s))
s = "(]"
print(a.isValid(s))



