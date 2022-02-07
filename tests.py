#import pygame, sys
#from pygame.locals import *
#
#pygame.init()
#
#fenetre = pygame.display.set_mode((640, 480))
#
#perso = pygame.image.load("perso.png").convert_alpha()
#position_perso = perso.get_rect()
#
#
#
#while True :
#    fenetre.fill([10,186,181])
#    fenetre.blit(perso, position_perso)
#    for event in pygame.event.get():   
#      if event.type == KEYDOWN:
#        if event.key == K_RIGHT:
#          print("flèche droite appuyée")
#    pygame.key.set_repeat(50)
#    for event in pygame.event.get():    
#      if event.type == MOUSEBUTTONDOWN and event.button == 1 :
#          print("clic gauche détecté")
#    position_perso.topleft = (100,200)
#    pygame.display.flip()


#import pygame, sys
#from pygame.locals import *
#from random import randint
#
#pygame.init()
#
#fenetre = pygame.display.set_mode((640, 480))
#
#perso = pygame.image.load("perso.png").convert_alpha()
#
#position_perso = perso.get_rect()
#
#while True :
#    fenetre.fill([10,186,181])
#    position_perso.topleft = (500,300)
#    position_perso.move(-100,10)
#    fenetre.blit(perso, position_perso)
#    pygame.display.flip()
#    pygame.time.delay(1000)

import pygame, sys
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(50)

fenetre = pygame.display.set_mode((640, 480))

perso = pygame.image.load("perso.png").convert_alpha()

position_perso = perso.get_rect()

pas_deplacement = 15 

while True :

    for event in pygame.event.get() :    
        if event.type == KEYDOWN:

            if event.key == K_DOWN : 
                position_perso = position_perso.move(0,pas_deplacement)

            if event.key == K_UP :
                position_perso = position_perso.move(0,-pas_deplacement)

            if event.key == K_RIGHT : 
                position_perso = position_perso.move(pas_deplacement,0)

            if event.key == K_LEFT : 
                position_perso = position_perso.move(-pas_deplacement,0)   

    fenetre.fill([10,186,181])
    fenetre.blit(perso, position_perso)
    pygame.display.flip()

