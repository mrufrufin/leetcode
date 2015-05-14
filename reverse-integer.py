#simulates 32-bit overflow, largest int is 2**31-1
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x >= 0:
            retStr = str(x)[::-1]
        else:
            retStr = "-" + str(x)[::-1][:-1]
        retStr = int(retStr)
        if abs(retStr) > (2**31-1):
            return 0
        return retStr
