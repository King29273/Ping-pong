
import pygame
pygame.init()
from random import randint
from time import time
window = pygame.display.set_mode((700,500))
 
back =  pygame.image.load("galaxy.jpg")
back = pygame.transform.scale(back,(700,500))
FPS = 60
red = (255, 0,50)

clock = pygame.time.Clock()


class Area:
    def __init__(self,x,y,w,h,image):
        self.rect = pygame.Rect(x ,y, w, h)
        image = pygame.transform.scale(image,(w,h))
        self.image = image
    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
class Player(Area):
    def __init__(self,x,y,w,h,image):
        super().__init__(x,y,w,h,image)
    def move(self,Left,Right):
        k = pygame.key.get_pressed()
        if k [Down]:
            if self.rect.y < 475:
                self.rect.y += 2
        if k [Up]:
            if self.rect.y > 5:
                self.rect.y -= 2

        
    def update_score(player):
        global PLAYER_1_SCORE, PLAYER_2_SCORE
        if player == "right":
            PLAYER_1_SCORE += 1
        else:
            PLAYER_2_SCORE += 1

class Ball(Area):
    def move(self):
        pass


platform_pict = pygame.image.load("platform90.png")
player1 = Player(50,200,25,100,platform_pict)
player2 = Player(650,200,25,100,platform_pict)
#platform.paint_pict()

ball_pict = pygame.image.load("1.png")
ball = Ball(220,250,50,50,ball_pict)
step_x = 1
font2 = pygame.font.Font(None,50)
you_lose = font2.render("Ти програв!",True,(0,0,0))
step_y = 1
game = True
while game:
    window.blit(back,(0,0))
    player1.update()
    player1.move(pygame.K_d,pygame.K_a)
    player2.update()
    player2.move(pygame.K_RIGHT,pygame.K_LEFT)
    ball.update()
    ball.move()


    if ball.rect.x >=650:
        game = False
    elif ball.rect.x <= 50:
        game = False
    if ball.rect.colliderect(player2.rect):
        step_y *= -1
    if ball.rect.colliderect(player1.rect):
        step_y *= -1
    if ball.rect.y <= 0:
        step_y *= -1
    ball.rect.x += step_x
    ball.rect.y += step_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)