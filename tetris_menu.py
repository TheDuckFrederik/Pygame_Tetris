#
import time, pygame, random, sys
#
HEIGHT, WIDTH = 640, 480
BACKGROUND_IMAGE = 'assets/background/menu_background_1.png'
credit = ''
#
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
#
def print_screen_backround(image):
    backround = pygame.image.load(image).convert()
    screen.blit(backround, (0, 0))
#
def credit_animation():
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
        screen.blit(img, (20, 200 - i))
        #
        pygame.display.update()
    #
time.sleep(0.7)
#
for n in range(8):
    credit = 'Sprites per:'
    credit_animation()
    #
    credit = 'Unai O. Pujol'
    credit_animation()
    #
    credit = 'Codi per:'
    credit_animation()
    #
    credit = 'Unai O. Pujol:'
    credit_animation()
    #
    credit = 'Musica per:'
    credit_animation()
    #
    credit = 'Unai O. Pujol'
    credit_animation()
    #
    credit = 'El millor profe del mon:'
    credit_animation()
    #
    credit = 'Xavi Sancho'
    credit_animation()
    #
#

