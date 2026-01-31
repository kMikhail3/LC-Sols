class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for i in range(9):
            boxRow = i//3
            boxCol = i%3
            seen = set()
            for c in range(3):
                for r in range(3):
                    val = board[boxRow*3 +r][boxCol*3 + c]
                    if val == ".":
                        continue
                    if val in seen:
                        return False
                    seen.add(val)
        return True



