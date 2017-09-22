class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        Capital: 65-90
        other: 97-122
        """
        if word == None: return False
        
        count = 0
        
        for char in word:
            if 65 <= ord(char) <= 90:
                count += 1
        
        if count == 1:
            if 65 <= ord(word[0]) <= 90:
                return True
        
        if count == len(word):
            return True
        
        if count == 0:
            return True
        
        return False
