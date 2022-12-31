# Environment
from constant import *
from State import State
from Action import Action
import numpy as np
import random

class Puzzle:

    def __init__(self, state:State = None):
        self.state = state

    def make_goal_state (self, rows=ROWS, cols=COLS):
        board = np.arange(rows*cols)
        board = board.reshape((rows, cols))
        return State(board)

    def is_legal_action (self, action: Action, state:State = None):
        if state is None:
            state = self.state
        if action is None:
            return False
        blank_row, blank_col = state.get_blank_pos()
        match action:
            case Action.UP: return blank_row > 0
            case Action.DOWN: return blank_row < state.rows-1
            case Action.RIGHT: return blank_col < state.cols-1
            case Action.LEFT : return blank_col > 0

    def get_actions (self, state: State = None):
        if state is None:
            state = self.state
        actions = []
        if self.is_legal_action(Action.DOWN, state): 
            actions.append(Action.DOWN)
        if self.is_legal_action(Action.RIGHT, state): 
            actions.append(Action.RIGHT)
        if self.is_legal_action(Action.UP, state): 
            actions.append(Action.UP)
        if self.is_legal_action(Action.LEFT, state): 
            actions.append(Action.LEFT)
        return actions

    def move (self, action: Action):
        if not self.is_legal_action(action):
            return
        state = self.state
        blank_row, blank_col = state.get_blank_pos()
        target_row, target_col = blank_row, blank_col
        match action:
            case Action.UP: target_row -=1
            case Action.DOWN: target_row +=1
            case Action.RIGHT: target_col +=1
            case Action.LEFT : target_col -=1
        state.board[blank_row, blank_col], state.board[target_row, target_col] = state.board[target_row, target_col], state.board[blank_row, blank_col]
        

    def next_state (self, action: Action, state: State):
        if not self.is_legal_action(action, state):
            return
        state = state.copy()
        blank_row, blank_col = state.get_blank_pos()
        target_row, target_col = blank_row, blank_col
        match action:
            case Action.UP: target_row -=1
            case Action.DOWN: target_row +=1
            case Action.RIGHT: target_col +=1
            case Action.LEFT : target_col -=1
        state.board[blank_row, blank_col], state.board[target_row, target_col] = state.board[target_row, target_col], state.board[blank_row, blank_col]
        return state

    def shuffle (self, state: State = None, iteration=70):
        if state is None:
            self.state = self.make_goal_state()
        path = []
        for i in range(iteration):
            actions = self.get_actions()
            action = random.choice(actions)
            self.move(action)
            path.append(action)
        return path