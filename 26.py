"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。

输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return 1
        store = 0
        # len(nums)>=2
        for i in range(len(nums)):
            store = nums[i]
            j = i+1
            # case: out of index
            if j == len(nums):
                return len(nums)

            while store == nums[j]:
                # print("index",j,"j=",nums)
                nums.pop(j)
                # j+=1
                if j == len(nums):
                    return len(nums)


        return len(nums)


s = Solution()
nums = [1,1,2]
# nums = [0,0,1,1,1,1,1,2,2,3,3,4,4,4,4]
ans = s.removeDuplicates(nums)
print(ans)