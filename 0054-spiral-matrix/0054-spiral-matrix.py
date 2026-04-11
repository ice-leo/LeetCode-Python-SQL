class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        row = 0
        col = 0
        ul = -1 # row
        ur = len(matrix[0]) # column
        ll = -1 # column
        lr = len(matrix) # row


        def forward(ul, ur, row, col):
            while col < ur - 1:
                result.append(matrix[row][col])
                col += 1
            ul += 1
            return ul, ur, row, col

        def downward(ur, lr, row, col):
            while row < lr - 1:
                result.append(matrix[row][col])
                row += 1
            ur -= 1
            return ur, lr, row, col

        def backward(lr, ll, row, col):
            while col > ll + 1:
                result.append(matrix[row][col])
                col -= 1
            lr -= 1
            return lr, ll, row, col
        
        def upward(ll, ur, row, col):
            while row > ul + 1:
                result.append(matrix[row][col])
                row -= 1
            ll += 1
            return ll, ur, row, col

        control = 0
    
        while len(result) != len(matrix) * len(matrix[0]) - 1:
            if control % 4 == 0:
                ul, ur, row, col = forward(ul, ur, row, col)
            elif control % 4 == 1:
                ur, lr, row, col = downward(ur, lr, row, col)
            elif control % 4 == 2:
                lr, ll, row, col = backward(lr, ll, row, col)
            elif control % 4 == 3:
                ll, ur, row, col = upward(ll, ur, row, col)
            control += 1
        result.append(matrix[row][col])

        return result
        