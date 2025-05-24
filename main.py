import pygame
import pygame.mixer
from time import *
from pygame.locals import *
import random
last_direction="right"
gameoverMessage="none"
K=20
speed=0.1
v=0.5
score = 0
n=1
SCREEN_X=1500
Screen_Y=500
X=[]
Y=[]
p=70
p0=1
q0=1
q=20
pause=False
gameWindowcolor=(0, 225, 0)
messageColor=(0,0,0)
scorecardColor=(0,0,255)
for i in range(n):
    X.append(i*K)
    Y.append(0)
direction="none"
food_x = random.randint(p0, p) * K
food_y = random.randint(q0, q) * K
bug_x = random.randint(p0, p) * K
bug_y = random.randint(q0, q) * K
def gameInfo():
    font=pygame.font.Font(None,23)
    font.set_italic(True)
    message=font.render("DEVELOPER: ER.NITISH BUBNA",True,messageColor)
    gameHelp1=font.render("ece ->quit | space->pause/resume",True,messageColor)
    gameHelp2 = font.render("1->volume up | 2->volume down", True, messageColor)
    gameHelp3 = font.render("3->speed up | 4->speed down", True, messageColor)
    gameWindow.blit(gameHelp1,(1200,5))
    gameWindow.blit(gameHelp2,(1200,25))
    gameWindow.blit(gameHelp3,(1200,45))
    gameWindow.blit(message,(1250,470))
def newBlock():
    gameWindow.blit(food,(food_x,food_y))
def bugblock():
    gameWindow.blit(bug,(bug_x,bug_y))
def updateBugposition():
    global bug_x,bug_y
    if bug_x==food_x and bug_y==food_y:
        bug_x = 120
        bug_y = 120
    bug_x = random.randint(p0, p) * K
    bug_y = random.randint(q0, q) * K
def directionGameover():
    global last_direction,gameoverMessage
    if (direction == "right" and last_direction == "left") or \
            (direction == "left" and last_direction == "right") or \
            (direction == "up" and last_direction == "down") or \
            (direction == "down" and last_direction == "up"):
        gameoverMessage="SNAKE REVERSED!!!  GAME OVER!!!"
        return True
def boundryGameover():
    global gameoverMessage
    if X[n - 1] < 0 or X[n - 1] > SCREEN_X-K or Y[n - 1] < 0 or Y[n - 1] > Screen_Y-K:
        gameoverMessage="SNAKE TOUCHED BOUNDRY!!!  GAME OVER!!!"
        return True
    else:
        return False
def bugGameover():
    global gameoverMessage
    if X[n-1]==bug_x and Y[n-1]==bug_y:
        gameoverMessage="VEG SNAKE TRIES TO EAT NON-VEG!!!  GAME OVER"
        return True
    else:
        return False
def tailtouchGameover():
    global gameoverMessage
    for i in range(n - 2):
        if X[n - 1] == X[i] and Y[n - 1] == Y[i]:
            gameoverMessage="SNAKE ATE ITSELF!!! GAME OVER!!!"
            return True
        else:
            return False
def gameBoundry():
    font=pygame.font.Font(None,10)
    temp=font.render("*",True,(0,0,255))
    for a in range(0,1500):
        gameWindow.blit(temp, (a, 0))
        gameWindow.blit(temp, (a, 495))
    for a in range(0,500):
        gameWindow.blit(temp, (0, a))
        gameWindow.blit(temp, (1495, a))
def eatFood():
    global n,score
    X.append(food_x)
    Y.append(food_y)
    eat_sound.set_volume(v)
    eat_sound.play()
    n+=1
    score+=1
def putFood():
    global food_x,food_y
    food_x = random.randint(p0, p) * K
    food_y = random.randint(q0, q) * K
def gameover():
    gameover_sound.set_volume(v)
    gameover_sound.play()
    font = pygame.font.Font(None, 50)
    text_surface = font.render(gameoverMessage, True, (255,0,0))
    gameWindow.blit(text_surface, (100, 250))
    pygame.display.flip()
    sleep(4)
    pygame.quit()
    exit()
def scorecard():
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Score: {score} | ", True, scorecardColor)
    gameWindow.blit(text_surface, (10, 10))
def volumeLabel():
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"volume: {v} | ", True, scorecardColor)
    gameWindow.blit(text_surface, (130, 10))
def speedLable():
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"speed: {speed}", True, scorecardColor)
    gameWindow.blit(text_surface, (290, 10))
def setXYcorinates():
    for i in range(n - 1):
        X[i] = X[i + 1]
        Y[i] = Y[i + 1]
def move():
    gameWindow.fill(gameWindowcolor)
    gameBoundry()
    gameInfo()
    scorecard()
    volumeLabel()
    speedLable()
    for i in range(n):
        if i%2!=0:
            gameWindow.blit(head, (X[i], Y[i]))
        else:
            gameWindow.blit(body, (X[i], Y[i]))
    if(boundryGameover()==True):
        gameover()
    elif(tailtouchGameover())==True:
        gameover()
    elif(directionGameover()==True):
        gameover()
    elif(bugGameover()==True):
        gameover()
    newBlock()
    bugblock()
    pygame.display.flip()
def moveRight():
    setXYcorinates()
    global food_x, food_y
    X[n-1]=X[n-1]+K
    if X[n-1]==food_x and Y[n-1]==food_y:
        eatFood()
        updateBugposition()
        putFood()
    move()
def moveLeft():
    setXYcorinates()
    global food_x, food_y
    X[n-1]=X[n-1]-K
    if X[n - 1] == food_x and Y[n - 1] == food_y:
        eatFood()
        updateBugposition()
        putFood()
    move()
def moveUp():
    global food_x, food_y
    setXYcorinates()
    Y[n-1] = Y[n-1]-K
    if X[n - 1] == food_x and Y[n - 1] == food_y:
        eatFood()
        updateBugposition()
        putFood()
    move()
def moveDown():
    global food_x,food_y
    setXYcorinates()
    Y[n-1] = Y[n-1]+K
    if X[n - 1] == food_x and Y[n - 1] == food_y:
        eatFood()
        updateBugposition()
        putFood()
    move()
pygame.init()
pygame.mixer.init()
gameWindow=pygame.display.set_mode((SCREEN_X,Screen_Y))
pygame.display.set_caption("veg SNAKE")
gameWindow.fill(gameWindowcolor)
font = pygame.font.Font(None, 50)
start_msg = font.render("HI WELCOME", True, (253,3,240))
gameWindow.blit(start_msg, (600, 250))
pygame.display.flip()
body=pygame.image.load("body.png").convert()
head=pygame.image.load("head.png").convert()
bug=pygame.image.load("bug.png").convert()
food=pygame.image.load("food.png").convert()
eat_sound=pygame.mixer.Sound("eat.wav")
gameover_sound=pygame.mixer.Sound("gameover.wav")
back_sound=pygame.mixer.Sound("backsound.mp3")
running=True
direction=last_direction
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        elif event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                running=False
            elif event.key==K_SPACE:
                pause=not pause
            elif not pause:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_RIGHT:
                    direction = "right"
                elif event.key == K_LEFT:
                    direction = "left"
                elif event.key == K_UP:
                    direction = "up"
                elif event.key == K_DOWN:
                    direction = "down"
                elif event.key==K_1:
                    v+=.1
                    v=round(v,1)
                    v=min(v,1)
                elif event.key==K_2:
                    v-=.1
                    v=max(v,0)
                    v=round(v,1)
                elif event.key==K_3:
                    speed+=.1
                    speed=round(speed,1)
                elif event.key==K_4:
                    speed-=.1
                    speed=round(speed,1)
    if not pause:
        if direction == "right":
            moveRight()
        elif direction == "left":
            moveLeft()
        elif direction == "up":
            moveUp()
        elif direction == "down":
            moveDown()
        last_direction = direction
    else:
        font = pygame.font.Font(None, 50)
        pauseMessage = font.render(("GAME paused!"), True, (0, 0, 255))
        gameWindow.blit(pauseMessage, (100, 100))
        pygame.display.flip()
    sleep(speed)