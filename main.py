import pygame

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    Rect,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/lil_guy.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2) # 2 instead of 1 to counteract the gravity mechanic
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

all_sprites = pygame.sprite.Group()

running = True

while running:
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == QUIT:
            running = False
            
    pressed_keys = pygame.key.get_pressed() # makes a dictionary of all the keys that are currently pressed down

    if player.rect.bottomright[1] < SCREEN_HEIGHT / 2 or 400 < player.rect.bottomright[0] < 500 : # basic gravity, checks that the y coordinate is above a certain level, and causes the sprite to fall down if true
        player.rect.move_ip(0, 1)

    if player.rect.bottomright[1] > SCREEN_HEIGHT / 2: # if the player is in the hole, it can't move past the walls of the hole
        if player.rect.bottomleft[0] < 403:
            if pressed_keys[K_LEFT]:
                player.rect.move_ip(2, 0)
        elif 497 < player.rect.bottomright[0]:
            if pressed_keys[K_RIGHT]:
                player.rect.move_ip(-2, 0)

    if player.rect.bottomright[1] > SCREEN_HEIGHT:
        running = False

    player.update(pressed_keys) # move the sprite based on what keys are pressed

    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    pygame.draw.rect(screen, "green", Rect(0, SCREEN_HEIGHT / 2, 400, SCREEN_HEIGHT / 2))
    pygame.draw.rect(screen, "green", Rect(500, SCREEN_HEIGHT / 2, 300, SCREEN_HEIGHT / 2))

    

    pygame.display.flip() # refreshes the display every frame