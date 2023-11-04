class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # if line vertical
        if coordinates[1][0] == coordinates[0][0]:
            for x,y in coordinates:
                if x != coordinates[0][0]:
                    return False
            return True
        else:
            # if line straight and not vertical, y = slope * x + y_displacement
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            y_displacement = coordinates[0][1] - slope * coordinates[0][0]
            
            for x,y in coordinates:
                if slope * x + y_displacement != y:
                    return False
            return True