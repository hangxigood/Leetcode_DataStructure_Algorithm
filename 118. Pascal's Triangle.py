# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        last_row = [1]
        output = [last_row]

        for count in range(numRows-1):

            new_rows = [1]

            for n in range(count): 
                new_element = last_row[n] + last_row[n+1] 
                new_rows.append(new_element)

            new_rows.append(1)
            last_row = new_rows
            output.append(new_rows)
        
        return output
