import pygame
import random
import time
import sys

# Launches pygame 'SWEN Snake'
pygame.init()

# Color variables
background_color = pygame.Color(26, 73, 33)
mid_green = pygame.Color(51, 150, 65)
light_green = pygame.Color(98, 205, 114)


def help_display():
    help_menu = True
    while help_menu:
        pygame_window = pygame.display.set_mode((480, 480))
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
                font_two = pygame.font.SysFont('impact', 60)

                text_escape = font.render('Escape', True, light_green)
                pygame_window.blit(text_escape, (0, 0))

                text_help_one = font.render('To move the snake in the direction you want, you must ', True, light_green)
                pygame_window.blit(text_help_one, (0, 50))

                text_help_two = font.render('control it using the arrow keys.', True, light_green)
                pygame_window.blit(text_help_two, (0, 75))

                text_help_three = font.render('Food dots will randomly appear on the screen, one at a time.', True,
                                              light_green)
                pygame_window.blit(text_help_three, (0, 100))

                text_help_four = font.render('Your goal is to collect as much food as possible to increase ', True,
                                             light_green)
                pygame_window.blit(text_help_four, (0, 125))

                text_help_five = font.render('your score. As you eat more food the snakes body will grow.', True,
                                             light_green)
                pygame_window.blit(text_help_five, (0, 150))

                text_help_six = font.render('If the snake crashes into its body or the border of the ', True,
                                            light_green)
                pygame_window.blit(text_help_six, (0, 175))

                text_help_six = font.render('windows, the game is over.', True,
                                            light_green)
                pygame_window.blit(text_help_six, (0, 200))

                text_help_seven = font.render('When the game begins the snake will be still. The game', True,
                                              light_green)
                pygame_window.blit(text_help_seven, (0, 225))

                text_help_eight = font.render('will being once your press an arrow key ', True,
                                              light_green)
                pygame_window.blit(text_help_eight, (0, 250))

                text_help_seven = font_two.render('Good luck', True, light_green)
                pygame_window.blit(text_help_seven, (120, 360))

                pygame.display.update()
                (pygame.time.Clock()).tick(15)


def main_menu():
    closeGame = False
    while not closeGame:
        pygame.display.set_caption('SWEN Snake')
        pygame_window = pygame.display.set_mode((480, 480))
        font = pygame.font.SysFont('impact', 60)
        font_two = pygame.font.SysFont('impact', 30)
        menu = True
        selected = "start"
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    closeGame = True
                    menu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "help"
                    elif event.key == pygame.K_ESCAPE:
                        selected = "escape"
                        closeGame = True
                        menu = False
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            menu = False
                            game()
                            print("Start")
                            closeGame = True

                        if selected == "help":
                            print("Help")
                            menu = False
                            help_display()
                        if selected == "escape":
                            closeGame = True
                            menu = False
            pygame_window.fill(background_color)
            title = font.render('Pygame Snake', True, light_green)

            if selected == "start":
                text_start = font.render('Start', True, mid_green)
            else:
                text_start = font.render('Start', True, light_green)
            if selected == "help":
                text_help = font.render('Help', True, mid_green)
            else:
                text_help = font.render('Help', True, light_green)
            text_escape = font_two.render('Escape', True, light_green)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            text_help.get_rect()
            text_escape.get_rect()

            # Main Menu Text
            pygame_window.blit(title, (480 / 2 - (title_rect[2] / 2), 80))
            pygame_window.blit(text_start, (480 / 2 - (start_rect[2] / 2), 300))
            pygame_window.blit(text_help, (480 / 2 - (start_rect[2] / 2), 360))
            pygame_window.blit(text_escape, (0, 0))
            pygame.display.update()
            (pygame.time.Clock()).tick(15)


# Mini Game Snake

def game():
    closeGame = False
    while not closeGame:
        pygame_window = pygame.display.set_mode((480, 480))
        # Default game parameters
        head = [240, 240]
        trail = [[]]
        movement = 'STAND BY'
        movement_filter = movement
        rng = random.randint(10, 470)
        rng_2 = random.randint(10, 470)
        point_location = [round(rng, -1), round(rng_2, -1)]
        point_on_screen = True
        points = 0
        while point_on_screen:

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
                head[1] -= 10
            if movement == 'X-':
                head[0] -= 10
            if movement == 'Y-':
                head[1] += 10
            if movement == 'X+':
                head[0] += 10

            # Increases trail length
            trail.insert(0, list(head))

            if head[0] == point_location[0] and head[1] == point_location[1]:
                points += 1
                point_on_screen = False
            else:
                trail.pop()

            # Changes point position

            if point_on_screen == False:
                rng = random.randint(10, 470)
                rng_2 = random.randint(10, 470)
                point_location = [round(rng, -1), round(rng_2, -1)]
            point_on_screen = True

            # Refreshes Screen
            pygame_window.fill(background_color)

            for length in trail:
                pygame.draw.rect(pygame_window, mid_green, pygame.Rect(length[0], length[1], 10, 10))

            # Draws food
            pygame.draw.rect(pygame_window, light_green, pygame.Rect(point_location[0], point_location[1], 10, 10))

            # Border and Body Collision

            if head[0] < 0 or head[0] > 470 or head[1] < 0 or head[1] > 470:
                font = pygame.font.SysFont('impact', 60)
                font_output = font.render('Game Over', True, light_green)
                font_position = font_output.get_rect()
                font_position.midtop = (240, 160)
                pygame_window.fill(background_color)
                pygame_window.blit(font_output, font_position)
                points_position.midtop = (240, 240)
                pygame_window.blit(font_points_output, points_position)
                pygame.display.flip()
                time.sleep(5)
                closeGame = True
                point_on_screen = False
            '''
            if head[0] < 0:
                head[0] = 480
            if head[0] > 480:
                head[0] = 0
            if head[1] < 0:
                head[1] = 480
            if head[1] > 480:
                head[1] = 0
            '''

            # Touching the snake body
            for block in trail[1:]:
                if head[0] == block[0] and head[1] == block[1]:
                    font = pygame.font.SysFont('impact', 60)
                    font_output = font.render('Game Over', True, light_green)
                    font_position = font_output.get_rect()
                    font_position.midtop = (240, 160)
                    pygame_window.fill(background_color)
                    pygame_window.blit(font_output, font_position)
                    points_position.midtop = (240, 240)
                    pygame_window.blit(font_points_output, points_position)
                    pygame.display.flip()
                    time.sleep(5)
                    closeGame = True
                    point_on_screen = False

            font_points = pygame.font.SysFont('impact', 30)
            font_points_output = font_points.render('Points : ' + str(points), True, light_green)
            points_position = font_points_output.get_rect()
            points_position.midtop = (240, 20)
            pygame_window.blit(font_points_output, points_position)

            pygame.display.update()

            (pygame.time.Clock()).tick(15)


def main():
    main_menu()


if __name__ == '__main__':
    main()


else:
    print("Being called from menu")
