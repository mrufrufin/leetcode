class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        itera = 0
        summ = n
        if n == 1:
            happy = True
        else:
            happy = False
        while summ != 1 and itera < 100:
            summ =sum(map((lambda x: pow(int(x), 2)),list(str(summ))))
            if summ == 1:
                happy = True
            itera +=1
        return happy

