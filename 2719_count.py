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
        tem = num1
        while self.Compare(tem,num2):
            cnum += self.JudgeDigitSum(min_sum,max_sum,tem)
            tem = self.Increment(tem)
            # print(tem)
        cnum %= (10**9+7)
        return cnum


    def JudgeDigitSum(self,min,max,num):
        sum = 0
        for i in range(len(num)):
            sum += int(num[i])
        judge = sum>=min and sum<=max
        return judge
    # 返回判断 num1<=num2?
    def Compare(self,num1,num2):
        if len(num1)<len(num2):
            return True
        elif len(num1) == len(num2):
            for i in range(len(num1)):
                if num1[i]==num2[i]:
                    continue
                elif num1[i]<num2[i]:
                    return True
                else:
                    return False
            return True
        else:
            return False

    # 实现加一，输入和输出都是str
    def Increment(self,num):
        # print("===Increment===")
        # print("before:",num)
        val = 0
        add = 1
        l = len(num)
        for i in range(l):
            n = int(num[l-i-1])
            val = (n+add)%10
            add = (n+add)//10
            # print("val=",val)
            # num[l-i-1] = str(val)
            num = self.replaceStr(num,l-i-1,val)
        if add:
            num = "1"+num
        # print("after:",num)
        return num
    def replaceStr(self,snum,i,num):
        l = list(snum)
        l[i] = str(num)
        snum = ''.join(l)
        return snum

# num1 = "1"
# num2 = "12"
# min_sum = 1
# max_sum = 8

num1 ="41"
num2 ="77"
min_sum =8
max_sum =46


s = Solution()
a = s.count(num1, num2, min_sum, max_sum)
print(a)
# b = s.Increment("999")