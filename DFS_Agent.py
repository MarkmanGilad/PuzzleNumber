from Action import Action
from Puzzle import Puzzle
from State import State
import pygame

class DFS_Agent:
    
    def __init__(self, environment:Puzzle, goal: State):
        self.state = environment.state
        self.goal = goal
        self.environment = environment
        self.path = []
        self.stop = False
        self.maxLevel = 30
            
    def search_path (self, state, goal, visited, path):
        if state == goal:
            self.stop = True
            self.path = path.copy()
            return
        if self.stop:
            return
        
        if len(path) == self.maxLevel:
            print("max : ", len(visited))
            return
    
        actions = self.environment.get_actions(state)
        for action in actions:
            new_state = self.environment.next_state(action, state)
            if new_state  in visited:
                print ("in") 
            if new_state not in visited and not self.stop:
                visited.append(state)
                path.append(action)
                self.search_path(new_state, goal, visited, path)
                path.pop()
                
        
    def get_Action (self, event):
        if self.path is None or len(self.path) == 0:
            self.search_path(self.state, self.goal, [], [])
            print(self.path)
            print(len(self.path))
            
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            return self.path.pop(0)
        else:
            return None

    