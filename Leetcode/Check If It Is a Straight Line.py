'''
https://leetcode.com/problems/check-if-it-is-a-straight-line/
'''

def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    if len(coordinates) == 2:
        return True
    else:
        slope = list()
        for i in range(len(coordinates)-1):                
            x1 = coordinates[i][0]
            x2 = coordinates[i+1][0]
            y1 = coordinates[i][1]
            y2 = coordinates[i+1][1]
            try:
                slope.append((y2-y1) / (x2-x1))
            except:
                slope.append(float("inf"))
        if len(set(slope)) == 1:
            return True
        else:
            return False
