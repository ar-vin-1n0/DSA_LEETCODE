class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False

        count = {}

        for w in s:
            count[w] = count.get(w,0)+1

        for w in t:
            if w not in count:
                return False
            count[w] -= 1

            if count[w] < 0:
                return False

        return True                            
                

           

        