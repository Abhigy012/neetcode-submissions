class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [] , [], []
        for i in range (0,9):
            rows.append({})
            cols.append({})
            boxes.append({})
        i,j = 0,0
        while i<9:
            x = board[i][j]
            if x != '.':
                if(rows[i].get(x) != None):
                    print(rows)
                    print(i, " ", j, " ", "1 here")
                    return False
                else:
                    rows[i][x] = 1
                if(cols[j].get(x) != None):
                    print(cols)
                    print(i, " ", j, " ", "2 here")
                    return False
                else:
                    cols[j][x] = 1
                ind = 3*(int(i/3)) + int(j/3)
                if(boxes[ind].get(x) != None):
                    print(boxes)
                    print(i, " ", j, " ", "3 here")
                    return False
                else:
                    boxes[ind][x] = 1
            if j==8:
                j=0
                i += 1
            else:
                j+= 1
        return True