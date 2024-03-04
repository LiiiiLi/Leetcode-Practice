class Solution(object):
    def count(self, num1, num2, min_sum, max_sum):
        """
        :type num1: str
        :type num2: str
        :type min_sum: int
        :type max_sum: int
        :rtype: int
        """
        cnum = 0
    def strToInt(self,num):
        l = list(num)
        lenth = len(num)
        re = 0
        for i in range(lenth):
            re = re+int(l[lenth-i-1])*10**i
        return re




# num1 = "1"
# num2 = "12"
# min_sum = 1
# max_sum = 8

num1 ="4179205230"
num2 ="7748704426"
min_sum =8
max_sum =46


s = Solution()
# a = s.count(num1, num2, min_sum, max_sum)
# print(a)
# b = s.strToInt("098342")
# print(b)