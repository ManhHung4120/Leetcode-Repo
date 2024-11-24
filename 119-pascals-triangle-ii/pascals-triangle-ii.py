class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        rowBefore = [1,2,1]
        for i in range (2, rowIndex):
            rowBefore = self.generateRow(rowBefore)
        return rowBefore

    def generateRow(self, rowBefore):
        result = []
        for i in range(0, len(rowBefore) + 1):
            if i == 0:
                result.append(1)
            elif i == len(rowBefore):
                result.append(1)
            else:
                result.append(rowBefore[i - 1]+rowBefore[i])
        return result
            
        