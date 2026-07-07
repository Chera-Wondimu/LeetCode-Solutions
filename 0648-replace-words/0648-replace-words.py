class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        ans = []
        for word in sentence.split():
            replaced = word
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in roots:
                    replaced = prefix
                    break
            ans.append(replaced)
        return " ".join(ans)
        