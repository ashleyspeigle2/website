##Ashley Speigle
    ##This program runs the game 'Galaga'
        ## Final Project

#imports a library of multiple functions
import pygame,graphics,math
##initializes game content
pygame.init()

##def drawBackground():
## This sets the background image for the game
##    pygame.display.init()
##screen = pygame.display.set_mode((700,500))
##set_mode(resolution(0,0),flags=0, depth=0)
##background_image = pygame.image.load("starBackground.jpg").convert()
##screen.blit(background_image, [0,0])
##
##drawBackground()

def mainProgram():
    #Defines some colors
    Black = (0,0,0)
    White = (255,255,255)
    Green = (0,255,0)
    Red = (255,0,0)

    #Sets the height and width of the screen
    size = (700,500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Galaga Game")

    ###Loop until the user clicks the close button
    ##done = False

    #Manages how fast the screen updates
    clock = pygame.time.Clock()
#Loop until the user clicks the close button
    done = False
#Loop as long as done == False
    while not done:
        for event in pygame.event.get(): #User did something
            if event.type == pygame.QUIT: #If user clicked close
                done = True
                
    #Game logic should go here


    #Clear the screen and set the screen background
    screen.fill(White)

    ## This is where the drawing occurs ##

    Rect = [55,50,20,25]
    pygame.draw.rect(screen, Red, Rect, 0)
 
    pygame.display.flip()

    clock.tick(60)

mainProgram()

pygame.quit()
