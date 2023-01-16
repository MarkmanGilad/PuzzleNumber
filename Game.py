import numpy as np
import pygame
from Graphics import Graphics
from constant import *
from State import State
from Puzzle import Puzzle
from Human_Agent import Human_Agent
from DFS_Agent import DFS_Agent
from BFS_Agent import BFS_Agent
from BFS_Agent2 import BFS_Agent2
import time


def main ():

    FPS = 60
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Puzzle')

    puzzle = Puzzle()
    puzzle.shuffle(iteration=30)
    goal = puzzle.make_goal_state(ROWS,COLS)

    graphics = Graphics(win)
    # agent = Human_Agent()
    # agent = DFS_Agent(puzzle, goal)
    # agent = BFS_Agent(puzzle, goal)
    agent = BFS_Agent2(puzzle, goal)
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
    