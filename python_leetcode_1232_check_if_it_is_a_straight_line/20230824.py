coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] # true
coordinates = [[0,0],[0,1],[0,-1]]                  # 


class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates)==2:
            return True

        point1 = coordinates[0]
        point2 = coordinates[1]

        try:
            a = (point1[1]-point2[1])/(point1[0]-point2[0]) 
            b = point1[1]-a*point1[0]

            for coordinate in coordinates[2:]:  # coordinate = coordinates[2]
                check_y = a*coordinate[0]+b
                if check_y == coordinate[1]:
                    continue
                else:
                    return False
        except:
            for coordinate in coordinates[2:]:  # coordinate = coordinates[2]
                if point1[0] == coordinate[0]:
                    continue
                else:
                    return False 


        return True