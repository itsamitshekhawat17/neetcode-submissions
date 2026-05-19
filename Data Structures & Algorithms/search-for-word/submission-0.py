class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(board,r ,c ,word,i):
            if i==len(word):
                return True 
            if r<0 or c<0 or r>=rows or c >=cols:
                return False
            if board[r][c]==" " or board[r][c]!=word[i]:
                return False 
            char = board[r][c]
            board[r][c] = " "
            if  dfs(board,r+1 ,c ,word,i+1) or dfs(board,r-1 ,c ,word,i+1) or dfs(board,r ,c+1 ,word,i+1) or dfs(board,r ,c-1 ,word,i+1):
                return True
            board[r][c] = char
            return False
        for r in range(rows):
            for c in range(cols):
                if dfs(board,r,c,word,0):
                    return True
        return False