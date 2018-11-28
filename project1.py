import pygame
import time
import random
pygame.init()
green=(0,200,0)
bright_green=(0,255,0)
bright_red=(255,0,0)
red=(200,0,0)

win = pygame.display.set_mode((1500,1000),pygame.RESIZABLE)

pygame.display.set_caption("STUD GAME")

walkRight = [pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'),pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'),pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png')]
walkLeft = [pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'),pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'),pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png')]
bg = pygame.image.load('bg2.jpg').convert()
char = pygame.image.load('s1.png')
bg_0=pygame.image.load('bg_1.jpeg')
bg1=pygame.transform.scale(bg_0,(1500,1000))
for i in range(len(walkRight)):
    walkRight[i] = pygame.transform.scale(walkRight[i],(100,100))
for j in range(len(walkLeft)):
    walkLeft[j] = pygame.transform.scale(walkLeft[j],(100,100))
    
char = pygame.transform.scale(char,(100,100))
bg = pygame.transform.scale(bg,(1500,1000))
jump=pygame.image.load('j1.png')
jump=pygame.transform.scale(jump,(150,150))
bulletsound = pygame.mixer.Sound('bullet.mp3')
hitsound= pygame.mixer.Sound('hit.mp3')
#music=pygame.mixer.music.load('music_1.mp3')
#pygame.mixer.music.play(-1)
#soundobj.play()
music1=pygame.mixer.Sound('music_1.mp3')

smallfont = pygame.font.SysFont("comicsansms",70)


clock = pygame.time.Clock()


screenwidth = 1500

class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.isJump = False
        self.jumpcount = 12
        self.shoot=False
        self.left = False
        self.right = True
        self.walkcount = 0
    
    def draw(self, win):
            if self.walkcount + 1 >= 18:
                self.walkcount  = 0
            if self.left:
                win.blit(walkLeft[self.walkcount // 7],(self.x,self.y))
                self.walkcount += 1
            elif self.right:
                    win.blit(walkRight[self.walkcount // 7],(self.x,self.y))
                    self.walkcount += 1
            elif self.isJump:
                win.blit(jump,(self.x,self.y))
            else:
                win.blit(char,(self.x,self.y))
            
class projectile:
    def __init__(self,x,y,radius,color):
        self.x = int(x)
        self.y = int(y)
        self.radius =  radius
        self.color = color
        self.vel = 70
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class enemy(object):
    walkright = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkleft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    for i in range(len(walkright)):
        walkright[i]=pygame.transform.scale(walkright[i],(130,130))
    for j in range(len(walkleft)):
        walkleft[j]=pygame.transform.scale(walkleft[j],(130,130))
    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        #self.path=[self.x,self.end]
        self.walkcount=0
        self.vel=-15
        self.k=0
    def draw(self,win):
        self.move()
        if self.walkcount + 1>=33:
            self.walkcount = 0

        if self.vel > 0:
            win.blit(self.walkright[self.walkcount // 3], (self.x,self.y))
            self.walkcount +=1
        if self.vel<0:
            win.blit(self.walkleft[self.walkcount // 3], (self.x,self.y))
            self.walkcount +=1

    def move(self):
         #if self.vel>0:
           # if self.x + self.vel <self.path[1]:
                self.x+=self.vel
                
            #else:
             #   self.vel = self.vel * -1
              #  self.walkcount = 0
         #else:
          #  if self.x - self.vel>self.path[0]:
           #     self.x+=self.vel
           # else:
            #    self.vel = self.vel * -1
             #   self.walkcount =0
    
class object_0:
    walkleft= [pygame.image.load('spike1.png')]
    walkleft[0]=pygame.transform.scale(walkleft[0],(64,64))
    
    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        #self.path=[self.x,self.end]
        self.walkcount=0
        self.vel=-7
        self.k=0
    def move(self):
        self.x+=self.vel

    def draw(self,win):
        self.move()
       # if self.walkcount + 1==1:
        self.walkcount = 0

       # if self.vel > 0:
        #     win.blit(self.walkright[self.walkcount // 3], (self.x,self.y))
         #    self.walkcount +=1
        if self.vel<0:
             win.blit(self.walkleft[self.walkcount // 1], (self.x,self.y))
          #   self.walkcount +=1

def redrawgamewindow():
    global walkcount
    man.draw(win)
    pygame.display.update()

    for bullet in bullets:
            bullet.draw(win)
    pygame.display.update()


man = player(400,750,64,64)
#goblin = enemy(210,480,64,64,450)
bullets = []

#enemies=[]
'''def enem():
    l=650        
    if len(enemies)>0:
        for i in enemies:
            enemies.pop(enemies.index(i))
    else:
        for j in range(10):
            enemies.append(enemy(l,730,64,64,450))
            #if l<1300:
            l+=100
            #else:
             #   l=650'''

def text_objects(text,font,color):
        textSurface = font.render(text, True,color)
        return textSurface, textSurface.get_rect()

def msg_disp(text,u,v,s,color):
    largeText=pygame.font.Font('freesansbold.ttf',s)
    TextSurf,TextRect=text_objects(text,largeText,color)
    TextRect.center=(u,v)
    win.blit(TextSurf, TextRect)
    pygame.display.update()
def score(score):
    score_text = smallfont.render("Score: "+str(score),True,(255,0,0))
    win.blit(score_text,[0,0])
    pygame.display.update()
def crash():
    if (s[0]>score2[0]):
        msg_disp("CONGRATULATIONS",750,500,115,(0,128,0))
        msg_disp("NEW HIGH SCORE = " + str(int(s[0])),700,700,115,(0,0,0))
        score2[0]=s[0]
    else:
        msg_disp("TRY AGAIN",750,500,115,(255,0,0))
        msg_disp("Score = " + str(int(s[0])),700,700,115,(0,0,0))
        msg_disp("HIGH SCORE = " + str(int(score2[0])),650,800,90,(0,0,0))
    #score(score1[0])
    sound[0]=0
    time.sleep(2)

    game_intro()

def button(msg,x,y,w,h,ic,ac,action=None):
    count=0
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if msg=="Play without sound!":
                sound[0]+=1
                action()
            else:
                action()
    else:
        pygame.draw.rect(win,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText,(0,0,0))
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)
    pygame.display.update()
def la():
    pass
#def tp():
 #   game_intro()
def _quit():
    pygame.quit()
    quit()
def inst():
    #win.fill((255,255,255))
    #button("",450,500,100,50,(255,255,255),(255,255,255),la)
    #pygame.draw.rect(win,(255,255,255),(950,500,100,50))
    msg_disp("1.Spacebar to shoot",800,850,40,(0,0,0))
    msg_disp("2.Up arrow key to jump",800,950,40,(0,0,0))
    #button("BACK",200,750,100,50,red,bright_red,tp)
    pygame.display.update()
def names():
    msg_disp("1.Kashif",1200,850,20,(0,0,0))
    msg_disp("2.Mudit",1200,900,20,(0,0,0))
    msg_disp("3.Manan",1200,950,20,(0,0,0))
    pygame.display.update()


score2=[0]
s=[0]
sound=[0]

def yo(enemies=[],objects=[]):
    if sound[0]==0:
        music=pygame.mixer.music.load('music_1.mp3')
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()
    man.right=True 
    enemies=[]
    objects=[]
   # l=1900
    #if len(enemies)>0:
     #   for i in enemies:
      #      enemies.pop(enemies.index(i))
    #else:
    
    #l=random.randint(1900,3000)
    #for j in range(1):
     #   enemies.append(enemy(l,730,64,64,450))
            #if l<1300:
        #if j==5:
         #   l=t
        #l+=100
            #else:
             #   l=650

    run=True
    f=700
    t=0 

    #score2[0]=int(s[0])
    s[0]=0
    i=10
    count=0
    l=1900
    y=l
    z=f
    #l=650
    while run:
        #music=pygame.mixer.music.load('music_1.mp3')
        #pygame.mixer.music.play(-1)
        count+=1
        if count%60==0:
            z=f
            if s[0]<20:
                f=random.randint(1900,3000)
            else:
                f=random.randint(1500,3000)

            if z!=f :
                #if f<z-200 or f>z+200 :
                    for i in range(1):
                        objects.append(object_0(f,790,64,64,450))

            y=l
                
            if s[0]<20: 
                l=random.randint(1900,3000)
            else:
                l=random.randint(1500,3000)
            if y!=l: 
                
            #else:    
                for j in range(1):
                    enemies.append(enemy(l,730,64,64,450))

        
        clock=pygame.time.Clock()
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for bullet in bullets:
            if bullet.x < 1500 and bullet.x > 0:
                bullet.x += bullet.vel
                # if bullet.x==310:
                    #    enemies.pop()
            
            else:
                bullets.pop(bullets.index(bullet))
    #if len(enemies)==0 :
     #       enemies.append(enemy(159,480,64,64,450))
    
        #enem()
        for e in enemies:
            if man.x+10<=e.x<=man.x+20 and man.isJump==False:
                man.right = False
                crash()
        '''for k in bullets:
            for i in enemies:
                if k.x>=i.x and k.y==782 :
                    enemies.pop(enemies.index(i))
                    bullets.pop(bullets.index(k))
                    if i.x<=1500:
                        s[0]+=10
                    hitsound.play()'''
        for o in objects:
            if man.x+10 <=o.x<=man.x+20 and man.isJump==False:
                man.right = False
                crash()
                
        #redrawgamewindow()
        #s = 0    
        #while(s >= 0):
        if man.right or man.isJump:
            #for i in range(100):
                s[0]+=0.1
                score(int(s[0]))
                #time.sleep(1)

                

        #pygame.display.update()
        if len(enemies)>0:
            for j in enemies:
                j.draw(win)
        if len(objects)>0:
            for k in objects:
                k.draw(win)


        #redrawgamewindow()
        #pygame.display.update()
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_SPACE]:
            if len(bullets) < 1:
                bullets.append(projectile(432,man.y+32,6,(0,0,0)))
                bulletsound.play()
        for k in bullets:
            for i in enemies:
                if k.x>=i.x and k.y==782 :
                    enemies.pop(enemies.index(i))
                    bullets.pop(bullets.index(k))
                    if i.x<=1500:
                        s[0]+=10
                    hitsound.play()
        redrawgamewindow()
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.left = False 
            man.right = True
    
        elif man.right and  man.x < screenwidth - man.width- man.vel:
            man.right = True
            man.left = False
    
        else:
            man.right= False 
            man.left = False
            man.walkcount = 0
    
        if not(man.isJump): 
                if keys[pygame.K_UP]:
                    man.isJump = True
                    man.right =False 
                    man.left = False
    
        else:
                    if man.jumpcount >= -12:
                        neg = 1
                        if man.jumpcount < 0:
                            neg = -1
                        man.y -= (man.jumpcount ** 2) * 0.5* neg
                        man.jumpcount -= 1
        
                    else:
                        man.isJump = False
                        man.right=True
                        man.jumpcount = 12
        x1=1500+t
        win.blit(bg,(t,0))
        win.blit(bg,(x1,0))
        if s[0]<=50:
            t-=15
        elif 50<s[0]<=100:
            t-=18
            for i in enemies:
                i.vel=-20
            for i in objects:
                i.vel=-17
        elif 100<s[0]<=150:
            t-=20
            for i in enemies:
                i.vel=-25
            for i in objects:
                i.vel=-20
        elif 150<s[0]<=200:
            t-=24
            for i in enemies:
                i.vel=-27
            for i in objects:
                i.vel=-24
        elif 200<s[0]<=250:
            t-=28
            for i in enemies:
                i.vel=-30
            for i in objects:
                i.vel=-27
        elif 250<s[0]<=320:
            t-=33
            for i in enemies:
                i.vel=-34
            for  i in  objects:
                i.vel=-32
        else:
            t-=40
            for i in enemies:
                i.vel=-38
            for i in objects:
                i.vel=-35


                
        if t<-1500:
            t=0
        #redrawgamewindow()
#enemies=[]
#t=0
def game_intro():
        #l=650
        #win.fill((0,255,255))
        win.blit(bg1,(0,0))
        pygame.mixer.music.stop()
        #music=pygame.mixer.music.load('music_1.mp3')
        #pygame.mixer.music.play(-1)
        #largeText = pygame.font.Font('freesansbold.ttf',40)
        #enemies=[]
        #for i in range(10):
         #   enemies.append(enemy(l,730,64,64,450))
          #  l+=100
        #enem()
        #TextSurf,TextRect = text_objects("<click right to continue>",largeText)
        #TextRect.center=(750,500)
        #win.blit(TextSurf, TextRect)
        #button("GO!",450,500,100,50,green,bright_green,yo)
        #button("Quit",950,500,100,50,red,bright_red,_quit)
        #pygame.display.update()
        msg_disp("The iron patriot",750,200,115,(255,0,0))
        
        clock.tick(15)
        intro=True
        while intro:
           # music=pygame.mixer.music.load('music_1.mp3')
            #pygame.mixer.music.play(-1)
            #music1.play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #msg_disp("The iron patriot",750,200)
            
            button("Play!",450,500,100,50,green,bright_green,yo)
            button("Play without sound!",200,750,200,50,green,bright_green,yo)

            button("Quit",950,500,100,50,red,bright_red,_quit)
            button("Instructions",700,750,150,50,(200,200,0),(255,255,0),inst)
            button("Credits",1200,750,100,50,(255,192,203),(200,160,180),names)
            #pygame.display.update()
            #button("Instructions",750,750,green,bright_green,inst)
            #msg_disp("The iron patriot",750,200)
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_RIGHT]:
             #   yo()

game_intro()
pygame.quit()

