"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)==0:
            return -1
        if len(needle)==0:
            return 0
        left = 0
        right = len(needle)
        ni = 0
        while left<=len(haystack)-len(needle):
            if haystack[left:right]==needle:
                return left
            left+=1
            right+=1
        return -1

haystack,needle = "hello","lloo"
s = Solution()
ans = s.strStr(haystack,needle)
print(ans)
