from collections import Counter, defaultdict
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)
        groups = defaultdict(list)
        for ch, f in freq.items():
            groups[f].append(ch)
        best_freq = -1
        best_size = -1
        for f, chars in groups.items():
            if len(chars) > best_size or (len(chars) == best_size and f > best_freq):
                best_size = len(chars)
                best_freq = f
        return "".join(groups[best_freq])