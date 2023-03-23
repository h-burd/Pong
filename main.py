import pygame
from pygame.locals import *

clock = pygame.time.Clock()
vec = pygame.math.Vector2

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
        if(self.side == 'right'):
        	self.rect.x = SCREEN_WIDTH - 15
        else:
            self.rect.x = 5
        # self.surf_center = ((SCREEN_WIDTH - self.surf.get_width())/2, (SCREEN_HEIGHT - self.surf.get_height())/2)

    def keys_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and self.side == 'right':
            self.rect.y += 5
        if keys[pygame.K_UP] and self.side == 'right':
            self.rect.y -= 5
        if keys[pygame.K_s] and self.side == 'left':
            self.rect.y += 5
        if keys[pygame.K_w] and self.side == 'left':
            self.rect.y -= 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH/20, SCREEN_HEIGHT/20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.surf_center = ((SCREEN_WIDTH - self.surf.get_width())/2, (SCREEN_HEIGHT - self.surf.get_height())/2)
        self.vel = vec(3.56, 4.33)
        self.colList = [(249,38,114), (61,209,119), (255,201,0),(174, 129, 255), (255,63,128), (0,176,255), (254,254,254)]
        self.i = 0
        self.count = 0

    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
        self.keep_on_screen()

    def keep_on_screen(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.change_vel()
            self.vel.x = self.vel.x * - 1
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.change_vel()
            self.vel.x = self.vel.x * - 1
        if self.rect.top <= 0:
            self.rect.top = 0
            self.change_vel()
            self.vel.y = self.vel.y * - 1
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.change_vel()
            self.vel.y = self.vel.y * - 1
            

    def change_vel(self):
        if self.i < len(self.colList):
            col = self.colList[self.i]
            self.i += 1
        else:
            self.i = 0
            col = self.colList[self.i]
        self.surf.fill(col)
        self.vel.y = self.vel.y * 1.01
        self.vel.x = self.vel.x * 1.01
        self.count += 1


ball = Player()
P1 = Paddle('right')
P2 = Paddle('left')

ball.vel.x = -2
ball.vel.y = 4

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

    P1.keys_move()
    P2.keys_move()

    ball.update()

    


    # print(pygame.key.get_pressed())
    # print(K_RIGHT)
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)

    # for sprite in all_sprites:
    # 	screen.blit(sprite.surf, sprite.rect)

    # text = font.render(str(P1.count), True, P1.colList[-1])
    # screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT * 0.05))

    pygame.display.flip()
    
    clock.tick(30)

pygame.quit()



