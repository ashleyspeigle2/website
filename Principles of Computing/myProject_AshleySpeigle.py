import pygame
import time
import random

pygame.init()

display_width = 700
display_height = 743

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

space_width = 50

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("My Galaga")
clock = pygame.time.Clock()

backgroundSpaceImg = pygame.image.load("starBackground.jpg")
spaceImg = pygame.image.load("galagaShip.png")

##screen_rect = gameDisplay.get_rect()

def bot(botx, boty, botw, both, color):
    pygame.draw.rect(gameDisplay, color, [botx, boty, botw, both])
    
def spaceship(x,y):
    gameDisplay.blit(spaceImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
##
##def message_display(text):
##    largeText = pygame.font.Font("freesansbold.ttf",115)
##    TextSurf, TextRect = text_objects(text, largeText)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf, TextRect)
##
##    pygame.display.update()
##
##    time.sleep(2)
##
##    game_loop()
##    
##
##def shot():
##    message_display("Game Over")


##This allows us to draw the bullet to shoot out of the spaceship
def bullet(bulletx, bullety, bulletw, bulleth, color):
    pygame.draw.rect(gameDisplay, color, [bulletx, bullety, bulletw, bulleth])

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font("freesansbold.ttf",115)
        TextSurf, TextRect = text_objects("Galaga", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
 
def game_loop():
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    #get this to start in a specific spot, not random#
    bot_startx = 0 #random.randrange(0,display_width)
    bot_starty = 0
    bot_speed = 8
    bot_width = 30
    bot_height = 31

#Determines where the bullet will shoot from
    bullet_startx = 0
    bullet_starty = 0
    bullet_speed = 8
    bullet_width = 4
    bullet_height = 4

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
        bot(bot_startx, bot_starty, bot_width, bot_height, red)
        bot_startx += bot_speed
        
        spaceship(x,y)

        if bot_startx > display_height:
            bot_startx = 0 - bot_height
            #bot_starty = 0
                #This will draw the enemy bot in this position
        
        ##if x > display_width - space_width or x < 0:
            ##shot()


        bullet(bullet_startx, bullet_starty, bullet_width, bullet_height, white)
##        bullet_starty += bullet_speed

        spaceship(x,y)

##        if bullet_starty == spaceship:
##            bot_starty = 0 - bullet_height
            

        pygame.display.update()

        clock.tick(60)

game_intro()        
game_loop()
pygame.quit()
quit()

