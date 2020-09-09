'''
https://leetcode.com/problems/fair-candy-swap/
'''

def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    expect = (sum(B) - sum(A)) // 2
    setB = set(B)
    for i in A:
        if i + expect in setB:
            return [i, i+expect]
