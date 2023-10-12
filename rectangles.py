# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from pygame_grid import draw_grid
pygame.init()

# Create and open a pygame screen with the given size
width = 640
height = 220

screen = pygame.display.set_mode((width, height))

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

### PUT YOUR GAME CODE HERE
screen.fill("lightgray")

box = pygame.Rect(50, 20, 120, 100)
pygame.draw.rect(screen, "red", box)
box = pygame.Rect(100, 60, 120, 100)
pygame.draw.rect(screen, "green", box)
box = pygame.Rect(150, 100, 120, 100)
pygame.draw.rect(screen, "blue", box)
box = pygame.Rect(350, 20, 120, 100)
pygame.draw.rect(screen, "red", box, 1)
box = pygame.Rect(400, 60, 120, 100)
pygame.draw.rect(screen, "green", box, 4)
box = pygame.Rect(450, 100, 120, 100)
pygame.draw.rect(screen, "blue", box, 8)

# Uncomment this line to show a grid
draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
