#
import time
from pygame.locals import *
import pygame
import random
import sys
#
HEIGHT, WIDTH = 640, 480
BACKGROUND_IMAGE = 'assets/background/menu_background_1.png'
credit = ''
boing = 'Xavi Sancho'
x = 0
#
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Tetris")
#
def print_screen_backround(image):
    backround = pygame.image.load(image).convert()
    screen.blit(backround, (0, 0))
#
def credit_animation(x):
    print_screen_backround(BACKGROUND_IMAGE)
    pygame.display.update()
    #
    font = pygame.font.SysFont(None, 52)
    #
    for i in range(120):
        time.sleep(0.02)
        #
        print_screen_backround(BACKGROUND_IMAGE)
        img = font.render(credit, True, (i + 50, i + i, i))
        screen.blit(img, (x, 200 - i))
        #
        pygame.display.update()
    #
    time.sleep(0.7)
#
def print_menu():
    print_screen_backround(BACKGROUND_IMAGE)
    #
    transparent_area = pygame.Surface((255, 130), pygame.SRCALPHA)
    pygame.draw.rect(transparent_area, (0, 0, 0, 100), (0, 0, 255, 130))
    #
    screen.blit(transparent_area, (210, 42))
    #
    font = pygame.font.SysFont(None, 36)
    img1 = font.render("1 - Play", True, (255, 255, 255))
    img2 = font.render("2 - Credits", True, (255, 255, 255))
    img3 = font.render("3 - Exit", True, (255, 255, 255))
    #
    screen.blit(img1, (285, 50))
    screen.blit(img2, (285, 90))
    screen.blit(img3, (285, 130))
    #
    pygame.display.update()
#
while True:
    # credit = 'Jan Vilaplana'
    # credit_animation(217)
    # #
    # credit = '&'
    # credit_animation(315)
    #
    credit = 'Unai O. Pujol'
    credit_animation(220)
    #
    credit = 'presenta:'
    credit_animation(250)
    #
    credit = 'TETRIS'
    credit_animation(260)
    #
    break
#
def tetris_menu():
    print_menu()
    #
    while True:
        #
        pygame.display.update()
        #
        keys = pygame.key.get_pressed()
        #
        if keys[K_1]:
            print('Helo')
        if keys[K_2]:
            while True:
                credit = 'Sprites per:'
                credit_animation(210)
                #
                credit = 'Jan Vilaplana'
                credit_animation(217)
                #
                credit = '&'
                credit_animation(315)
                #
                credit = 'Unai O. Pujol'
                credit_animation(220)
                #
                credit = 'Codi per:'
                credit_animation(240)
                #
                credit = 'Unai O. Pujol'
                credit_animation(220)
                #
                credit = 'Musica per:'
                credit_animation(220)
                #
                credit = 'Unai O. Pujol'
                credit_animation(220)
                #
                credit = 'El millor profe del mon:'
                credit_animation(120)
                #
                credit = boing
                credit_animation(200)
                #
                credit = 'Ayuda ocasional:'
                credit_animation(170)
                #
                credit = 'Jan Vilaplana'
                credit_animation(217)
                #
                time.sleep(0.5)
                pygame.display.update()
                #
                break
            tetris_menu()
        #
        if keys[K_3]:
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    #
tetris_menu()