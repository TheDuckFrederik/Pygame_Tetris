#
import time, pygame, random, sys
#
HEIGHT, WIDTH = 640, 480
BACKGROUND_IMAGE = 'assets/background/menu_background_1.png'
credit = ''
boing = 'Alberto Vellon'
#
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
#
def print_screen_backround(image):
    backround = pygame.image.load(image).convert()
    screen.blit(backround, (0, 0))
#
x = 0
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
while True:
    credit = 'Sprites per:'
    credit_animation(210)
    #
    credit = 'Unai O. Pujol'
    credit_animation(200)
    #
    credit = 'Codi per:'
    credit_animation(240)
    #
    credit = 'Unai O. Pujol'
    credit_animation(200)
    #
    credit = 'Musica per:'
    credit_animation(220)
    #
    credit = 'Unai O. Pujol'
    credit_animation(200)
    #
    credit = 'El millor profe del mon:'
    credit_animation(120)
    #
    credit = boing
    credit_animation(200)
    #
    credit = 'Esta ayudando!!!:'
    credit_animation(170)
    #
    credit = 'Jan Vilaplana'
    credit_animation(190)
    #
    break
#

