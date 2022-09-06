import numpy as np
import pygame
import sys


pygame.init()

# Colors
screen_color = (28, 128, 128)

# Makes the screen size 700 by 700
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Tic Tac Toe')
player1 = 1
player2 = 2
board = np.zeros((3, 3))
square_size = 235

def make_square():

    width = 700
    line_width = 20
    line_color = (128,128,128)
    screen = pygame.display.set_mode((700, 700))
    screen.fill(screen_color)

    # Makes the horizontal line
    pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
    pygame.draw.line(screen, line_color, (0, square_size * 2), (width, square_size * 2), line_width)

    # Makes the vertical line
    pygame.draw.line(screen, line_color, (square_size, 0), (square_size, width), line_width)
    pygame.draw.line(screen, line_color, (square_size * 2, 0), (square_size * 2, width), line_width)


player = 2
def draw_player_sign():
    square = 235
    for row in range(3):
        for colom in range(3):
            if board[row][colom] == player1:
                pygame.draw.circle(screen, (143, 0, 255),(int(colom * square + square//2),
                                                        int(row * square + square//2)), 60, 15)
            elif board[row][colom] == player2:
                pygame.draw.line(screen, (0, 0, 255), (colom * square + 55,
                                                       row * square + square - 55),
                                 (colom * square + square - 55, row * square + 55), 22)
                pygame.draw.line(screen, (0, 0, 250), (colom * square + 55, row * square + 55),
                                 (colom * square + square - 55, row * square + square - 55), 22)


def draw_on_square(row, colom, player):
    board[row][colom] = player
#
# def check(player):
#     for colom in range(3):
#         if board[0][colom] == player and board[1][colom] == player and board[2][colom] == player:


def open_square(row, colom):
    return board[row][colom] == 0

def board_full():
    for row in range(3):
        for colom in range(3):
            if board[row][colom] == 0:
                return False
    return True

def draw_diagonal_win(side, player):
    if player == player1:
        color = (0, 0, 255)
    elif player == player2:
        color = (0, 0, 255)

    if side == 1:
        pygame.draw.line(screen, color, (15, 700- 15), (700-15, 15), 20)
    elif side == 2:
        pygame.draw.line(screen, color, (15, 15), (700 - 15, 700 - 15), 20)

def draw_win_line(side, len, player):
    len = len * square_size + square_size // 2

    if player == 1:
        color = 143, 0, 255
    elif player == 2:
        color = 0, 0, 255


    if side == 1:
        pygame.draw.line(screen, color, (len, 15), (len, 700 - 15), 15)
    elif side == 2:
        pygame.draw.line(screen, color, (15, len), (700 - 15, len), 15)

def win_check(player):
    # checks for horizontal win
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            draw_win_line(2, i, player)
            return True

        # checks for the vertical win
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            draw_win_line(1, i, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diagonal_win(1, player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonal_win(2, player)
        return True

    return False


def menu():
    print("")


def main():
    make_square()
    player = 2

    # players score
    player1_win = 0
    player2_win = 0
    count = 0

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                if count == 1:
                    x_axis = event.pos[0]
                    y_axis = event.pos[1]

                    colom = int(x_axis // 235)
                    row = int(y_axis // 235)

                    if open_square(row, colom):
                        draw_on_square(row, colom, player)
                        draw_player_sign()

                        if win_check(player):
                            if player == 1:
                                player1_win += 1
                                print("player 1 wins")
                            elif player == 2:
                                player2_win += 1
                                print("player 2 wins")

                            print("Score")
                            print("Player 1: ", player1_win)
                            print("Player 2: ", player2_win)


                    #player +=1
                    player = player % 2 +1
                else:
                    count = 1

        pygame.display.update()



if __name__ == '__main__':
    main()