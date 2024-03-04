class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x<10:
            return True
        a = []
        b = 0
        while(x//10!=0):
            a.append(x%10)
            x = x//10
        a.append(x)
        l = len(a)-1
        for i in range(l):
            if i != l-i:
                b += a[i]==a[l-i]
        return bool(b)
x = 123123
s = Solution()
print(s.isPalindrome(x))
