import numpy as np
import pygame
from Graphics import Graphics
# from constant import *
from State import State
from Puzzle import Puzzle
from Human_Agent import Human_Agent
from DFS_Agent import DFS_Agent
from BFS_Agent import BFS_Agent
from BFS_Agent2 import BFS_Agent2
from A_Star_Agent import A_Star_Agent
from Greedy_BFS_Agent import Greedy_BFS_Agent 
import time
start_time = time.time()


def main ():

    FPS = 60
    
    # board = np.array([[1, 7, 5], [2, 0, 8],[3, 6, 4]])
    # board = np.array([[3, 2, 8], [5, 0, 1],[6, 7, 4]])
    board = np.array([[4, 9, 1, 3], [5, 15, 2, 6],[0, 8, 13, 14],[12, 10, 7, 11]])
    puzzle = Puzzle()
    # puzzle.shuffle(iteration=100)
    puzzle.state.board = board
    puzzle.state.set_blank_pos()
    ROWS, COLS = puzzle.state.rows, puzzle.state.cols
    HEIGHT, WIDTH = ROWS * 100, COLS *100
    goal = puzzle.make_goal_state(ROWS, COLS)
    win = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption('Puzzle')
    graphics = Graphics(win)
    # agent = Human_Agent()
    # agent = DFS_Agent(puzzle, goal)
    agent = BFS_Agent(puzzle, goal)
    # agent = BFS_Agent2(puzzle, goal)
    # agent = Greedy_BFS_Agent (puzzle, goal)
    # agent = A_Star_Agent(puzzle, goal)
    run = True
    clock = pygame.time.Clock()
    graphics.draw(puzzle.state)
    pygame.display.update()

    while(run):

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False

            action = agent.get_Action(event)
            puzzle.move(action)
            time.sleep(0.02)
        
        graphics.draw(puzzle.state)
        pygame.display.update()
        
        if puzzle.state == goal:
            print("Victory")
            run = False
            
            time.sleep(3)
    pygame.quit()

if __name__ == '__main__':
    main()
    