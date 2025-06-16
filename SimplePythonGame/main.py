import pygame
import time
import copy
from dataclasses import dataclass


@dataclass
class Player:
    i: int
    j: int
    c: str = '◭'


def write_board(board: str):
    for line in board:
        print(''.join(line))


def main():
    PLAYING = True
    pygame.init()
    start_time = time.time()
    board1 = ['----------',
              '|   *    |',
              '|        |',
              '|        |',
              '|        |',
              '|     *  |',
              '|  *     |',
              '|        |',
              '|        |',
              '|   *    |',
              '|      🏁|',
              '----------']
    win_board = ['          _______          ',
                 '|\     /|(  ___  )|\     /|',
                 '( \   / )| (   ) || )   ( |',
                 ' \ (_) / | |   | || |   | |',
                 '  \   /  | |   | || |   | |',
                 '   ) (   | |   | || |   | |',
                 '   | |   | (___) || (___) |',
                 '   \_/   (_______)(_______)',
                 '                           ',
                 '         _________ _       ',
                 '|\     /|\__   __/( (    /|',
                 '| )   ( |   ) (   |  \  ( |',
                 '| | _ | |   | |   |   \ | |',
                 '| |( )| |   | |   | (\ \) |',
                 '| || || |   | |   | | \   |',
                 '| () () |___) (___| )  \  |',
                 '(_______)\_______/|/    )_)']


    base_board = [[c for c in line] for line in board1]
    p = Player(1, 1)

    main_board = [line[:] for line in base_board][:] + [f'time taken = {time.time()-start_time:3.2f}s']

    while PLAYING:
        time.sleep(0.01)
        current_time = time.time()
        write_board(main_board)
        main_board[p.j][p.i] = copy.copy(base_board[p.j][p.i])
        main_board[-1] = [f'time taken = {current_time-start_time:3.2f}s']
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_board[p.j - 1][p.i] in [' ', '🏁']:
                        p.j -= 1
                elif event.key == pygame.K_DOWN:
                    if main_board[p.j + 1][p.i] in [' ', '🏁']:
                        p.j += 1
                elif event.key == pygame.K_LEFT:
                    if main_board[p.j][p.i - 1] in [' ', '🏁']:
                        p.i -= 1
                elif event.key == pygame.K_RIGHT:
                    if main_board[p.j][p.i + 1] in [' ', '🏁']:
                        p.i += 1
                else:
                    PLAYING = False
        print("\033c", end="")
        if main_board[p.j][p.i] == '🏁':
            win_board += [f'time taken = {time.time()-start_time:3.2f}s']
            write_board(win_board)
            time.sleep(5)
            PLAYING = False
        main_board[p.j][p.i] = p.c


if __name__ == '__main__':
    main()
