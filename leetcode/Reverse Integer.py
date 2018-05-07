#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output: 321
#Example 2:

#Input: -123
#Output: -321
#Example 3:

#Input: 120
#Output: 21

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            num = int("".join(list(str(x))[::-1]))
        else:
            num = -int("".join(list(str(abs(x)))[::-1]))
            
        if num < 2**31-1 and num > -2**31:
            return num
        else:
            return 0
