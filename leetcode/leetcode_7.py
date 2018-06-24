# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2 ** 31,  2 ** 31 − 1]. 
# For the purpose of this problem, assume that your function returns 0 
# when the reversed integer overflows.


class Solution:
    
    def __init__(self):
        self.upper_bound = 2 ** 31

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        symbol = abs(x) / x
        reversed_x = 0
        left_x = abs(x)

        while left_x > 1:
            tail = left_x % 10
            reversed_x = reversed_x * 10 + tail
            left_x = left_x // 10
        if left_x :
            reversed_x = reversed_x * 10 + left_x
        
        reversed_x = int(symbol * reversed_x)
        if (reversed_x >= self.upper_bound) or (reversed_x < - self.upper_bound):
            return 0
        else:
            return reversed_x

solution = Solution()

