from collections import Counter

class Solution(object):
    def canPermutePalindrome(s):
        return sum([item[1]%2 for item in Counter(s).items()]) <= 1

    print canPermutePalindrome('saudfya;')
