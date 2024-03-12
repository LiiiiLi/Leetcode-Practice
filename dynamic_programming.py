# 寻找最大的递增子序列
def findMaxIncre(list):
    # return max(findIncre(list,i) for i in range(len(list)))
    memo = {}
    def dpFindIncre(list, i):
        if i in memo:
            return memo[i]
        if i == len(list) - 1:
            return 1
        max_len = 1
        # 查询从i开始，往后有没有递增的数字
        for j in range(i + 1, len(list)):
            # 如果有，那就以该数字为起点，继续往后查询
            if list[i] < list[j]:
                # 如果查询到的max length更大，则替换掉当前的max lenth
                max_len = max(max_len, dpFindIncre(list, j) + 1)
        memo[i] = max_len
        return max_len

    return max(findIncre(list, i) for i in range(len(list)))
def findIncre(list,i):
    if i == len(list)-1:
        return 1
    max_len = 1
    # 查询从i开始，往后有没有递增的数字
    for j in range(i+1,len(list)):
        # 如果有，那就以该数字为起点，继续往后查询
        if list[i]<list[j]:
            # 如果查询到的max length更大，则替换掉当前的max lenth
            max_len = max(max_len,findIncre(list,j)+1)
    return max_len

def dpFindMaxIncre(list):
    memo = [1]*len(list)
    for i in reversed(range(len(list)-1)):
        for j in reversed(range(i+1,len(list))):
            if list[i]<list[j]:
                memo[i]=max(memo[i],memo[j]+1)
    return max(re for re in memo)



# list = [1,5,2,4,3,4,5,6,9]
# # list = [1,4,2,3]
# ans = findMaxIncre(list)
# print(ans)

# ans1 = dpFindMaxIncre(list)
# print(ans1)

# # 寻找连续子序列的最大和
def maxSeqSum(list):
    # 思路：其实只需要记录起始和末尾的需要就行了，得到一个 n*n的三角矩阵
    memo = {}
    max_sum = max(list)
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (i,j-1) in memo:
                memo[(i,j)] = memo[(i,j-1)]+list[j]
                max_sum = max(max_sum,memo[(i,j)])
            else:
                memo[(i,j)] = list[i]+list[j]
                max_sum = max(max_sum, memo[(i, j)])
    # print(memo)
    return max_sum
list = [3,-4,2,-1,2,6,-5,4]
ans = maxSeqSum(list)
print(ans)