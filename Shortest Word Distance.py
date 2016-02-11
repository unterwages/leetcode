def shortestDistance(self, words, word1, word2):

        w1 = [i for i in xrange(len(words)) if words[i] == word1]
        w2 = [i for i in xrange(len(words)) if words[i] == word2]

        return min([abs(i - j) for i in w1 for j in w2])
