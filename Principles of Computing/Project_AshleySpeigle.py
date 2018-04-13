import pygame

BLACK = (0,0,0)

pygame.init()

size = [700,743]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Galaga")

done = False

clock = pygame.time.Clock

backgroundSpace_image = pygame.image.load("starBackground.jpg").convert()

## MAIN PROGRAM LOOP ##
while done==False:
    for event in pygame.get():
        if event.type == pygame.QUIT:
            done=True

##ALL GAME LOGIC SHOULD GO HERE##

    screen.blit(background_image, [50,50])

## ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    pygame.display.flip()

    clock.tick(20)

##class Background:
##    def __init__(self):
##        self._space = True
##        self._display_space = None
##        self._image_space = None
##
##    def on_init(self):
##        pygame.init()
##        self._display_space = pygame.display.set_mode(size)
##
##        self._space = True
##        self._image_space = pygame.image.load("starBackground.jpg").convert()
####        screen.blit(backgroundImage, [0,0])
##        
##    def on_render(self):
##        self._display_space.fill((0,0,0))
##        self._display_space.blit(self._image_space,[0,0])
##        pygame.display.flip()

#Space ship#

##class Player:
##    x = 10
##    y = 10
##    speed = 1
##
##    def moveRight(self):
##        self.x = self.x + self.speed
##
##    def moveLeft(self):
##        self.x = self.x - self.speed
##        
##class App:
##    windowWidth = 800
##    windowHeight = 600
##    player = 0
##    x = 10
##    y = 10
##
##    def __init__(self):
##        self._running = True
##        self._display_surf = None
##        self._image_surf = None
##        self.player = Player()
##
##    def on_init(self):
##        pygame.init()
##        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
##
##        self._running = True
##        self._image_surf = pygame.image.load("spaceship_2.png").convert()
##
##    def on_event(self, event):
##        if event.type == QUIT:
##            self._running = False
##
##    def on_loop(self):
##        pass
##    
##    def on_render(self):
##        self._display_surf.fill((0,0,0))
##        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
##        pygame.display.flip()
##        
##    def on_cleanup(self):
##        pygame.quit()
##
##    def on_execute(self):
##        if self.on_init() == False:
##            self._running = False
##
##        while( self._running ):
##            pygame.event.pump()
##            keys = pygame.key.get_pressed()
##
##            if (keys[K_RIGHT]):
##                self.player.moveRight()
##
##            if (keys[K_LEFT]):
##                self.player.moveLeft()
##
##            if (keys[K_ESCAPE]):
##                self._running = False
##                
##            self.on_loop()
##            self.on_render()
##        self.on_cleanup()
##                                                     
##if __name__ == "__main__" :
##    theApp = App()
##    theApp.on_execute()                              
##        
##                                                     
