"""
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #================= first ========================
        # i = 0
        # while i < len(nums):
        #
        #     if nums[i]==val:
        #         nums.pop(i)
        #         i-=1
        #     i+=1
        #
        # return len(nums)
        #=================================================
        # ================= second ========================
        # left = 0
        # right = 0
        # for i in range(len(nums)):
        #     if nums[right]==val:
        #         right+=1
        #     else:
        #         nums[left] = nums[right]
        #         left+=1
        #         right+=1
        # return left
        # =================================================

        # ================= third ========================
        left = 0
        # 对于这个right，index必须是right-1，不然left就不能代表所需要的数组元素数了
        right = len(nums)
        while left != right:
            if nums[left]==val:
                nums[left]=nums[right-1]
                right-=1
            else:
                left+=1
            print(nums,"left",left,";right",right)
        return left+1







        # =================================================

s = Solution()
# nums = [1, 1, 2]
# nums = [0,0,1,1,1,1,1,2,2,3,3,4,4,4,4,2,2]
nums = [3,2,2,3]
ans = s.removeElement(nums,3)

print(ans,nums[:ans])