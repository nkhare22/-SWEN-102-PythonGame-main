import sys
import pygame
from pygame.locals import *

def main():

    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    bullets = []
    aliens = []

    background = pygame.image.load("Aliens/bg.jpeg").convert()
    ship = pygame.image.load("Aliens/UserIcon.png").convert_alpha()
    ship = pygame.transform.scale(ship, (64, 64))
    bulletpicture = pygame.image.load("Aliens/bullet.png").convert_alpha()
    alienpicture = pygame.image.load("Aliens/alien.png").convert_alpha()
    alienpicture = pygame.transform.scale(alienpicture, (40, 40))

    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            elif event.type == MOUSEBUTTONDOWN:
                bullets.append([500, event.pos[0]])

            elif event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()

        clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        posY = 10
        for a in range(3):
            posX = 200
            for b in range(8):
                aliens.append([posY, posX])
                posX += 50
            posY += 50

        for b in range(len(bullets)):
            bullets[b][0] -= 10

        # Iterate over a slice copy if you want to mutate a list.
        for bullet in bullets[:]:
            if bullet[0] < 0:
                bullets.remove(bullet)

        screen.blit(background, (0, 0))

        for bullet in bullets:
            screen.blit(bulletpicture, pygame.Rect(bullet[1], bullet[0], 0, 0))
        for alien in aliens:
            screen.blit(alienpicture, pygame.Rect(alien[1], alien[0], 0, 0))

        screen.blit(ship, (mx - 32, 500))
        pygame.display.flip()

if __name__ == '__main__':
    main()