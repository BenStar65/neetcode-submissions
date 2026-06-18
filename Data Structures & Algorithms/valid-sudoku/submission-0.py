class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        boxes = {}

        for col in range(9):
            for row in range(9):
                num = board[col][row]

                if num == ".":
                    continue
                
                box = (row // 3, col // 3)

                if row not in rows:
                    rows[row] = set()

                if col not in cols:
                    cols[col] = set()
                
                if box not in boxes:
                    boxes[box] = set()
                
                if num in rows[row]:
                    return False
                if num in cols[col]:
                    return False
                if num in boxes[box]:
                    return False
                
                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)

        return True


                
        