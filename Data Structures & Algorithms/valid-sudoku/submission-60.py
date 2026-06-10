class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = defaultdict(list)
        for i in range(len(board)):
            # checking if every column is valid
            column = [r[i] for r in board if r[i] != "."]
            if len(column) != len(set(column)):
                return False
            # checking if every row is valid
            row = [board[i][k] for k in range(9) if board[i][k] != "."]
            print(row)
            if len(row) != len(set(row)):
                print(row)
                print(set(row))
                return False
            # checking if every subbox is valid
            for j in range(3):
                if i in range(0, 3):
                    tempi = 0
                elif i in range(3, 6):
                    tempi = 3
                elif i in range(6, 9):
                    tempi = 6
                if j == 0:
                    tempj = 0
                elif j == 1:
                    tempj = 3
                elif j == 2:
                    tempj = 6
                subbox = [board[a][b] for a in range(tempi, tempi+3) for b in range(tempj, tempj+3) if board[a][b] != "."]
                if len(subbox) != len(set(subbox)):
                    return False
        return True