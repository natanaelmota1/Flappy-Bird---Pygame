import pygame
from random import randrange
import os
from datetime import datetime

# teste de execução do jogo
try:
    pygame.init()
except:
    print('O módulo pygame não foi inicializado com sucesso')

# parâmetros da tela
largura = 288
altura = 512
today = datetime.now()
day = today.day
month = today.month
year = today.year

# interface
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('FLAPPY BIRD')
relogio = pygame.time.Clock()
background_day = pygame.image.load("sprites/background-day.png").convert()
background_night = pygame.image.load("sprites/background-night.png").convert()
sair = True

while(sair):
    
    # escolha do background
    if (today.hour < 18):
        screen.blit(background_day, (0,0))
    else:
        screen.blit(background_night, (0,0))
    pygame.display.update()
    
    # condição de fechamento do jogo
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sair = False