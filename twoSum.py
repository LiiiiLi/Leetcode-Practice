class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenth = len(nums)
        index = 0
        temp = 0
        for i in range(lenth):
            temp = nums.pop(0)
            index+=1
            # print(i,temp)
            for j in range(0,lenth-index):
                if target - temp ==nums[j]:
                    # print("yes")
                    return [i,j+index]