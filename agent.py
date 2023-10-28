import rgb
import util
import random
class Agent:
    def __init__(self, state):
        self.__state = state

    def _search(self, query):
        count = 0
        state = self.__state
        fringe = [] #open list
        closed = [] #visited list
        

        
        if query == "astar":
            initial_node = Node(state, parent =None, state_value= self.heuristic_value(state))
            gNStart = initial_node.get_number_of_state_from_start()-1     
        else:
            initial_node = Node(state)
        fringe.append(initial_node)


        while fringe:
            if query == "bfs":
                node = fringe.pop(0)    # for BFS, remove from the front (given we append thing at the end)
            elif query == "dfs":
                node = fringe.pop()     # for DFS, remove from the end (given we append thing at the end)
            elif query == "astar":      # for Astar, remove from the front after sorting the state value from smallest to largest
                fringe = sorted(fringe, key=lambda node : node.getStateValue())
                node = fringe.pop(0)

                
            util.pprint(node.get_path())
            count+=1

            if node.getState().is_goal():
                print(count)
                break
            
            if node.getState() not in closed and node.getState() not in fringe:
                closed.append(node)
                state = node.getState()     # Get the current state from the node
                actions = state.actions()   # Get a list of available actions for the current state

                for action in actions:
                    new_state = state.clone()  
                    new_state.execute(action) 
                    
                    #bfs and dfs
                    if query != "astar":    
                        child_node = Node(new_state, parent=node)
                    
                    #astar
                    else:
                        
                        gN = node.get_number_of_state_from_start()                  
                        child_node = Node(new_state, parent=node, state_value= self.heuristic_value(new_state) + gN)

                    # append to the open list at the end
                    if child_node.getState() not in closed and child_node.getState() not in fringe:
                        fringe.append(child_node)             
                        

    def bfs(self): 
        return self._search("bfs")
    def dfs(self):
        return self._search("dfs")
    def astar(self):
        return self._search("astar")
    
    def random_walk(self, state, n):
        current_node = Node(state)
        for i in range(n-1):
            current_state = rgb.State(str(current_node))
            parent_node = current_node
            actions = current_state.actions()
            action = random.choice(actions)
            current_node = Node(current_state.execute(action), parent= parent_node )
        
        util.pprint(current_node.get_path())
    
    
    # Heuristic function to count adjacent cells with the same color
    def heuristic_value(self, state):
        # state = self.__state
        count = 0
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x in range(state.size):
            for y in range(state.size):
                cell = state.get(x, y)
                if cell != rgb.Cell.EMPTY:
                    for dx, dy in deltas:
                        adj_x, adj_y = x + dx, y + dy
                        if state.is_legal(adj_x, adj_y) and state.get(adj_x, adj_y) == cell:
                            count += 1
        return count
    
    def get_correct_position(self, color):
        if color == 'r':
            return 0, 0
        elif color == 'g':
            return 0, 1
        elif color == 'b':
            return 1, 0

class Node:
    def __init__(self, state, parent=None, state_value=None):
        self.__state = state  
        self.__parent = parent  
        self.__state_value = state_value  

    def __str__(self):
        return f"{self.__state}"

    def __repr__(self):
        return f"Current State:{self.__state}, parent_state={self.__parent}]"
    
    def getState(self):
        return self.__state
    
    def getParent(self):
        return self.__parent
    
    def getStateValue(self):
        return self.__state_value
    
    def get_path(self):
        path = []
        current_node = self
        while current_node is not None:
            path.insert(0, current_node.__state)
            current_node = current_node.__parent
        return path
    
    #count: this is g(n) (distance from starting state) for astar
    def get_number_of_state_from_start(self):
        count = 0
        current_node = self
        while current_node is not None:
            count += 1
            current_node = current_node.__parent
        return count

