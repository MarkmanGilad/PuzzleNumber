from enum import Enum

class Action (Enum):
    UP = 1
    RIGHT = 2
    LEFT = 3
    DOWN = 4

    def inverse (self, action):
        match action:
            case Action.UP: return Action.DOWN
            case Action.DOWN: return Action.UP
            case Action.RIGHT: return Action.LEFT
            case Action.LEFT: return Action.RIGHT