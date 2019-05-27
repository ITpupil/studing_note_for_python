class Solution:
    def removeDuplicates(self, nums):
        return sorted(set(nums))


# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# set方法默认去重

a=[0,0,1,1,1,2,2,3,3,4]


b=Solution()
c=b.removeDuplicates(a)

print(c)
