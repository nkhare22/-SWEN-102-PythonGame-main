import pygame
import random
import time
import sys

# Launches pygame 'SWEN Snake'
pygame.init()

# Color variables
background_color = pygame.Color(76, 70, 50)
red = pygame.Color(255, 0, 0)
light_green = pygame.Color(98, 205, 114)
yellow = pygame.Color(255, 255, 0)
light_yellow = pygame.Color(255, 255, 153)
black = pygame.Color(0, 0, 0)

# Window settings (480 x 480)
pygame_window = pygame.display.set_mode((480, 480))
pygame.display.set_caption('Pitfall Game')

# Default game parameters
points = 0
player = [240, 240]
mine = [[]]
movement = 'STAND BY'
movement_filter = movement
rng = random.randint(10, 470)
rng_2 = random.randint(10, 470)
mine_location = [round(rng, -1), round(rng_2, -1)]
mine_on_screen = True


def help_display():
    help_menu = True
    selected = ""
    while help_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    help_menu = False
                    main_menu()
                    print("Menu")

            else:

                pygame_window.fill(background_color)
                font = pygame.font.SysFont('impact', 20)
                fonttwo = pygame.font.SysFont('impact', 60)


                text_escape = font.render('Escape', True, yellow)
                pygame_window.blit(text_escape, (0, 0))

                text_help_one = font.render('To move the player in the direction you want, you must ', True,
                                            light_yellow)
                pygame_window.blit(text_help_one, (0, 50))

                text_help_two = font.render('control them using the arrow keys.', True, light_yellow)
                pygame_window.blit(text_help_two, (0, 75))

                text_help_three = font.render('Green plots will randomly appear on the screen, one at a.', True,
                                              light_yellow)
                pygame_window.blit(text_help_three, (0, 100))

                text_help_three_pt2 = font.render('time.', True,
                                              light_yellow)
                pygame_window.blit(text_help_three_pt2, (0, 125))

                text_help_four = font.render('Your goal is to move over as many as possible to increase ', True,
                                             light_yellow)
                pygame_window.blit(text_help_four, (0, 150))

                text_help_five = font.render('your score. As you move over the points they will turn red.', True,
                                             light_yellow)
                pygame_window.blit(text_help_five, (0, 175))

                text_help_six = font.render('If you walk over the red points again, then its game over.', True,
                                            light_yellow)
                pygame_window.blit(text_help_six, (0, 200))

                text_help_six = font.render('Find a way to avoid them all, be sure to use the border!.', True,
                                            light_yellow)
                pygame_window.blit(text_help_six, (0, 225))

                text_help_seven = font.render('When the game begins the player will be still. The game', True,
                                            light_yellow)
                pygame_window.blit(text_help_seven, (0, 250))

                text_help_eight = font.render('will being once your press an arrow key ', True,
                                              light_yellow)
                pygame_window.blit(text_help_eight, (0, 275))

                text_help_seven = fonttwo.render('Good luck', True,
                                              light_yellow)
                pygame_window.blit(text_help_seven, (120, 360))

                pygame.display.update()
                (pygame.time.Clock()).tick(15)


def main_menu():
    font = pygame.font.SysFont('impact', 60)
    fonttwo = pygame.font.SysFont('impact', 30)
    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "help"
                elif event.key == pygame.K_ESCAPE:
                    selected = "escape"
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        menu = False
                        print("Start")
                    if selected == "help":
                        print("Help")
                        menu = False
                        help_display()
                    if selected == "escape":
                        pygame.quit()
                        quit()
        pygame_window.fill(background_color)
        title = font.render('Pitfall', True, light_yellow)

        if selected == "start":
            text_start = font.render('Start', True, yellow)
        else:
            text_start = font.render('Start', True, light_yellow)
        if selected == "help":
            text_help = font.render('Help', True, yellow)
        else:
            text_help = font.render('Help', True, light_yellow)
        text_escape = fonttwo.render('Escape', True, light_yellow)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        help_rect = text_help.get_rect()
        quit_escape = text_escape.get_rect()

        # Main Menu Text
        pygame_window.blit(title, (480 / 2 - (title_rect[2] / 2), 80))
        pygame_window.blit(text_start, (480 / 2 - (start_rect[2] / 2), 300))
        pygame_window.blit(text_help, (480 / 2 - (start_rect[2] / 2), 360))
        pygame_window.blit(text_escape, (0, 0))
        pygame.display.update()
        (pygame.time.Clock()).tick(15)


main_menu()


# End Game Parameters
def end_game():
    font = pygame.font.SysFont('impact', 60)
    font_output = font.render('Game Over', True, yellow)
    font_position = font_output.get_rect()
    font_position.midtop = (240, 160)
    pygame_window.fill(background_color)
    pygame_window.blit(font_output, font_position)
    points_position.midtop = (240, 240)
    pygame_window.blit(font_points_output, points_position)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


# Minigame Snake
while True:
    # To Force close the game
    for user_input in pygame.event.get():
        if user_input.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # User input
        if user_input.type == pygame.KEYDOWN:
            if user_input.key == pygame.K_UP:
                movement_filter = 'Y+'
            if user_input.key == pygame.K_DOWN:
                movement_filter = 'Y-'
            if user_input.key == pygame.K_LEFT:
                movement_filter = 'X-'
            if user_input.key == pygame.K_RIGHT:
                movement_filter = 'X+'

    # Prevents movement collision on the same axis
    if movement_filter == 'Y+' and movement != 'Y-':
        movement = 'Y+'
    if movement_filter == 'Y-' and movement != 'Y+':
        movement = 'Y-'
    if movement_filter == 'X+' and movement != 'X-':
        movement = 'X+'
    if movement_filter == 'X-' and movement != 'X+':
        movement = 'X-'

    # Movements on the X/ Y plane

    if movement == 'Y+':
        player[1] -= 10
    if movement == 'X-':
        player[0] -= 10
    if movement == 'Y-':
        player[1] += 10
    if movement == 'X+':
        player[0] += 10


    # Increases trail length

    mine.insert(0, list(player))

    if player[0] == mine_location[0] and player[1] == mine_location[1]:
        points += 1
        mine_on_screen = False
    else:
        mine.pop(1)

    # Changes food position

    if mine_on_screen == False:
        rng = random.randint(10, 470)
        rng_2 = random.randint(10, 470)
        mine_location = [round(rng, -1), round(rng_2, -1)]
    mine_on_screen = True

    # Refreshes Screen
    pygame_window.fill(background_color)
    for length in mine:
        if length == player:
            pygame.draw.rect(pygame_window, yellow, pygame.Rect(length[0], length[1], 10, 10))
        else:
            pygame.draw.rect(pygame_window, red, pygame.Rect(length[0], length[1], 10, 10))

    # Draws food
    pygame.draw.rect(pygame_window, light_green, pygame.Rect(mine_location[0], mine_location[1], 10, 10))

    # Border and Body Collision
    '''
    if player[0] < 0 or player[0] > 470 or player[1] < 0 or player[1] > 470:
        end_game()
    '''
    if player[0] < 0:
        player[0] = 470
    if player[0] > 480:
        player[0] = 10
    if player[1] < 0:
        player[1] = 470
    if player[1] > 480:
        player[1] = 10


    # Touching the snake body
    for block in mine[1:]:
        if player[0] == block[0] and player[1] == block[1]:
            end_game()

    font_points = pygame.font.SysFont('impact', 30)
    font_points_output = font_points.render('Points : ' + str(points), True, yellow)
    points_position = font_points_output.get_rect()
    points_position.midtop = (240, 20)
    pygame_window.blit(font_points_output, points_position)

    pygame.display.update()

    (pygame.time.Clock()).tick(15)
