import pygame
import numpy
from Board import Board
from pieces import Pieces

cellsize = 200
pawn_image = pygame.image.load(r"C:\Users\beglelc\Documents\2021\Comp Sci\Chess\pawn.png")
def main():
    pygame.init()
    
    white=(255,255,255)
    black=(30,30,30)
    red=(255,0,0)
    green=(0,255,0)
    cream=(252,239,215)
    brown=(145,98,10)
    black=(0,0,0)
    
    screen_width=1600
    screen_height=1600
    screen=pygame.display.set_mode([screen_width, screen_height])
    screen.fill(white)
    
    board = Board(cellsize)
    

    
    double_black = 0
    double_white = 0

    Bf_counter_1 = 0
    Bf_counter_2 = 0




    pygame.display.init()
    
    #turns
    turn_counter = "white"
    wking_move_counter = 0
    bking_move_counter = 0
    mode = "none"
    while True:
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        board.draw_board(screen)
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_down_column = (pos[0] // 200)  # column
                mouse_down_row = (pos[1] // 200)  # row
                mode = "pressed"
                
      
                 
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if mode == "pressed":
                    mode = "unpressed"
                    pos = pygame.mouse.get_pos()
                    mouse_up_column = (pos[0] // 200)  # column
                    mouse_up_row = (pos[1] // 200)  # row
# moves --------------------------------
                    up = mouse_down_row - 1, mouse_down_column
                    down = mouse_down_row + 1, mouse_down_column
                    up2 = mouse_down_row - 2, mouse_down_column
                    down2 = mouse_down_row + 2, mouse_down_column
                    left = mouse_down_row, mouse_down_column - 1
                    right = mouse_down_row, mouse_down_column + 1
                    up_left = mouse_down_row - 1, mouse_down_column - 1
                    up_right = mouse_down_row - 1, mouse_down_column + 1
                    down_left = mouse_down_row + 1, mouse_down_column - 1
                    down_right = mouse_down_row + 1, mouse_down_column + 1
                
                    pawn_valid_w = []
                    pawn_valid_b = []
                    pawnf_valid_w = []
                    pawnf_valid_b = []
                    
                    try:
                        if board.board_pieces[mouse_down_row - 1] [mouse_down_column] == '':
                            pawn_valid_w = [up]
                    except:
                        pass
                    try:
                        if board.board_pieces[mouse_down_row + 1] [mouse_down_column] == '':
                            pawn_valid_b = [down]
                    except:
                        pass
                    try:
                        if board.board_pieces[mouse_down_row - 1] [mouse_down_column] == '':
                            pawnf_valid_w = [up]
                            if board.board_pieces[mouse_down_row - 2] [mouse_down_column] == '':
                                pawnf_valid_w = [up, up2]
                    except:
                        pass
                    try:
                        if board.board_pieces[mouse_down_row + 1] [mouse_down_column] == '':
                            pawnf_valid_b = [down]
                            if board.board_pieces[mouse_down_row + 2] [mouse_down_column] == '':
                                pawnf_valid_b = [down, down2]
                    except:
                        pass
   
# pawn attacking -------------------------------------
                    pawn_attack_w = []
                    pawn_attack_b = []
                    try:
                        if board.board_pieces[mouse_down_row - 1] [mouse_down_column + 1] != '':
                            p_valid = mouse_down_row - 1, mouse_down_column + 1
                            pawn_attack_w.append(p_valid)
                        if board.board_pieces[mouse_down_row - 1] [mouse_down_column - 1] != '':
                            p_valid = mouse_down_row - 1, mouse_down_column - 1 
                            pawn_attack_w.append(p_valid)
                        
                        if board.board_pieces[mouse_down_row + 1] [mouse_down_column + 1] != '':
                            p_valid = mouse_down_row + 1, mouse_down_column + 1
                            pawn_attack_b.append(p_valid)
                        if board.board_pieces[mouse_down_row + 1] [mouse_down_column - 1] != '':
                            p_valid = mouse_down_row + 1, mouse_down_column - 1
                            pawn_attack_b.append(p_valid)
                    except:
                        pass
                    
#en passant --------------------------------------------------
                    Bf_counter_1 = sum(x.count('Bf') for x in board.board_pieces)

                    
                    en_passant_w = []
                    en_passant_b = []


                    if double_black == 1:
                        try:
                            if 'Bp' in board.board_pieces[mouse_down_row] [mouse_down_column - 1]:
                                if mouse_down_row == 3:
                                    p_valid = mouse_down_row - 1, mouse_down_column - 1
                                    en_passant_w.append(p_valid)
                                     
                            if 'Bp' in board.board_pieces[mouse_down_row] [mouse_down_column + 1]:
                                if mouse_down_row == 3:
                                    p_valid = mouse_down_row - 1, mouse_down_column + 1
                                    en_passant_w.append(p_valid)
                        except:
                            pass
                    if double_white == 1:
                        try:
                            if 'pw' in board.board_pieces[mouse_down_row] [mouse_down_column - 1]:
                                if mouse_down_row == 4:
                                    p_valid = mouse_down_row + 1, mouse_down_column - 1
                                    en_passant_b.append(p_valid)
                                     
                            if 'pw' in board.board_pieces[mouse_down_row] [mouse_down_column + 1]:
                                if mouse_down_row == 4:
                                    p_valid = mouse_down_row + 1, mouse_down_column + 1
                                    en_passant_b.append(p_valid) 
                        except:
                            pass
                                
                    
                    Bf_counter_2 = sum(x.count('Bf') for x in board.board_pieces)
                    double_black = 0
                    double_white = 0
#knights -------------------------------
                    knight_up_right = mouse_down_row - 2, mouse_down_column + 1
                    knight_up_left = mouse_down_row - 2, mouse_down_column - 1
                    knight_right_up = mouse_down_row - 1, mouse_down_column + 2
                    knight_right_down = mouse_down_row + 1, mouse_down_column + 2
                    knight_left_up = mouse_down_row - 1, mouse_down_column - 2
                    knight_left_down = mouse_down_row + 1, mouse_down_column - 2
                    knight_down_right = mouse_down_row + 2, mouse_down_column + 1
                    knight_down_left = mouse_down_row + 2, mouse_down_column - 1
                    knight_valid_list = [knight_up_right, knight_up_left, knight_right_up, knight_right_down, knight_left_up, knight_left_down, knight_down_left, knight_down_right]
#bishops -----------------------
                    bishop_valid_list = []
                    if [mouse_up_row] < [mouse_down_row]:
                        row_multi = -1
                    else:
                        row_multi = 1
                    if [mouse_up_column] < [mouse_down_column]:
                        column_multi = -1
                    else:
                        column_multi = 1
                    bish_row = mouse_down_row
                    bish_column = mouse_down_column
                    for i in range(1,8):
                        try:
                            if (board.board_pieces[bish_row + row_multi][bish_column + column_multi]) == "":
                                bishop_valid = bish_row + row_multi, bish_column + column_multi
                                bish_row += row_multi
                                bish_column += column_multi
                                bishop_valid_list.append(bishop_valid)
                        except:
                            pass
                    bishop_valid = bish_row + row_multi, bish_column + column_multi
                    bish_row += row_multi
                    bish_column += column_multi
                    bishop_valid_list.append(bishop_valid)
                    
#rooks --------------------------------------------------------
                    rook_valid_list = []
                    if [mouse_up_row] > [mouse_down_row]:
                        row_multi = 1
                    elif [mouse_up_row] == [mouse_down_row]:
                        row_multi = 0
                    else:
                        row_multi = -1

                        
                    if [mouse_up_column] > [mouse_down_column]:
                        column_multi = 1
                    elif [mouse_up_column] == [mouse_down_column]:
                        column_multi = 0
                    else:
                        column_multi = -1
                    
                    print(row_multi, column_multi)
                    rook_row = mouse_down_row
                    rook_column = mouse_down_column
                    for i in range(1,8):
                        try:
                            if (board.board_pieces[rook_row + row_multi][rook_column + column_multi]) == "":
                                rook_valid = rook_row + row_multi, rook_column + column_multi
                                rook_row += row_multi
                                rook_column += column_multi
                                rook_valid_list.append(rook_valid)
                        except:
                            pass
                    rook_valid = rook_row + row_multi, rook_column + column_multi
                    rook_row += row_multi
                    rook_column += column_multi
                    rook_valid_list.append(rook_valid)


                            
                    

                    print(board.board_pieces[mouse_down_row][mouse_down_column])
                    print(mouse_down_row,mouse_down_column)
                    
                    
                    pawn_valid_moves_w = pawn_valid_w + pawn_attack_w + en_passant_w
                    pawn_valid_moves_b = pawn_valid_b + pawn_attack_b + en_passant_b
                    pawnf_valid_moves_w = pawnf_valid_w + pawn_attack_w
                    pawnf_valid_moves_b = pawnf_valid_b + pawn_attack_b
                    
                                     
# Moving/Valid checking code --------------------------------------------------------------------
                    
                    
                    
                    
                    
                    
                    if 'p' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "white":
                        valid_moves = pawn_valid_moves_w
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)

                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column] or 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                if mouse_up_row == mouse_down_row - 1 and mouse_up_column == mouse_down_column - 1:
                                    board.board_pieces[mouse_down_row][mouse_down_column - 1] = ""
                                if mouse_up_row == mouse_down_row - 1 and mouse_up_column == mouse_down_column + 1:
                                    board.board_pieces[mouse_down_row][mouse_down_column + 1] = ""
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "black"
                                pygame.event.clear()
                                
                    if 'p' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "black":
                        valid_moves = pawn_valid_moves_b
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column] or 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                if mouse_up_row == mouse_down_row + 1 and mouse_up_column == mouse_down_column - 1:
                                    board.board_pieces[mouse_down_row][mouse_down_column - 1] = ""
                                if mouse_up_row == mouse_down_row + 1 and mouse_up_column == mouse_down_column + 1:
                                    board.board_pieces[mouse_down_row][mouse_down_column + 1] = ""
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "white"
                                pygame.event.clear()
                                
                    if 'f' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "white":
                        valid_moves = pawnf_valid_moves_w
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column] or 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                if mouse_up_row == mouse_down_row - 2:
                                    double_white = 1
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', "pw"
                                turn_counter = "black"
                                pygame.event.clear()
                                
                    if 'f' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "black":
                        valid_moves = pawnf_valid_moves_b
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column] or 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                if mouse_up_row == mouse_down_row + 2:
                                    double_black = 1
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', "Bp"
                                turn_counter = "white"
                                pygame.event.clear()
                                
                    if 'k' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "white":
                        valid_moves = up, left, down, right, up_left, up_right, down_left, down_right
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        rook_check = [mouse_up_row], [mouse_up_column]
                        if wking_move_counter == 0:
                            if rook_check == ([7],[0]) and 'rw' in board.board_pieces[mouse_up_row][mouse_up_column]:
                                if board.board_pieces[7][1] == '' and board.board_pieces[7][2] == '' and board.board_pieces[7][3] == '':
                                    board.board_pieces[7][3] = 'rw'
                                    board.board_pieces[7][2] = 'kw'
                                    board.board_pieces[mouse_down_row][mouse_down_column] = ''
                                    board.board_pieces[mouse_up_row][mouse_up_column] = ''
                                    wking_move_counter += 1
                                    turn_counter = "black"
                                    pygame.event.clear()
                            if rook_check == ([7],[7]) and 'rw' in board.board_pieces[mouse_up_row][mouse_up_column]:
                                if board.board_pieces[7][6] == '' and board.board_pieces[7][5] == '':
                                    board.board_pieces[7][5] = 'rw'
                                    board.board_pieces[7][6] = 'kw'
                                    board.board_pieces[mouse_down_row][mouse_down_column] = ''
                                    board.board_pieces[mouse_up_row][mouse_up_column] = ''
                                    wking_move_counter += 1
                                    turn_counter = "black"
                                    pygame.event.clear()
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                wking_move_counter += 1
                                turn_counter = "black"
                                pygame.event.clear()
                                
                                
                                
                    if 'k' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "black":
                        valid_moves = up, left, down, right, up_left, up_right, down_left, down_right
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column, 
                        print("-----")
                        print(valid_checker)
                        rook_check = [mouse_up_row], [mouse_up_column]
                        if bking_move_counter == 0:
                            if rook_check == ([0],[0]) and 'Br' in board.board_pieces[mouse_up_row][mouse_up_column]:
                                if board.board_pieces[0][1] == '' and board.board_pieces[0][2] == '' and board.board_pieces[0][3] == '':
                                    board.board_pieces[0][3] = 'Br'
                                    board.board_pieces[0][2] = 'Bk'
                                    board.board_pieces[mouse_down_row][mouse_down_column] = ''
                                    board.board_pieces[mouse_up_row][mouse_up_column] = ''
                                    bking_move_counter += 1
                                    turn_counter = "white"
                                    pygame.event.clear()
                            if rook_check == ([0],[7]) and 'Br' in board.board_pieces[mouse_up_row][mouse_up_column]:
                                if board.board_pieces[0][6] == '' and board.board_pieces[0][5] == '':
                                    board.board_pieces[0][5] = 'Br'
                                    board.board_pieces[0][6] = 'Bk'
                                    board.board_pieces[mouse_down_row][mouse_down_column] = ''
                                    board.board_pieces[mouse_up_row][mouse_up_column] = ''
                                    bking_move_counter += 1
                                    turn_counter = "white"
                                    pygame.event.clear()
                        
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                bking_move_counter += 1
                                turn_counter = "white"
                                pygame.event.clear()
                                
                                
                    if 'b' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "white":
                        valid_moves = bishop_valid_list
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)

                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "black"
                                pygame.event.clear()
                                
                    if 'b' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "black":
                        valid_moves = bishop_valid_list
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)

                        if valid_checker in valid_moves:
                            print("valid")
                            if 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "white"
                                pygame.event.clear()
                                
                    if 'r' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "black":
                        valid_moves = rook_valid_list
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "white"
                                pygame.event.clear()
                                
                    if 'r' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "white":
                        valid_moves = rook_valid_list
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "black"
                                pygame.event.clear()


                                
                    
                    queen_valid_list = bishop_valid_list + rook_valid_list
                    
                    if 'q' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "white":
                        valid_moves = queen_valid_list
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "black"
                                pygame.event.clear()
                        
                    if 'q' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "black":
                        valid_moves = queen_valid_list
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "white"
                                pygame.event.clear()
                                
                
                                
                    if 'h' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "white":
                        valid_moves = knight_valid_list
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'w' in board.board_pieces[mouse_down_row][mouse_down_column] and 'w' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "black"
                                pygame.event.clear()
                        
                    if 'h' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and turn_counter == "black":
                        valid_moves = knight_valid_list
                        print(valid_moves)
                        valid_checker = mouse_up_row, mouse_up_column
                        print("-----")
                        print(valid_checker)
                        if valid_checker in valid_moves:
                            print("valid")
                            if 'B' in board.board_pieces[mouse_down_row][mouse_down_column] and 'B' in board.board_pieces[mouse_up_row][mouse_up_column]:                           
                                pass       
                            elif "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                                board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
                                turn_counter = "white"
                                pygame.event.clear()


                    

    
                    print(turn_counter)
                    
                        
        
        
        
        
        board.draw_board(screen)
        board.draw_pieces(screen)
        
        pygame.display.flip()
        pygame.display.update()
        
main()

