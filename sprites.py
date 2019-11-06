import pygame
# Sprites do pássaro
tuple_birds = (
    # passarinho vermelho
    (
        'sprites/redbird-upflap.png',
        'sprites/redbird-midflap.png',
        'sprites/redbird-downflap.png',
    ),
    # passarinho azul
    (
        'sprites/bluebird-upflap.png',
        'sprites/bluebird-midflap.png',
        'sprites/bluebird-downflap.png',
    ),
    # passarinho amarelo
    (
        'sprites/yellowbird-upflap.png',
        'sprites/yellowbird-midflap.png',
        'sprites/yellowbird-downflap.png',
    )
)
# Sprites do background
def base_generator(screen, sub_floor):
    floor1_x = 288 - sub_floor
    floor2_x = 0 - sub_floor
    base_sprite = pygame.image.load("sprites/base.png").convert()
    screen.blit(base_sprite, (floor1_x,400))
    screen.blit(base_sprite, (floor2_x,400))

