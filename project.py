import pygame
pygame.init()
 
win = pygame.display.set_mode((1000,700),pygame.RESIZABLE)

pygame.display.set_caption("Game")

walkRight = [pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'),pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'),pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png')]
walkLeft = [pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'),pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png'),pygame.image.load('b1.png'), pygame.image.load('b2.png'), pygame.image.load('b3.png')]
bg = pygame.image.load('bg2.jpg').convert()
char = pygame.image.load('s1.png')

for i in range(len(walkRight)):
    walkRight[i] = pygame.transform.scale(walkRight[i],(100,100))
for j in range(len(walkLeft)):
    walkLeft[j] = pygame.transform.scale(walkLeft[j],(100,100))
    
char = pygame.transform.scale(char,(100,100))
bg = pygame.transform.scale(bg,(1000,700))
jump=pygame.image.load('j1.png')
jump=pygame.transform.scale(jump,(150,150))




clock = pygame.time.Clock()


screenwidth = 1000

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
        self.vel = 25
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

run=True
t=0
def redrawgamewindow():
    global walkcount
    man.draw(win)
    for bullet in bullets:
            bullet.draw(win)
    pygame.display.update()


man = player(200,500,64,64)
bullets = []
while run:
    clock=pygame.time.Clock()
    clock.tick(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
    for bullet in bullets:
        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2),round(man.y + man.height //2),6,(0,0,0)))
    
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
    x1=1000+t
    win.blit(bg,(t,0))
    win.blit(bg,(x1,0))
    t-=7
    if t<-1000:
        t=0
    

    redrawgamewindow()
pygame.quit()
