import numpy as np
import pygame
import sys
import math
import menu

BRIGHTBLUE = (0, 78, 255)
NAVYBLUE = (0, 0, 205)
COLOR1 = NAVYBLUE
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BRICKRED = (178, 34, 34)
COLOR2 = BRICKRED
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
LIME = (0, 255, 0)
ORANGE = (247, 105, 2)

RETURN = False

ROW_COUNT = 6
COLUMN_COUNT = 7

pygame.init()
largeText = pygame.font.Font('freesansbold.ttf', 50)
medText = pygame.font.Font('freesansbold.ttf', 40)


# Creates Board (Grid)
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


# where a piece lands on the grid
def drop_piece(board, row, col, piece):
    board[row][col] = piece


# checks if piece dropped is not being dropped onto the last row
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


# check to see if next available row is valid at column(col)
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


# prints boards state onto the console
def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


# Draws the GUI for the connect 4 board as well as the pieces dropped into the board
def draw_board(board, screen, SQUARESIZE, height, RADIUS):
    # connect 4 board
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, ORANGE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    # pieces dropped into the board
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


# Function to create buttons
def creating_buttons_menu(screen, font, words, pos_x, pos_y, width, height, COLOR):
    text = font.render(words, True, WHITE)
    textRect = pygame.draw.rect(screen, COLOR, (pos_x, pos_y, width, height))
    font_rect = text.get_rect()
    font_rect.center = textRect.center
    return text, font_rect


# check if mouse is hovering over a button
def isHovering(rect, pos):
    if pos[0] > rect.left and pos[0] < rect.left + rect.width:
        if pos[1] > rect.top and pos[1] < rect.top + rect.height:
            return True
    return False


# Game play
def play_game():
    global RETURN
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    pygame.display.set_caption("Connect 4")
    screen = pygame.display.set_mode(size)
    draw_board(board, screen, SQUARESIZE, height, RADIUS)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                RETURN = True

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            screen.blit(label, (22, 10))
                            game_over = True


                # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (22, 10))
                            game_over = True

                if 0 not in board:
                    label = myfont.render("It's a tie!!", 1, LIME)
                    screen.blit(label, (40, 10))
                    game_over = True;

                print_board(board)
                draw_board(board, screen, SQUARESIZE, height, RADIUS)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)


# Menu before launching actual game - allows player to play again or quit and go back to the launcher
def menu():
    global COLOR1, COLOR2, RETURN
    exitGame = False
    width = int(700 / 5)
    height = 75

    while not exitGame:
        screen = pygame.display.set_mode((600, 500))
        pygame.display.set_caption("Menu")
        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (230, 90), 65, 4)
        pygame.draw.circle(screen, YELLOW, (355, 90), 65, 4)
        pygame.draw.rect(screen, BRIGHTBLUE, (35, 171, 535, 85))
        text1, font_rect1 = creating_buttons_menu(screen, medText, "Welcome to Connect 4", 40, 175, 2100 // 4, 80,
                                                  BLACK)
        text2, font_rect2 = creating_buttons_menu(screen, largeText, "Play", 100, 350, width, height, COLOR1)
        text3, font_rect3 = creating_buttons_menu(screen, largeText, "Quit", 360, 350, width, height, COLOR2)
        screen.blit(text1, font_rect1)
        screen.blit(text2, font_rect2)
        screen.blit(text3, font_rect3)
        pygame.display.update()
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                # Gets out menu and returns to the launcher
                exitGame = True

            # checks if mouse is hovering over button
            if ev.type == pygame.MOUSEMOTION:
                if isHovering(font_rect2, pos):
                    COLOR1 = BRIGHTBLUE
                    pygame.display.update()
                else:
                    COLOR1 = NAVYBLUE
                    pygame.display.update()
                if isHovering(font_rect3, pos):
                    COLOR2 = RED
                    pygame.display.update()
                else:
                    COLOR2 = BRICKRED
            # checks if button is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if isHovering(font_rect2, pos):
                    play_game()
                if isHovering(font_rect3, pos):
                    # Gets out menu and returns to the launcher
                    exitGame = True
        if RETURN:
            exitGame = True
            RETURN = False


def main():
    menu()


if __name__ == '__main__':
    main()

else:
    print("Being called from menu")
    # menu()
