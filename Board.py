import pygame
from pieces import Pieces

# piece images
pawn_image = pygame.image.load(r"pawn.png")
rook_image = pygame.image.load(r"rook.png")
knight_image = pygame.image.load(r"knight.png")
bishop_image = pygame.image.load(r"bishop.png")
queen_image = pygame.image.load(r"queen.png")
king_image = pygame.image.load(r"king.png")
wpawn_image = pygame.image.load(r"wpawn.png")
wrook_image = pygame.image.load(r"wrook.png")
wknight_image = pygame.image.load(r"wknight.png")
wbishop_image = pygame.image.load(r"wbishop.png")
wqueen_image = pygame.image.load(r"wqueen.png")
wking_image = pygame.image.load(r"wking.png")

# -=-=-=-=-=-=-=-=-
class Board:
    def __init__(self, cellsize):
        self.board = []
        self.board_pieces = []
        self.cellsize = cellsize
        temp = 0
        temp2 = 0
        for i in range(8):
            self.board.append([])
            if temp2 % 2 == 0:
                for c in range(8):
                    if temp % 2 == 0:
                        self.board[i].append("w")
                    else:
                        self.board[i].append("b")
                    temp += 1
            else:
                for c in range(8):
                    if temp % 2 == 0:
                        self.board[i].append("b")
                    else:
                        self.board[i].append("w")    
                    temp += 1
            temp2 += 1
            
#         for i in range(8):
#             self.board_pieces.append([])
#             for c in range (8):
#                 if i == 7:
#                     self.board_pieces[i].append("p")
#                 else:
#                     self.board_pieces[i].append("")

        board_pieces = [['Br','Bh','Bb','Bq','Bk','Bb','Bh','Br'],
                             ['Bf','Bf','Bf','Bf','Bf','Bf','Bf','Bf'],
                             ['','','','','','','','','',''],
                             ['','','','','','','','','',''],
                             ['','','','','','','','','',''],
                             ['','','','','','','','','',''],
                             ['fw','fw','fw','fw','fw','fw','fw','fw'],
                             ['rw','hw','bw','qw','kw','bw','hw','rw']]
        self.board_pieces = board_pieces
        print(self.board_pieces)  
            
                    
        
    def draw_pieces(self, screen):
        for y, col in enumerate(self.board_pieces):
            for x, cell in enumerate(col):
                if "w" in self.board_pieces[y][x]:
                    if "p" in self.board_pieces[y][x]:
                        screen.blit(wpawn_image, (x*200, y*200))
                    if "f" in self.board_pieces[y][x]:
                        screen.blit(wpawn_image, (x*200, y*200))
                    if "r" in self.board_pieces[y][x]:
                        screen.blit(wrook_image, (x*200, y*200))
                    if "b" in self.board_pieces[y][x]:
                        screen.blit(wbishop_image, (x*200, y*200))
                    if "h" in self.board_pieces[y][x]:
                        screen.blit(wknight_image, (x*200, y*200))
                    if "q" in self.board_pieces[y][x]:
                        screen.blit(wqueen_image, (x*200, y*200))
                    if "k" in self.board_pieces[y][x]:
                        screen.blit(wking_image, (x*200, y*200))
                else:
                    if "p" in self.board_pieces[y][x]:
                        screen.blit(pawn_image, (x*200, y*200))
                    if "f" in self.board_pieces[y][x]:
                        screen.blit(pawn_image, (x*200, y*200))
                    if "r" in self.board_pieces[y][x]:
                        screen.blit(rook_image, (x*200, y*200))
                    if "b" in self.board_pieces[y][x]:
                        screen.blit(bishop_image, (x*200, y*200))
                    if "h" in self.board_pieces[y][x]:
                        screen.blit(knight_image, (x*200, y*200))
                    if "q" in self.board_pieces[y][x]:
                        screen.blit(queen_image, (x*200, y*200))
                    if "k" in self.board_pieces[y][x]:
                        screen.blit(king_image, (x*200, y*200))
    
    
    
    
    
        
    def draw_board(self, screen):
        black=(120,158,87)
        off_white=(232,219,200)
        for y, col in enumerate(self.board):
            for x, cell in enumerate(col):
                if self.board[y][x] == "w":
                    # white cell
                    pygame.draw.rect(screen, off_white,(x*self.cellsize,y*self.cellsize,self.cellsize,self.cellsize))
                else:
                    # black cell
                    pygame.draw.rect(screen, black,(x*self.cellsize,y*self.cellsize,self.cellsize,self.cellsize))
                
        