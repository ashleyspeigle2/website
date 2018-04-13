##Ashley Speigle Galaga Project

import pygame
import time
import random

##Initializes the game
pygame.init()

#Sets the height and width
display_width = 700
display_height = 743

#Defines the colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
yellow = (255,255,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

space_width = 50

#Runs the window
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("My Galaga")
clock = pygame.time.Clock()

#Loads images in that are needed for the game
backgroundSpaceImg = pygame.image.load("starBackground.jpg")
spaceImg = pygame.image.load("galagaShip.png")

pygame.display.set_icon(spaceImg)

pause = False

screen_rect = gameDisplay.get_rect()

#The objects which are being defined for the actual game
def bot(botx, boty, botw, both, color):
    pygame.draw.rect(gameDisplay, color, [botx, boty, botw, both])
    
def spaceship(x,y):
    gameDisplay.blit(spaceImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()

    ##time.sleep(2)
##
##    game_loop()
##    
##
##def shot():
##    message_display("Game Over")


##This allows us to draw the bullet to shoot out of the spaceship
def bullet(bulletx, bullety, bulletw, bulleth, color):
    pygame.draw.rect(gameDisplay, color, [bulletx, bullety, bulletw, bulleth])

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    ##print(click)
## Allows the buttons to appear to be interactive
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",13)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(TextSurf, TextRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("PAUSED", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("CONTINUE",120,570,100,50,green,bright_green,unpause)
        button("QUIT",490,570,100,50,red,bright_red,quitgame)        
        
        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Galaga", largeText)

        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("START GAME",120,570,100,50,green,bright_green,game_loop)
        button("QUIT",490,570,100,50,red,bright_red,quitgame)        
        
        pygame.display.update()
        clock.tick(15)



 
def game_loop():

    global pause
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    #get this to start in a specific spot, not random#
    bot_startx = random.randrange(50, display_width)
    bot_starty = 300
    bot_speed = 4
    bot_width = 30
    bot_height = 31

#Determines where the bullet will shoot from
    bullet_startx = x
    bullet_starty = y
    bullet_speed = 8
    bullet_width = 4
    bullet_height = 10

    done = False

    while not done:
    #Event Handling Loop#
        for event in pygame.event.get():
        #creates a list of events that has happened in a frame
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5        
                if event.key == pygame.K_SPACE:
                    bullet_starty += bullet_speed
                    print("fire")
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    ##if bullet_starty > display_height:
                        ##bullet_starty = 0 - bullet_height

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_SPACE:
                        bullet_starty += bullet_speed
                        


        ##spaceImg.clamp_ip(gameDisplay_rect)
        
        x += x_change            

        gameDisplay.blit(backgroundSpaceImg, [0,0])

        #This is where the enemy bot drawings are made
        ##bot(botx, boty, botw, both, color)
        bot(bot_startx, bot_starty, bot_width, bot_height, green)
        bot_startx += bot_speed
        
        ##bullet(bulletx, bullety, bulletw, bulleth, color)
            

        if bot_startx > display_height:
            bot_startx = 0 - bot_height

        if y < bot_starty + bot_height:
            print("step 1")
            #bot_starty = 0
                #This will draw the enemy bot in this position
        
        ##if x > display_width - space_width or x < 0:
            ##shot()


        bullet(bullet_startx, bullet_starty, bullet_width, bullet_height, yellow)
        spaceship(x,y)
####        bullet_starty += bullet_speed
##
####        if bullet_starty == spaceship:
####            bot_starty = 0 - bullet_height
            

        pygame.display.update()

        clock.tick(60)

game_intro()        
game_loop()
pygame.quit()
quit()

