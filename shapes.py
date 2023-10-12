# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from pygame_grid import draw_grid
pygame.init()

# Create and open a pygame screen with the given size
width = 400
height = 400

screen = pygame.display.set_mode((width, height))

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

### PUT YOUR GAME CODE HERE
screen.fill("white")
point_list = [(145,0), (0,107), (55,277), (235,277), (290,107)]
pygame.draw.polygon(screen, "darkblue", point_list)
box = pygame.Rect(150, 300, 100, 50)
pygame.draw.rect(screen, "black", box)
pygame.draw.line(screen, "green", (60,300), (120,300), 4)
pygame.draw.circle(screen, "green", (300,50), 20)
box = pygame.Rect(300, 250, 40, 80)
pygame.draw.ellipse(screen, "black", box, 1)

# Uncomment this line to show a grid
draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
