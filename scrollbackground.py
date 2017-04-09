class ScrollBackground:
    def __init__(self, img, groundRect, speed=1):
        self.img = img
        self.speed = speed
        self.x = 0 #start with upper-left corner at origin
        self.y = 0
        self.groundRect=groundRect
        self.width=self.img.get_width()

    def update(self, screen):
        #scrolling accomplished through using two versions of same image
        screen.blit(self.img, (self.x, self.y))
        screen.blit(self.img, (self.x+self.width,self.y))
        self.x -= self.speed
        if abs(self.x)>self.width:
            self.x = 0
        
    
    
