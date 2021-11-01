
import pygame,sys
clock=pygame.time.Clock()
from pygame.locals import *
pygame.init()
WINDOW_SCREEN=(900,600)
screen=pygame.display.set_mode(WINDOW_SCREEN,0,32)
pygame.display.set_caption("hanghang")
colour_white=(255,255,255)
colour_gray=(170,170,170)
smallfont = pygame.font.SysFont('Corbel',35)
font=pygame.font.SysFont(None,100)
notif="im gey"
keyword="top top"

L1=pygame.image.load("lives=0.png")
L2=pygame.image.load("lives=1.png")
L3=pygame.image.load("lives=2.png")
L4=pygame.image.load("lives=3.png")
L5=pygame.image.load("lives=4.png")
L6=pygame.image.load("lives=5.png")
L7=pygame.image.load("lives=6.png")

def tries(lives):
    cmd="screen.blit(L"+str(lives)+",(600,200))"
    eval(cmd)
def mẫu():
 while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
         pygame.quit()
         sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    clock.tick(10)

def draw_text(text, font, color, surface, x, y):  # i copied this
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
def main_menu():
  click=False
  while True:
    screen.fill((0,0,0))
    #guesser: 61,303; guesser_win2: 21,300
    mx,my=pygame.mouse.get_pos()
    button_1=pygame.Rect(320,100,200,50)
    button_2 = pygame.Rect(320, 170, 200, 50)
    if button_1.collidepoint((mx,my)):
        if click:
            play()
    if button_2.collidepoint((mx,my)):
        if click:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, colour_gray, button_1)
    pygame.draw.rect(screen, colour_gray, button_2)
    draw_text("hang man", font, (255,255,255), screen,250,20)
    draw_text("PLAY",smallfont, (255,105,180), screen,380,110)
    draw_text("QUIT",smallfont, (255,105,180), screen,380,180)
    click = False
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
               click=True
    pygame.display.update()
    clock.tick(10)
def play():
    click=False #click assigned to prevent bugs
    while True:
        lives=7
        screen.fill((0, 0, 0))
        draw_text(notif, smallfont, colour_white, screen, 20, 20)
        draw_text(keyword,smallfont,colour_gray,screen,200,250)
        tries(lives)
        #exit button
        #--------------------------------------------------------------
        mx, my = pygame.mouse.get_pos()
        button = pygame.Rect(660, 20, 210, 50)
        if button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        #--------------------------------------------------------------
        pygame.draw.rect(screen, colour_gray, button)
        draw_text("EXIT", smallfont, (255, 105, 180), screen, 730, 30)
        click = False
        #click assigned to prevent bugs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(10)
main_menu()

