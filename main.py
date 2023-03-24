import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
vec = pygame.math.Vector2
font = pygame.font.Font('freesansbold.ttf', 25)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

colList = [(249,38,114), (61,209,119), (255,201,0),(174, 129, 255), (255,63,128), (0,176,255), (254,254,254)]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((46, 42, 46))


class Paddle(pygame.sprite.Sprite):
    def __init__(self, player_side):
        super(Paddle, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH/40, SCREEN_HEIGHT/10))
        self.surf.fill(colList[-1])
        self.rect = self.surf.get_rect()
        self.side = player_side
        self.score = 0
        if(self.side == 'right'):
        	self.rect.x = SCREEN_WIDTH - 15
        else:
            self.rect.x = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and self.side == 'right':
            self.rect.y += 7
        if keys[pygame.K_UP] and self.side == 'right':
            self.rect.y -= 7
        if keys[pygame.K_s] and self.side == 'left':
            self.rect.y += 7
        if keys[pygame.K_w] and self.side == 'left':
            self.rect.y -= 7

    def point_score(self):
        self.score += 1

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH/25, SCREEN_HEIGHT/25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.surf_center = ((SCREEN_WIDTH - self.surf.get_width())/2, (SCREEN_HEIGHT - self.surf.get_height())/2)
        self.vel = vec(5, random.randrange(-5,5))

    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
        self.bounce()
        self.keep_on_screen()
        
    def keep_on_screen(self):
        if self.rect.left < 0:
            self.rect.left = 0
            P2.point_score()
            self.rect.x = 200
            self.rect.y = 200
            self.vel.x = self.vel.x * - 1
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            P1.point_score()
            self.rect.x = 200
            self.rect.y = 200
            self.vel.x = self.vel.x * - 1
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vel.y = self.vel.y * - 1
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel.y = self.vel.y * - 1
    
    def bounce(self):
        paddleList = [P1.rect, P2.rect]
        velList = [-5,-4,-3,3,4,5]
        if(not pygame.Rect.collidelist(self.rect, paddleList) == -1):
            self.vel.x = self.vel.x * - 1
            self.vel.y = velList[random.randrange(len(velList))]



ball = Ball()
P1 = Paddle('right')
P2 = Paddle('left')

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)
all_sprites.add(ball)



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((46, 42, 46))

    P1.update()
    P2.update()
    ball.update()


    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)


    P1Score = font.render(str(P1.score), True, colList[-1])
    P2Score = font.render(str(P2.score), True, colList[-1])
    screen.blit(P1Score, (SCREEN_WIDTH/3, SCREEN_HEIGHT * 0.05))
    screen.blit(P2Score, (SCREEN_WIDTH * 2/ 3, SCREEN_HEIGHT * 0.05))

    pygame.display.flip()
    
    clock.tick(30)

pygame.quit()
