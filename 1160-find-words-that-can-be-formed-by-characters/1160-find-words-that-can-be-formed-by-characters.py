class Solution(object):
    def countCharacters(self, words, chars):
        char_count = Counter(chars)
        total = 0
        for w in words:
            w_count = Counter(w)
            x = True
            for c, freq in w_count.items():
                if freq > char_count[c]:
                     x = False
                     break
            if x:
                total += len(w)
        return total
 
        