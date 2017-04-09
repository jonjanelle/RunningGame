'''
GameController handles getting input, coordinating
interactions between the player/enemies/environment,
and drawing everything to the screen
'''
import pygame
class GameController:
    def __init__(self, bg, player, enemies=[], gravity = 2):
        self.bg = bg
        self.player = player
        self.enemies = enemies
        self.gravity = gravity
        self.font = pygame.font.SysFont("monospace", 32)
        self.score = 0

    #Check for key presses and call the appropriate
    #functions
    def checkInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("left")

        if keys[pygame.K_RIGHT]:
            self.player.move("right")

        if keys[pygame.K_SPACE]:
            self.player.move("jump")

    #check for collisions between the player and enemies
    #If the player is struck, then the game is over. 
    def checkCollision(self):
        for enemy in self.enemies:
            if self.player.get_rect().colliderect(enemy.get_rect()):
                return True        
        return False

        
    #Draw background, player, and enemies to the screen
    #Applies gravity to the player and all enemies
    #Check for user key presses
    def update(self, screen):
        #update background
        self.bg.update(screen)

        #update player and apply gravity
        self.player.update(screen, self.bg.groundRect)
        self.player.vy+=self.gravity

        #update the enemies and apply gravity to them
        for enemy in self.enemies:
            if enemy.update(screen, self.bg.groundRect):
                self.score+=1
            enemy.vy+=self.gravity
            
        #check for key press
        self.checkInput()

        #Draw score
        scoreMsg=self.font.render("Score: "+str(self.score),True,(0,0,255))
        screen.blit(scoreMsg, (screen.get_width()/2-scoreMsg.get_width()/2,20))

        #Check for collisions between player and enemies.
        #Returns True if game should end, False otherwise
        return self.checkCollision()


        
