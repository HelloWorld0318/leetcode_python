from _ast import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            isValid = []
            for i in range(9):
                isValid.append(False)
            for column in range(9):
                if board[row][column] == '.':
                    continue
                if isValid[int(board[row][column]) - 1]:
                    return False
                else:
                    isValid[int(board[row][column]) - 1] = True

        for column in range(9):
            isValid = []
            for i in range(9):
                isValid.append(False)

            for row in range(9):
                if board[row][column] == '.':
                    continue
                if isValid[int(board[row][column]) - 1]:
                    return False
                else:
                    isValid[int(board[row][column]) - 1] = True

        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                isValid = []
                for i in range(9):
                    isValid.append(False)

                for i in range(row, row + 3):
                    for j in range(column, column + 3):
                        if board[i][j] == '.':
                            continue
                        if isValid[int(board[i][j]) - 1]:
                            return False
                        else:
                            isValid[int(board[i][j]) - 1] = True

        return True
