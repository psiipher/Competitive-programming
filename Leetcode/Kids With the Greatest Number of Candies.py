'''
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
'''

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    ans = []
    maxCandy = max(candies)
    for i in candies:
        ans.append(i + extraCandies >= maxCandy)
    return ans
