import pygame
class Enemy:
    def __init__(self, img, vx, x=0,y=0):
        self.img = img
        self.vx=vx
        self.x = x
        self.y = y
        self.vy = 0
        self.height=self.img.get_height()
        self.width=self.img.get_width()
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())


    def update(self, screen,groundRect):
        #if offScreen is set to true in this method, then player should get a point
        offScreen = False
        #Draw enemy to screen
        screen.blit(self.img, (self.x, self.y))
        #move to the left
        self.x -= self.vx 
        #check if off screen, reset position if yes
        if self.x < 0: 
            self.x=screen.get_width()+10
            offScreen=True

        #If enemy is falling, make it stop upon hitting ground
        self.y+=self.vy
        if self.get_rect().colliderect(groundRect):
            self.vy=0
            self.y=groundRect.y-self.height
            
        #returns True if player should get a point, false otherwise
        return offScreen
