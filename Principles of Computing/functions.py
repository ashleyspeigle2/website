##functions and control structures

from graphics import *

win = GraphWin()

catImage = Image(Point(100,100),"giphy_cat.gif")

sizeX = catImage.getWidth()
sizeY = catImage.getHeight()

print(sizeX,sizeY)
catImage = Image(Point(sizeX /2, sizeY/2),"giphy_cat.gif")

win = GraphWin("image", sizeX, sizeY)

catImage.draw(win)


for x in range(sizeX):
    for y in range(sizeY):
        red, green, blue = catImage.getPixel(x,y)
        ash = int(round(0.299 * red + 0.587 * green + 0.114 * blue))
        catImage.setPixel(x,y, color_rgb(ash,ash,ash))




##def absolute( x ):
##    if x < 0:
##        x = x * -1
##
##    return x
##
##def main():
##    num = -57
##
##    positiveNum = absolute(num)
##    
##    print( positiveNum )

