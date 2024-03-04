class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        n = len(s)
        max_len = 0

        for i in range(n):
            rk = i
            d = {}
            # print("==================== \n new item:",s[i])

            for j in range(i,n):
                # 如果出现了新的字符（不存在于当前窗口中）
                if d.get(s[j]):
                    # print("continue")
                    # continue
                    # print("break")
                    break
                else:
                    # print("j=", j, "s[j]=", s[j])
                    d[s[j]] = j + 1
                    rk += 1


            if max_len<=(rk-i):
                max_len = rk-i
            # print("k=",k,"rk=",rk,"maxlen=",max_len)
            print(d)


        return max_len

s = Solution()
# sin = "aabcabgacbn"
# sin = "abcabcbb"
# sin="aaab"
sin = "pwwkew"
a = s.lengthOfLongestSubstring(sin)
print(a)

# 废弃代码
#
#     # # print("k=",k,"i+1=",i+1)
#     # if k==i+1:
#     #     None
#     else:
#         print("in dict",d,"pop",s[k-1])
#         d.pop(s[k-1])
#         k+=1
#     # print("k+1=",k)
#         d[s[i]] = i + 1
#         rk+=1