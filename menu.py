import pygame

import SpaceInvaders
import TicTacToe
import connectFour
import Snake

# Start pygame
pygame.init()
# Font options
largeText = pygame.font.Font('freesansbold.ttf', 45)
medText = pygame.font.Font('freesansbold.ttf', 40)
smallText = pygame.font.Font('freesansbold.ttf', 25)


# Creates a rectangular button for us
def creating_buttons_rect(screen, font, words, pos_x, pos_y, width, height, fontColor, buttonColor, border, border_corners):
    text = font.render(words, True, fontColor)
    textRect = pygame.draw.rect(screen, buttonColor, (pos_x, pos_y, width, height), border, border_corners)
    font_rect = text.get_rect()
    font_rect.center = textRect.center
    return text, font_rect


# Check to see if were hovering over a button
def isHovering(rect, pos):
    if pos[0] > rect.left and pos[0] < rect.left + rect.width:
        if pos[1] > rect.top and pos[1] < rect.top + rect.height:
            return True
    return False


def main_menu():
    # Color options
    GREY = (96, 96, 96)
    BRIGHT_BLUE = (0, 78, 255)
    NAVY_BLUE = (0, 0, 205)
    SNAKE_GREEN = (47, 111, 55)
    SKY_BLUE = (0, 191, 255)
    LIGHT_BLUE = (0, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BRICK_RED = (178, 34, 34)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    LIME = (0, 255, 0)

    color1 = BRICK_RED
    color2 = SKY_BLUE
    color3 = SNAKE_GREEN
    color4 = NAVY_BLUE
    color6 = WHITE

    exit = False
    width0 = 160
    height0 = 60
    while not exit:
        screen = pygame.display.set_mode((650, 525))
        pygame.display.set_caption('Welcome')
        screen.fill(BLACK)
        # pygame.draw.rect(screen, LIME, (45, 24, 535, 92))
        heading, heading_rect = creating_buttons_rect(screen, largeText, "Minigame Collection", 65, 30, 2100 // 4, 80,
                                                      WHITE, BLACK, 0, 0)

        text = smallText.render('Pick A Game', True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (322, 160)
        pygame.draw.line(screen, WHITE, (225, 180), (415, 180), 4)

        text2, font_rect1 = creating_buttons_rect(screen, smallText, "Connect 4", 125, 215, width0, height0, YELLOW, color1,
                                                  8, 3)
        text3, font_rect2 = creating_buttons_rect(screen, smallText, "Tic Tac Toe", 125, 305, width0, height0, GREY,
                                                  color2, 8, 3)
        text4, font_rect3 = creating_buttons_rect(screen, smallText, "Snake", 370, 215, width0, height0, YELLOW, color3,
                                                  8, 3)
        text5, font_rect4 = creating_buttons_rect(screen, smallText, "A.I.", 370, 305, width0, height0, GREY,
                                                  color4, 8, 3)
        text6, font_rect5 = creating_buttons_rect(screen, smallText, "QUIT", 485, 425, 125, height0, WHITE,
                                                  color6, 8, 3)
        # render objects onto screens.
        screen.blit(heading, heading_rect)
        screen.blit(text, textRect)
        screen.blit(text2, font_rect1)
        screen.blit(text3, font_rect2)
        screen.blit(text4, font_rect3)
        screen.blit(text5, font_rect4)
        screen.blit(text6, font_rect5)
        pygame.display.update()
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                exit = True
                pygame.quit()
                quit()
            # checks if mouse is hovering over button and if so will highlight button
            if ev.type == pygame.MOUSEMOTION:
                if isHovering(font_rect1, pos):
                    # Connect 4
                    color1 = RED
                    pygame.display.update()
                else:
                    color1 = BRICK_RED
                    pygame.display.update()
                if isHovering(font_rect2, pos):
                    # Tic Tac Toe
                    color2 = LIGHT_BLUE
                    pygame.display.update()
                else:
                    color2 = SKY_BLUE
                    pygame.display.update()
                if isHovering(font_rect3, pos):
                    # Snake
                    color3 = LIME
                    pygame.display.update()
                else:
                    color3 = SNAKE_GREEN
                    pygame.display.update()
                if isHovering(font_rect4, pos):
                    # Alien Invaders
                    color4 = BRIGHT_BLUE
                    pygame.display.update()
                else:
                    color4 = NAVY_BLUE
                    pygame.display.update()
                if isHovering(font_rect5, pos):
                    color6 = GREY
                    pygame.display.update()
                else:
                    color6 = WHITE
                    pygame.display.update()
            # checks if button is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if isHovering(font_rect1, pos):
                    # Opens Connect 4
                    connectFour.main()
                if isHovering(font_rect2, pos):
                    # Opens TicTacToe
                    TicTacToe.main()
                if isHovering(font_rect3, pos):
                    # Opens Snake
                    Snake.main()
                if isHovering(font_rect4, pos):
                    # Opens Alien Invaders
                    SpaceInvaders.main()
                if isHovering(font_rect5, pos):
                    # Ends program
                    exit = True
                    pygame.quit()
                    quit()


if __name__ == '__main__':
    main_menu()


