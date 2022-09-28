class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """        
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        
        for r in range(9):
            for c in range(9):
                
                if board[r][c] == ".":
                    continue
                    
                if (board[r][c] in row_set[r] or
                    board[r][c] in col_set[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                
        return True
        
        