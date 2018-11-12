""" Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_length = len(nums)
        left, right = 0, num_length - 1
        while right > left:
            if nums[right] > nums[right-1]:
                left = right - 1
                break
            right -= 1
        if right:
            for j in range(num_length-1, left, -1):
                if nums[j] > nums[left]:
                    nums[j], nums[left] = nums[left], nums[j]
                    break
            nums[left+1:] = nums[left+1:][::-1]
        else:
            nums[::1] = nums[::-1]
        print(nums)

solution = Solution()
#solution.nextPermutation([7,9,9,8,6,5])
#solution.nextPermutation([0])
##solution.nextPermutation([0, 1])
#solution.nextPermutation([])
#solution.nextPermutation([1, 2, 3])
x = [4, 3, 2, 1]
solution.nextPermutation(x)
print(x)
#solution.nextPermutation([0, 0, 5])



