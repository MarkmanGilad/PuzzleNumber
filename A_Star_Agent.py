from Action import Action
from Puzzle import Puzzle
from State import State
import pygame
import time

class A_Star_Agent:
    
    def __init__(self, environment:Puzzle, goal: State):
        self.state = environment.state
        self.goal = goal
        self.environment = environment
        self.path = []

    def search_path (self, state:State, goal:State):
        start_time = time.time()
        visited = {}
        heap = {}
        state.action = None
        state.g = 0
        state.calc_h()
        heap[state] = state.f, state.g
    
        while heap:
            
            state = min(heap, key= lambda k: heap[k][0])
            heap.pop(state)
            visited[state] = state.action
            print(state.h, ", ", state.f, ", ", state.g)   
            
            if state == goal:
                print("--- %s seconds for victory ---" % (time.time() - start_time))
                print(len(visited))
                return self.find_path(goal, visited)
            
            actions = self.environment.get_actions(state)
            for action in actions:
                cost = 1
                new_state = self.environment.next_state(action, state)
                if new_state in visited:
                    continue
                
                new_state.action = action
                new_state.g = state.g + cost
                new_state.calc_h()

                if new_state not in heap:
                    heap[new_state] = new_state.f, new_state.g

                elif heap[new_state][1] > state.g + cost:
                    heap[new_state] = new_state.f, new_state.g
                    
        return []

    def find_path (self, state, visited):
        self.path = []
        while visited[state]:
            action = visited[state]
            self.path.insert(0, action)
            state = self.environment.next_state(action.inverse(action), state)
        return self.path 

    def get_Action (self, event):
        if self.path is None or len(self.path) == 0:
            self.search_path(self.state, self.goal)
            print(self.path)
            print(len(self.path))
            
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            return self.path.pop(0)
        else:
            return None

    