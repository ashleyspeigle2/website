##Ashley Speigle
##This is a practice program for pygame

#imports a library of multiple functions
import pygame
import math

#Initializes the game engine
pygame.init()

#Defines some colors
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)

#Sets the height and width of the screen
size = (500,700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Square")

#Create an empty array
##snow_list = []

#Loop 50 times and add a snow flake in a random x,y position
##for i in range(50):
##    x = random.randrange(0,400)
##    y = random.randrange(0,400)
##    snow_list.append([x,y])

#Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

#This will be outside of the main loop
#Starting position of the rectangle
rect_x = 50
rect_y = 50

#Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

#Loop as long as done == False
while not done:
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked close
            done = True #Flag that we are done so we exit this loop

#All drawing code happens after the for loop and but
#Inside the main while not done in loop

#Clear the screen and set the screen background
screen.fill(Black)

## This is where the drawing occurs ##
pygame.draw.rect(screen, White, [rect_x,rect_y,50,50])
pygame.draw.rect(screen, Red, [rect_x + 10, rect_y + 10,30,30])
# Move the rectangle starting point
rect_x += rect_change_x
rect_y += rect_change_y

if rect_y > 450 or rect_y < 0:
    rect_change_y = rect_change_y * -1
if rect_x > 650 or rect_x < 0:
    rect_change_y = rect_change_y * -1

pygame.display.flip()

clock.tick(60)

pygame.quit()
