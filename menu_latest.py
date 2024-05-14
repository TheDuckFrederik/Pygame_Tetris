#
import time
from pygame.locals import *
import pygame
import random
import sys
import numpy as np
from game_latest import main_game
from hard_mode_latest import hard_mode
#
HEIGHT, WIDTH = 640, 480
BACKGROUND_IMAGE = 'assets/background/menu_background_2.png'
END_TITLE = 'assets/background/menu_background_3.png'
credit = ''
boing = 'Xavi Sancho'
x = 0
#
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Tetris")
TETRIS = pygame.image.load('assets/peces/TETRIS/TETRIS.png')
#
def print_screen_backround(image):
    backround = pygame.image.load(image).convert()
    screen.blit(backround, (0, 0))
#
def credit_animation(credit, x):
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
def tetris_animation(x):
    print_screen_backround(END_TITLE)
    pygame.display.update()
    #
    for i in range(178):
        time.sleep(0.02)
        #
        print_screen_backround(END_TITLE)
        screen.blit(TETRIS, (x, 200 - i))
        #
        pygame.display.update()
    #
    time.sleep(0.7)
def print_menu():
    print_screen_backround(END_TITLE)
    #
    transparent_area = pygame.Surface((526, 87), pygame.SRCALPHA)
    pygame.draw.rect(transparent_area, (0, 0, 0, 200), (0, 0, 526, 87))
    #
    transparent_area2 = pygame.Surface((480, 102), pygame.SRCALPHA)
    pygame.draw.rect(transparent_area2, (0, 0, 0, 0), (0, 0, 526, 87))
    #
    screen.blit(transparent_area, (62, 377))
    screen.blit(transparent_area2, (86, 23))
    #
    font = pygame.font.SysFont(None, 36)
    img1 = font.render("1 - Play", True, (255, 255, 255))
    img2 = font.render("2 - Hard Mode", True, (255, 255, 255))
    img3 = font.render("3 - Credits", True, (255, 255, 255))
    img4 = font.render("4 - Exit", True, (255, 255, 255))
    #
    screen.blit(img1, (118, 391))
    screen.blit(img2, (118, 427))
    screen.blit(img3, (362, 391))
    screen.blit(img4, (362, 427))
    screen.blit(TETRIS, (87, 23))
    #
    pygame.display.update()
#
while True:
    # credit_animation('Jan Vilaplana', 217)
    # #
    # credit_animation('&', 315)
    #
    credit_animation('Unai O. Pujol',220)
    #
    credit_animation('presenta:', 250)
    #
    tetris_animation(87)
    #
    break
#
credit = credit
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
            main_game()
        if keys[K_2]:
            hard_mode()
        if keys[K_3]:
            credit_animation('Sprites per:', 210)
            #
            credit_animation('Jan Vilaplana', 217)
            #
            credit_animation('&', 315)
            #
            credit_animation('Unai O. Pujol', 220)
            #
            credit_animation('Codi per:', 240)
            #
            credit_animation('Unai O. Pujol', 220)
            #
            credit_animation('Musica per:', 220)
            #
            credit_animation('Unai O. Pujol', 220)
            #
            credit_animation('El millor profe del mon:', 120)
            #
            credit_animation(boing, 200)
            #
            credit_animation('Ayuda ocasional:', 170)
            #
            credit_animation('Jan Vilaplana', 217)
            #
            credit_animation('Beta testes:', 170)
            #
            credit_animation('Raquel Vargas', 217)
            #
            time.sleep(0.5)
            pygame.display.update()
        #
        if keys[K_4]:
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #
        print_menu()
    #
tetris_menu()