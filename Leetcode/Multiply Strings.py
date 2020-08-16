'''
    https://leetcode.com/problems/multiply-strings/
'''

def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        num1_int = 0
        num2_int = 0
        for i in range(len(num1)):
            num1_int += ((10**i) * int(num1[i]))
            
        for i in range(len(num2)):
            num2_int += ((10**i) * int(num2[i]))
            
        return str(num1_int*num2_int)
