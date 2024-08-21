from ast import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            mySet = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in mySet:
                        return False
                    mySet.add(board[i][j])
        for i in range(9):
            mySet = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in mySet:
                        return False
                    mySet.add(board[j][i])
        for k in range(0, 9, 3):
            for l in range(0, 9, 3):
                mySet = set()
                for i in range(3):
                    for j in range(3):
                        if board[i + k][j + l] != '.':
                            if board[i + k][j + l] in mySet:
                                return False
                            mySet.add(board[i + k][j + l])

        return True