import pygame

pygame.init()

# Definindo tamanho da janela
x = 1280
y = 720

# Abrir janela:
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Meu jogo em Python")

# Manter a execução
executando = True

# Criando evento
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        pygame.display.update()