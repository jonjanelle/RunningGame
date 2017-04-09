'''
Help the cat spaceperson jump over the angry blob!
An engrossing tale filled with mysery and intrigue for the ages...
'''
import pygame,sys,random,math
from player import *
from enemy import *
from gamecontroller import *
from scrollbackground import *
from mainmenu import *

#Always initialize pygame first or else.
pygame.init()

#SETUP WINDOW
#Create variables to hold window dimensions
W = 800
H = 600

#Create a new window
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Scrolling Game Demo")

#Setup clock and framerate 
clock = pygame.time.Clock()
FPS = 30

#Load player images
playerImages = []
for i in range(7):
    img = pygame.image.load("images/player"+str(i+1)+".png")
    playerImages.append(img)
    
#Load enemy image
enemyImg = pygame.image.load("images/anger.png")

#Load background image
bgImg = pygame.image.load("images/bg1.png").convert()

#Setup ground rectangle
ground = pygame.Rect(0, H-95, W, 95) #ground 95 pixels wide

#################
#START MAIN LOOPS
#################
#outer loop resets player/score/enemies and shows main menu
while True:
    #Create player object
    player = Player(playerImages,15,3) #images, jump, speed
    #Create enemy object
    enemy = Enemy(enemyImg, 5,W,0) #image, speed, start x, stary y
    #create scrolling background object
    bg = ScrollBackground(bgImg, ground, 2) #image, ground, scroll speed
    #Create GameController object to coordinate the background, player, enemy
    gc = GameController(bg, player, [enemy])
    #Show main menu
    showMenu(screen, bgImg)

    #Inner loop is main game loop
    while True:   
        for event in pygame.event.get(): #Terminate program if user tries to quit window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #GameController frame update
        if gc.update(screen):
            break
        
        # UPDATE DISPLAY #
        pygame.display.update((0,0,W,H))
        
        clock.tick(FPS)
