class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        out = ""
        # 首先排除只有一个单词的情况
        if (len(strs)==1):
            return strs[0]
        # 然后排除第一个单词为空的情况
        elif (strs[0]=="" ):
            return ""

        status = True
        i = 0
        while(status and i<len(strs[0])):
            out, status=self.judge_i_th_letter(i,out,status,strs)
            i+=1

        return out
    # 输入当前要比较的位数和当前的公共前缀
    def judge_i_th_letter(self,i,out,status,strs):
        letter = strs[0][i]
        # print(i,"th letter = ",letter)
        judge = 0 - len(strs)
        try:
            for j in range(len(strs)):
                if letter==strs[j][i]:
                    judge += 1
            if not judge:
                out = out+letter
            else:
                status = False
        except:
            return out, False
            # return out
        return out, status

strs = ["flower","flow","flight"]
s = Solution()
answer = s.longestCommonPrefix(strs)
print("The answer is",answer)

strs = ["dog","racecar","car"]
answer = s.longestCommonPrefix(strs)
print("The answer is",answer)

strs =["",""]
answer = s.longestCommonPrefix(strs)
print("The answer is",answer)

strs =["ab","a"]
answer = s.longestCommonPrefix(strs)
print("The answer is",answer)

strs =["flower","flower","flower","flower"]
answer = s.longestCommonPrefix(strs)
print("The answer is",answer)

# # 判断第一个字母是否相同
# letter = strs[0][0]
# print("first letter = ",letter)
# judge = 0 - len(strs)
# for i in range(len(strs)):
#     if letter==strs[i][0]:
#         judge += 1
# if not judge:
#     out = out+letter
# else:
#     return out