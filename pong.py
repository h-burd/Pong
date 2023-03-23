import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 64)
vec = pygame.math.Vector2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH/10, SCREEN_HEIGHT/10))
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


P1 = Player()
P2 = Player()

P2.vel.x = -2
P2.vel.y = 4


all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
# all_sprites.add(P2)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((46, 42, 46))

    for sprite in all_sprites:
    	screen.blit(sprite.surf, sprite.rect)

    text = font.render(str(P1.count), True, P1.colList[-1])
    screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT * 0.05))


    pygame.display.flip()
    P1.keep_on_screen()
    P1.update()
    # P2.keep_on_screen()
    # P2.update()
    clock.tick(30)


pygame.quit()











