#Longest Palindromic Substring,Palindormic
# just like the format of ABCDCBA or ABCCBA

#Example 1:

#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

#Example 2:
#Input: "cbbd"
#Output: "bb"

import pprint 

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_length = len(s)
        if str_length == 1:
            return s

        max_length, length = 1, 0
        max_length_str, length_str = s[0], ''

        for i in range(str_length):
            if i == 0:
                if s[0] == s[1]:
                    length = 2
                    length_str = s[:2]
                if length > max_length:
                    max_length_str = length_str
                    max_length = length

            elif i == (str_length - 1):
                if s[i] == s[i-1]:
                    length = 2
                    length_str = s[-2:]
                if length > max_length:
                    max_length_str = length_str
                    max_length = length


            else:
                if s[i-1] == s[i+1]:
                    j = 1
                    length = 3
                    while (i-j-1) >= 0 and (i+j+1) <= (str_length - 1):
                        if s[i-j-1] == s[i+j+1]:
                            length += 2
                            j += 1
                        else:
                            break
                    length_str = s[(i-j):(i+j+1)]
                    if length > max_length:
                        max_length_str = length_str
                        max_length = length


                if s[i] == s[i+1]:
                    j = 1
                    length = 2
                    while (i-j) >= 0 and (i+j+1) <= (str_length - 1):
                        if s[i-j] == s[i+1+j]:
                            length += 2
                            j += 1
                        else:
                            break
                    length_str = s[(i-j+1):(i+j+1)]
                    if length > max_length:
                        max_length_str = length_str
                        max_length = length
                

        return max_length_str

solution = Solution()
print(solution.longestPalindrome('aa'))
print(solution.longestPalindrome('ddadad'))
print(solution.longestPalindrome('cbbc'))
print(solution.longestPalindrome('abcabb'))





                

            
            



                
                
