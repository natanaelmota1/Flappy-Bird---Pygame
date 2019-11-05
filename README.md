# Flappy Bird

Um clone do famoso jogo Flappy Bird utilizando a biblioteca python PyGame.

## Q&A

- O que é pygame?  

  pygame é uma biblioteca python de livre utilização (Open Source) que tem como função a criação de aplicativos multimidia, jogos sendo um exemplo disso; pygame é altamente portável e roda em quase todas as plataformas e sistemas operacionais.

- Como instalar e configurar o pygame?  

  A melhor maneira de se instalar o pygame é pela ferramenta pip (Ferramenta que o python usa para instalar pacotes). 

  Para isso, usamos o comando abaixo:
  ```
  python3 -m pip install -U pygame --user
  ```

  Para testar se foi instalado, rodamos o seguinte exemplo:  
  ```
  python3 -m pygame.examples.aliens
  ```
- Como fazer animações com sprites usando o pygame?  

  Ao adicionar um jogador como mostrado abaixo, é simples adicionar os sprites após essa parte do código associando a nomenclatura.
  ```python
  # Definir um jogador fazendo uma classe com um def
  # O jogador será mostrado na superfície escrita na tela
  class Player(pygame.sprite.Sprite):
      def __init__(self):
          super(Player, self).__init__()
          self.surf = pygame.Surface((75, 25))
          self.surf.fill((255, 255, 255))
          self.rect = self.surf.get_rect()
  ```


## Contributors

- Antônio Diego Furtado da Silva: https://github.com/D1380M4nfr3
- Bruno França do Prado: https://github.com/BrunoThe13th
- Lucas Monte Ciriaco: https://github.com/lmc2631
- Max Barros de Sales: https://github.com/maxbarros
- Natanael da Mota Figueira: https://github.com/natanaelmota1

## Assets

- Sprites and songs:

    https://www.spriters-resource.com/mobile/flappybird/sheet/59894/

    https://github.com/sourabhv/FlapPyBird/tree/master/assets

## License

  [MIT License](https://github.com/natanaelmota1/Flappy-Bird---Pygame/blob/master/LICENSE.txt)

