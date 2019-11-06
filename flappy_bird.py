import pygame
import random
import os
from datetime import datetime
from sprites import *

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
sub_floor = 0

# parâmetros do pássaro
bird_x = 288/4
bird_y = 200

# selecionando pássarinho aleatório
rand_bird = random.randint(0,2)
bird = (
    pygame.image.load(tuple_birds[rand_bird][0]).convert_alpha(),
    pygame.image.load(tuple_birds[rand_bird][1]).convert_alpha(),
    pygame.image.load(tuple_birds[rand_bird][2]).convert_alpha()
)

while(exit):
    
    # escolha do background
    if (today.hour < 18):
        screen.blit(background_day, (0,0))
    else:
        screen.blit(background_night, (0,0))
    
    #gerando 
    if sub_floor >= 144:
        sub_floor = 0
    else:
        sub_floor += 1
    base_generator(screen, sub_floor)

    # animação do passarinho
    count_updates += 1
    if (count_updates % 2 == 0):
        bird_sprite = 0
    elif (count_updates % 3 == 0):
        bird_sprite = 1
    else:
        bird_sprite = 2
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