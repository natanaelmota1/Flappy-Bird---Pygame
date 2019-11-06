import pygame
import random
import os
from datetime import datetime

# teste de execução do jogo
try:
    pygame.init()
except:
    print('O módulo pygame não foi inicializado com sucesso')

# parâmetros da tela
width = 288
height = 512
today = datetime.now()
day = today.day
month = today.month
year = today.year

# interface
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('FLAPPY BIRD')
FPS = pygame.time.Clock()
background_day = pygame.image.load("sprites/background-day.png").convert()
background_night = pygame.image.load("sprites/background-night.png").convert()
exit = True
count_updates = 0

# parâmetros pássaro
bird_x = 288/2
bird_y = 512/2
bird_sprite = 1
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
    ),
)
# selecionando pássarinho aleatório
rand_bird = random.randint(0,2)
bird = (
    pygame.image.load(tuple_birds[rand_bird][0]).convert_alpha(),
    pygame.image.load(tuple_birds[rand_bird][1]).convert_alpha(),
    pygame.image.load(tuple_birds[rand_bird][2]).convert_alpha(),
)

while(exit):
    
    # escolha do background
    if (today.hour < 18):
        screen.blit(background_day, (0,0))
    else:
        screen.blit(background_night, (0,0))

    # animação passarinho
    count_updates += 1
    if (count_updates % 2 == 0):
        bird_sprite = 1
    elif (count_updates % 3 == 0):
        bird_sprite = 2
    else:
        bird_sprite = 0
    bird_y += 1.5
    bird_player = screen.blit(bird[bird_sprite], (bird_x, bird_y))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                bird_y -= 10

    # condição de fechamento do jogo
        if (event.type == pygame.QUIT):
            exit = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                exit = False
    
    pygame.display.update()
    FPS.tick(20)