'''
https://leetcode.com/problems/integer-to-roman/
'''

def intToRoman(self, num: int) -> str:
    singles = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    doubles = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']
    result = thousands[num//1000] + hundreds[num%1000//100] + doubles[num%100//10] + singles[num%10]
    return results
