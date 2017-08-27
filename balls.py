import pygame
import random
from pygame.locals import*
pygame.init()
kapeesh=1080
aarush=720
krishna=pygame.display.set_mode((kapeesh,aarush))
pygame.display.set_caption("crazy mind")
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
grt=(0,255,255)
fb=(255,155,0)
cd=(155,60,90)
pd=(210,0,155)
FPS=600
fpsclock=pygame.time.Clock()
def gameLoop2():
    gameExit2=False
    smallfont=pygame.font.SysFont("comicsansms",25)
    def page_1(msg1,color1,msg2,color2,msg3,color3):
        txt1=smallfont.render(msg1,True,color1)
        txt2=smallfont.render(msg2,True,color2)
        txt3=smallfont.render(msg3,True,color3)
        krishna.blit(txt1,[400,0])
        krishna.blit(txt2,[100,200])
        krishna.blit(txt3,[400,300])
    while not gameExit2:
        krishna.fill(white)
        page_1("WELCOME TO THE CRAZY MIND",red,"TRY TO COLLECT AS MANY BALLS YOU CAN",blue,"PRESS S TO PLAY GAME",grt)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_s:
                    gameLoop1()
    
def gameLoop1():
    points=0
    jgimg=pygame.image.load("jg.png")
    pygame.mixer.music.load("kp5.mp3")
    jgx=100
    jgy=600
    ct=0
    x_change=0
    y_change=0
    x1=540
    y1=-80
    x2=200
    y2=20
    x3=240
    y3=10
    x4=140
    y4=-50
    x5=180
    y5=5
    x6=200
    y6=-100
    x7=300
    y7=15
    x8=350
    y8=-60
    gameExit1=False
    gameOver1=False
    smallfont=pygame.font.SysFont("comicsansms",25)
    def msg_to_screen(msg1,color1,msg2,color2):
        text1=smallfont.render(msg1,True,color1)
        text4=smallfont.render(msg2,True,color2)
        krishna.blit(text4,[400,0])
        krishna.blit(text1,[400,300])
    def score(score):
        text2=smallfont.render("Your Score: "+str(points),True,white)
        text3=smallfont.render("timeleft: "+str(4000-ct),True,white)
        krishna.blit(text2,[0,0])
        krishna.blit(text3,[0,50])                       
    def bbl_1(color,x,y,r):
        pygame.draw.circle(krishna,color,(x,y),r)
        pygame.display.update()
        fpsclock.tick(FPS)
    pygame.mixer.music.play(-1,0.0)
    while not gameExit1:
        while gameOver1==True:
            krishna.fill(white)
            msg_to_screen("game Over,press S to play again AND press Q to quit",red,"Your Score: "+str(points),blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit1=True
                        gameOver1=False
                    if event.key==pygame.K_s:
                        gameLoop1()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit1=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-10
                    y_change=0
                        
                elif event.key==pygame.K_RIGHT:
                    x_change=10
                    y_change=0
                elif event.key==pygame.K_UP:
                    y_change=-10
                    x_change=0
                elif event.key==pygame.K_DOWN:
                    y_change=10
                    x_change=0
            if event.type==pygame.KEYUP:
                x_change=0
                y_change=0
        x=jgx
        y=jgy            
        jgx+=x_change
        jgy+=y_change
            
        score(points)
        if jgx>=1007 or jgx<=0:
            jgx=x
        if jgy>=622 or jgy<=0:
            jgy=y
        krishna.fill(black)
        score(points)
        krishna.blit(jgimg,(jgx,jgy))
        pygame.display.update()
        
        if y1!=710:
            bbl_1(fb,x1,y1,10)
            y1=y1+5
            if jgx<=x1-10 and jgx+73>=x1+10 and jgy+36>=y1+10 and jgy<=y1+10:
                points+=2
                score(points)     
                x1=100+random.randrange(0,800)
                y1=-80
        else:
            x1=100+random.randrange(0,800)
            y1=-80
        if y2!=710:
            bbl_1(green,x2,y2,10)
            y2=y2+5
            if jgx<=x2-10 and jgx+73>=x2+10 and jgy+36>=y2+10 and jgy<=y2+10:
                points+=5
                score(points)     
                x2=100+random.randrange(0,900)
                y2=20
        else:
            x2=100+random.randrange(0,900)
            y2=20
        if y3!=710:
            bbl_1(red,x3,y3,10)
            y3=y3+5
            if jgx<=x3-10 and jgx+73>=x3+10 and jgy+36>=y3+10 and jgy<=y3+10:
                points+=15
                score(points)
                x3=100+random.randrange(0,800)
                y3=10
        else:
            x3=100+random.randrange(0,800)
            y3=10
        if y4!=710:
            bbl_1(white,x4,y4,10)
            y4=y4+5
            if jgx<=x4-10 and jgx+73>=x4+10 and jgy+36>=y4+10 and jgy<=y4+10:
                points+=10
                score(points)
                x4=100+random.randrange(0,800)
                y4=-50
        else:
            x4=100+random.randrange(0,800)
            y4=-50
        if y5!=710:
            bbl_1(pd,x5,y5,10)
            y5=y5+5
            if jgx<=x5-10 and jgx+73>=x5+10 and jgy+36>=y5+10 and jgy<=y5+10:
                points+=2
                score(points)
                x5=100+random.randrange(0,800)
                y5=5
        else:
            x5=100+random.randrange(0,800)
            y5=5
        if y6!=710:
            bbl_1(green,x6,y6,10)
            y6=y6+5
            if jgx<=x6-10 and jgx+73>=x6+10 and jgy+36>=y6+10 and jgy<=y6+10:
                points+=5
                score(points)
                x6=100+random.randrange(0,900)
                y6=-100
        else:
            x6=100+random.randrange(0,900)
            y6=-100
        if y7!=710:
            bbl_1(red,x7,y7,10)
            y7=y7+5
            if jgx<=x7-10 and jgx+73>=x7+10 and jgy+36>=y7+10 and jgy<=y7+10:
                points+=15
                score(points)
                x7=100+random.randrange(0,900)
                y7=15
        else:
            x7=100+random.randrange(0,900)
            y7=15
        if y8!=710:
            bbl_1(grt,x8,y8,10)
            y8=y8+5
            if jgx<=x8-10 and jgx+73>=x8+10 and jgy+36>=y8+10 and jgy<=y8+10:
                points+=2
                score(points)
                x8=100+random.randrange(0,800)
                y8=-60
        else:
            x8=100+random.randrange(0,800)
            y8=-60
        ct=ct+1
        if ct>4000:
            gameOver1=True

    pygame.quit()
    quit()
gameLoop2()    
gameLoop1()    
