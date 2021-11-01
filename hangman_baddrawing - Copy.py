import pygame,sys

clock=pygame.time.Clock()

from pygame.locals import *

pygame.init()
WINDOW_SIZE= (900,600)
pygame.display.set_caption("hang")
screen=pygame.display.set_mode(WINDOW_SIZE,0,32)
color_light = (170,170,170)
color_white = (255,255,255)
hangicon=pygame.image.load("hangman.png")#1
pygame.display.set_icon(hangicon)
font=pygame.font.SysFont(None,100)
smallfont = pygame.font.SysFont('Corbel',35)
click=False
text1 = smallfont.render('PLAY' , True , (255,105,180))
text2 = smallfont.render('QUIT' , True , (255,105,180)) #and this
wrong_lst=[]
role="executioner"
key_word=""
def wrong_letters(a):
    global k
    if len(wrong_lst)>=6:
        pass
    elif a in wrong_lst:
        pass
    elif a not in wrong_lst:
     wrong_lst.append(a)

    pass
def tries(number):#7
    if number==6:
        image("lives=6.png",screen,467,216)
    if number==5:
        image("lives=5.png",screen,467,216)
    if number==4:
        image("lives=4.png",screen,467,216)
    if number==3:
        image("lives=3.png",screen,467,216)
    if number==2:
        image("lives=2.png",screen,467,216)
    if number==1:
        image("lives=1.png",screen,467,216)
    if number<=0:
        image("lives=0.png",screen,467,216)
def ending(number):#15
    end=number
    if end==1: #guesser win with more than 1 live
        image("guesser_win.png",screen,63,269)
        image("executioner_lost.png",screen,674,308)
    if end==2: #guesser win with just 1 live
        image("guesser_win2.png",screen,21,300)
        image("executioner_lost.png", screen, 674, 308)
    if end==3: #executioner win with flaws
        image("executioner_win.png",screen,674,277)
        image("guesser_lost.png",screen,61,303)
    if end==4: #executioner win with no flaws
        image("executioner_win2.png", screen, 674, 308)
        image("guesser_lost.png", screen, 61, 303)

def image(path,surface,x,y):
    load=pygame.image.load(path)
    surface.blit(load,(x,y))


def draw_text(text, font, color, surface, x, y): #i copied this
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
#that's why there r two way to print out texts, so yea:)


def main_menu():
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
    pygame.draw.rect(screen, color_light, button_1)
    pygame.draw.rect(screen, color_light, button_2)
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
    clock.tick(60)


def play():
  global key_word
  running=True
  while running:
      screen.fill((0,0,0))
      draw_text("waiting for other player...", font, (255, 255, 255), screen,20, 250)
      text_surface=smallfont.render(key_word,True,color_white)
      if role=="guesser":
          draw_text("you're the guesser",smallfont,color_white,screen, 50, 320)
          draw_text("please wait for the executioner to type in the word", smallfont, color_white, screen, 50, 370)
      if role=="executioner":
          draw_text("you're the executioner",smallfont,color_white,screen,50,320)
          draw_text("please, type the keyword:",smallfont,color_white,screen,50,370)
          screen.blit(text_surface,(420,370))
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
          if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  running = False
              if event.key== K_KP_ENTER or event.key==K_RETURN:#press enter to join the game for testing
                  hangman()
              if event.key==K_BACKSPACE:
                  key_word = key_word[:-1]
              else:
                  key_word+=event.unicode



      pygame.display.update()


def hangman():
    global key_word, wrong_lst
    state=True
    a=""
    running = True
    click=False
    game="start"
    b=a
    list_keyword=list(key_word)
    while running:
        f=183
        k=180
        lives = 6
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        button = pygame.Rect(660, 20, 210, 50)
        if button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, color_light, button)
        draw_text("EXIT", smallfont, (255, 105, 180), screen, 730, 30)
        image("board.png", screen, 155, 114)#16
        lives-=len(wrong_lst)

        tries(lives)

        if state==True and a.isalpha()==True:
            wrong_letters(a)
            state=False
        for i in wrong_lst:
                draw_text(i, smallfont, color_white, screen, k, 303)
                k += 30
        for i in range(len(list_keyword)):
            image("tile.png",screen,f,184)
            f+=40
        if game=="start":
         image("guesser.png",screen,61,303)
         image("executioner.png", screen, 674, 308)
        if game=="finish":
            ending(1)
            button_3 = pygame.Rect(20, 20, 210, 50)
            if button_3.collidepoint((mx, my)):
                if click:
                    lives = 6
                    wrong_lst = []
                    key_word = ""
                    play()
            pygame.draw.rect(screen, color_light, button_3)
            draw_text("RETRY", smallfont, (255, 105, 180), screen, 70, 20)
        if lives == 0:
                game = "finish"
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE :
                    running = False
                if event.key==K_2:
                    lives-=1
                a = event.unicode.upper()
                if a!=b:
                 b=a
                 state=True
                pass
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(10)
main_menu()


