import pygame
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
    

    




    
    pygame.display.init()
    
    
    
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
                
                #print(mouse_down_row, mouse_down_column)
                #print(board.board_pieces[mouse_down_row][mouse_down_column])
                
#             if "p" in board.board_pieces[mouse_down_row][mouse_down_column]:
#                  print("deese")

                 
                 
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if mode == "pressed":
                    mode = "unpressed"
                    pos = pygame.mouse.get_pos()
                    mouse_up_column = (pos[0] // 200)  # column
                    mouse_up_row = (pos[1] // 200)  # row
                    
    #                 print(mouse_up_row, mouse_up_column)


                    if "" in board.board_pieces[mouse_up_row][mouse_up_column]:
                        board.board_pieces[mouse_down_row][mouse_down_column], board.board_pieces[mouse_up_row][mouse_up_column] = '', board.board_pieces[mouse_down_row][mouse_down_column]
    #                     mouse_down_row, mouse_down_column = mouse_up_row, mouse_up_column
                        #board.board_pieces[mouse_up_row][mouse_up_column], = board.board_pieces[mouse_down_row][mouse_down_column]
                        #board.board_pieces[mouse_down_row][mouse_down_column] = ''
                        pygame.event.clear()
                   



                    

        
        
        
        board.draw_board(screen)
        board.draw_pieces(screen)
        
        pygame.display.flip()
        pygame.display.update()
        
main()

