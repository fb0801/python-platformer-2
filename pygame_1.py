import pygame, sys


from pygame import *
pygame.init()

pygame.display.set_caption('My first pygame')#title of the window


window_size = (400,400)

screen=pygame.display.set_mode(window_size, 0, 32)


while True:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
