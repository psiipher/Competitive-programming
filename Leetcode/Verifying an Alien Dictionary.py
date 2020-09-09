'''
https://leetcode.com/problems/verifying-an-alien-dictionary/
'''

def isAlienSorted(self, words: List[str], order: str) -> bool:
    ordered = {v: i for i, v in enumerate(order)}

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i+1]

        for k in range(min(len(word1), len(word2))):
            if word1[k] != word2[k]:
                if ordered[word1[k]] > ordered[word2[k]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False

    return True
