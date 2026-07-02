class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}

        for i in arr:
            freq[i] = freq.get(i,0)+1
                

        return len(freq.values()) == len(set(freq.values()))
            