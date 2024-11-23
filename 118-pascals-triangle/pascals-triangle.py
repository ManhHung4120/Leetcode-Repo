class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [[1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        pascalTriangle = [[1],[1,1]]
        for i in range (3, numRows + 1):
            row = self.generateRow(pascalTriangle[i - 2])
            pascalTriangle.append(row)
        
        return pascalTriangle

    def generateRow(self, rowBefore):
        result = []
        for i in range(0, len(rowBefore) + 1):
            if i == 0:
                result.append(1)
            elif i == len(rowBefore):
                result.append(1)
            else:
                result.append(rowBefore[i - 1] + rowBefore[i])
        return result


        