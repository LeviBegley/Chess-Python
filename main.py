import pygame




def main():
    pygame.init()
    
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    green=(0,255,0)
    
    
    screen_width=1600
    screen_height=1600
    screen=pygame.display.set_mode([screen_width, screen_height])
    screen.fill(white)
    
    x = 0
    y = 200
    while x != 1600:
        pygame.draw.rect(screen, green,(x,0,200,200))
        x += 400
        pygame.draw.rect(screen, red,(y,0,200,200))
        y += 400
    

    pygame.display.init()
    
    pygame.display.update()
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
    
    
    
main()

