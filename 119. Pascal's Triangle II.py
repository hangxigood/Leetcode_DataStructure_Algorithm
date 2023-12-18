# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        last_row = [1]
        new_rows = [1]

        for count in range(rowIndex):# 3 count=0,1
            new_rows = [1]
            for n in range(count): # 1 last_row = [1,1] n = 0
                new_element = last_row[n] + last_row[n+1] 
                new_rows.append(new_element)
            new_rows.append(1)
            last_row = new_rows
        
        return new_rows
