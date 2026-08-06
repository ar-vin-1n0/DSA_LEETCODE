
class Solution(object):
    def hammingWeight(self, n):

        binary =  bin(n)[2:]

        weight = 0

        for bit in binary:
            if bit == "1":
                weight += 1

        return weight   