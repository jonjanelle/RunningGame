import pygame,sys
####Main Menu
###################################
def showMenu(screen,bgImg):
    W=screen.get_width()
    H=screen.get_height()
    font=pygame.font.SysFont(None, 40)
    tfont=pygame.font.SysFont(None, 60)
    titleText = tfont.render("Scrolling Game - Main Menu",True,(50,50,250))

    startButton = pygame.Rect(W/2-int(.12*W), int(.2*H), int(.25*W), int(.1*H))
    startText = font.render("Start Game", True, (255,255,255))

    quitButton = pygame.Rect(W/2-int(.12*W), int(.35*H), int(.25*W), int(.1*H))
    quitText = font.render("Quit Game", True, (255,255,255))

    menuOpen = True
    while menuOpen:
        #draw menu background 
        screen.blit(bgImg,(0,0))

        screen.blit(titleText, (W/2-titleText.get_width()/2, 20))

        #Start button code
        if startButton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (150, 50,50), startButton)
            pygame.draw.rect(screen, (150, 255,50), startButton,3)
            if pygame.mouse.get_pressed()[0]==1:
                menuOpen=False
        else:
            pygame.draw.rect(screen, (225, 50,50), startButton)
            pygame.draw.rect(screen, (0, 50,255), startButton,1)
        
        screen.blit(startText,(startButton.x+25,startButton.y+startText.get_height()/2))

        #Quit button code
        if quitButton.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (150, 50,50), quitButton)
            pygame.draw.rect(screen, (150, 255,50), quitButton,3)
            if pygame.mouse.get_pressed()[0]==1:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, (225, 50,50), quitButton)
            pygame.draw.rect(screen, (0, 50,255), quitButton,1)
        
        screen.blit(quitText,(quitButton.x+25,quitButton.y+quitText.get_height()/2))
    
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    menuOpen = False
