'''
https://leetcode.com/problems/jewels-and-stones/
'''

def numJewelsInStones(self, J: str, S: str) -> int:
    count = dict()
    ans = 0
    for i in S:
        count[i] = count.get(i, 0) + 1
    
    for i in J:
        if i in count:
            ans += count[i]
    return ans
