class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return len(filter((lambda x: x == "1"), list(bin(n)[2:])))
