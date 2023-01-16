from Action import Action
from Puzzle import Puzzle
from State import State
import pygame

class BFS_Agent:
    
    def __init__(self, environment:Puzzle, goal: State):
        self.state = environment.state
        self.goal = goal
        self.environment = environment
        self.path = []
        self.stop = False
        self.maxLevel = 40
            
    def search_path (self, start, goal):
        
        visited = {start}
        queue = [start]
        parentTree ={start: (None, None)} #(state, Action)

        while queue:
            print(len(visited))
            state = queue.pop()
            if state == goal:
                return self.find_path(goal, parentTree)
            
            actions = self.environment.get_actions(state)
            for action in actions:
                new_state = self.environment.next_state(action, state)
                if new_state not in visited:
                    queue.insert(0, new_state)
                    visited.add(new_state)
                    parentTree[new_state] = state, action
            
        return self.find_path(parentTree)

    def find_path (self, goal, parentTree):
        self.path = []
        state, action = parentTree[goal]
        self.path = [action] 
        while parentTree[state][0]:
            state, action = parentTree[state]
            self.path.insert(0, action)
        # return path       
        
    def get_Action (self, event):
        if self.path is None or len(self.path) == 0:
            self.search_path(self.state, self.goal)
            print(self.path)
            print(len(self.path))
            
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            return self.path.pop(0)
        else:
            return None

    