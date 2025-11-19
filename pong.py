import pygame

pygame.init()

screen_width = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()


while True:
    for event in pygame.event():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()