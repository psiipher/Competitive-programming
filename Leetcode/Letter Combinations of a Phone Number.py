'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''


def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or digits is None:
            return []
        temp = []
        match = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],
                 '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'],'9':['w','x','y','z']}
        from itertools import product
        for i in digits:
            temp.append(match[i])
        temp = list(product(*temp))
        ans = []
        for i in temp:
            ans.append(''.join(i))
        return ans
        
