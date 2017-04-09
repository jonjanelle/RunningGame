import pygame
class Player:
    def __init__(self, images, jump, vx, x=10):
        self.images = images #a list of loaded images
        self.jump = jump #jump height. Bigger = higher jump
        self.imageNum = 0 #start by showing the first image in the list
        self.vx = vx
        self.vy = 0
        self.x = x
        self.y = 0
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        self.jumping = True

    def move(self, d):
        if d=="left":
            self.x-=self.vx
        elif d=="right":
            self.x+=self.vx
        elif d=="jump" and not self.jumping:
            self.vy=-self.jump
            self.jumping = True

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self, screen, groundRect):
        screen.blit(self.images[self.imageNum],(self.x, self.y))
        self.imageNum+=1
        if self.imageNum >= len(self.images):
            self.imageNum = 0
    
        self.y+=self.vy
        if self.get_rect().colliderect(groundRect):
            self.vy=0
            self.y=groundRect.y-self.height
            self.jumping = False
        
        
