# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from pygame_grid import draw_grid
pygame.init()

# Create and open a pygame screen with the given size
width = 640
height = 360
screen = pygame.display.set_mode((width, height))

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

### PUT YOUR GAME CODE HERE
screen.fill("lawngreen")
pygame.draw.circle(screen, "white", (320,100), 40)
pygame.draw.circle(screen, "black", (320,100), 40, 5)
pygame.draw.circle(screen, "black", (320,85), 5)
pygame.draw.circle(screen, "black", (340,80), 5)
pygame.draw.line(screen, "black", (320,110), (340,100), 5)
pygame.draw.line(screen, "darkred", (320,140), (320,220), 10)
pygame.draw.line(screen, "darkred", (320,143), (240,180), 10)
pygame.draw.line(screen, "darkred", (320,143), (400,180), 10)
pygame.draw.line(screen, "darkblue", (320,220), (300,320), 10)
pygame.draw.line(screen, "darkblue", (320,220), (340,320), 10)
pygame.draw.line(screen, "black", (280,320), (300,320), 10)
pygame.draw.line(screen, "black", (340,320), (360,320), 10)

# Uncomment this line to show a grid
draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
