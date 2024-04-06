
class Queen:
    def __init__(self, queen):
        self.any_queen = queen 
        
    def __str__(self):
        return self.any_queen
    
    def can_move(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
            return True
                    
class King:
    def __init__(self, king):
        self.any_king = king
        
    def __str__(self):
        return self.any_king
    
    def can_move(self, x1: int, y1: int, x2: int , y2: int) -> bool:
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            return True

class Bishop:
    def __init__(self, bishop):
        self.any_bishop = bishop
        
    def __str__(self):
        return self.any_bishop 
    
    def can_move(self, x1: int, y1: int, x2: int , y2: int) -> bool:
        if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
            return True
        
class Knight:
    def __init__(self, knight):
        self.any_knight = knight
        
    def __str__(self):
        return self.any_knight
    
    def can_move(self, x1: int, y1: int, x2: int , y2: int) -> bool:
        if abs(x1-x2) == 2 and abs(y1-y2) == 1 or abs(x1-x2) == 1 and abs(y1-y2) == 2:
            return True
        
class Rook:
    def __init__(self, rook):
        self.any_rook = rook
        
    def __str__(self):
        return self.any_rook
    
    def can_move(self, x1: int, y1: int, x2: int , y2: int) -> bool:
        if y1-y2 == 0 or x1-x2 == 0:
            return True
    
class Pawn:
    def __init__(self, pawn, color='white'):
        self.any_pawn = pawn
        self.color = color
        
    def __str__(self):
        return self.any_pawn
        
    def can_move(self, x1: int, y1: int, x2: int , y2: int) -> bool:
        if self.color == 'white':
            if x1-x2 == 0 and (y1-y2 == 2 or y1-y2 == 1) or y1-y2 == 1 and (x1-x2==1 or x1-x2==-1):
                return True
        elif self.color == 'black':
            if x1-x2 == 0 and (y1-y2 == -1 or y1-y2 == -2) or y1-y2 == -1 and (x1-x2==1 or x1-x2==-1):
                return True
       
board = [['.' for i in range(8)] for j in range(8)]
knight1 = Knight('\u2658')
knight2 = Knight('\u265E')
rook1 = Rook('\u2656')
rook2 = Rook('\u265C')
king1 = King('\u2654')
king2 = King('\u265A')
bishop1 = Bishop('\u2657')
bishop2 = Bishop('\u265D')
queen1 = Queen('\u2655')
queen2 = Queen('\u265B')
board[0][0] = rook1
board[0][1] = knight1
board[0][2] = bishop1
board[0][3] = queen1
board[0][4] = king1
board[0][5] = bishop1
board[0][6] = knight1
board[0][7] = rook1

pawn1 = Pawn('\u2659', 'black')
pawn2 = Pawn('\u265F', 'white')
for i in range(8):
    board[1][i] = pawn1
    board[6][i] = pawn2
    
board[7][0] = rook2
board[7][1] = knight2
board[7][2] = bishop2
board[7][3] = queen2
board[7][4] = king2
board[7][5] = bishop2
board[7][6] = knight2
board[7][7] = rook2
                
for row in board:
    print(*row, sep=' ')

flag = True    
while True:     
    if flag:
        chosen_figure, move_figure = input('move_white(a2-a3): ').split('-')     
        x1, y1 = chosen_figure
        x2, y2 = move_figure
        y1, y2 = 8 - int(y1), 8 - int(y2)
        x1, x2 = ord(x1) - 97, ord(x2) - 97
        figure = board[y1][x1]
        if board[y1][x1] == pawn2 and pawn2.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'
        elif board[y1][x1] == knight2 and knight2.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'           
        elif board[y1][x1] == rook2 and rook2.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'
        elif board[y1][x1] == king2 and king2.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.' 
        elif board[y1][x1] == bishop2 and bishop2.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.' 
        elif board[y1][x1] == queen2 and queen2.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'
        else:
            print('Wrong move!')
            continue
        for row in board:
            print(*row, sep=' ')
        flag = False
    else:
        chosen_figure, move_figure = input('move_black(a2-a3): ').split('-')     
        x1, y1 = chosen_figure
        x2, y2 = move_figure
        y1, y2 = 8 - int(y1), 8 - int(y2)
        x1, x2 = ord(x1) - 97, ord(x2) - 97
        figure = board[y1][x1]  
        if board[y1][x1] == pawn1 and pawn1.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'
        elif board[y1][x1] == knight1 and knight1.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'
        elif board[y1][x1] == rook1 and rook1.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'
        elif board[y1][x1] == king1 and king1.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'  
        elif board[y1][x1] == bishop1 and bishop1.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'
        elif board[y1][x1] == queen1 and queen1.can_move(x1, y1, x2, y2) == True:
            board[y2][x2] = figure
            board[y1][x1] = '.'          
        else:
            print('Wrong move!')
            continue
        for row in board:
            print(*row, sep=' ')
        flag = True