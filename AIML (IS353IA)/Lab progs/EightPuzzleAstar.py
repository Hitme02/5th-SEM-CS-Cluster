import numpy as np
from queue import PriorityQueue

class State:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    def __lt__(self, other):
        return False  # Define a default comparison method

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def print_state(self, state):
        print(state[:, :])

    def is_goal(self, state):
        return np.array_equal(state, self.goal_state)

    def get_possible_moves(self, state):
        possible_moves = []
        zero_pos = np.where(state == 0)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
        for direction in directions:
            new_pos = (zero_pos[0] + direction[0], zero_pos[1] + direction[1])
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:  # Check boundaries
                new_state = np.copy(state)
                new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]  # Swap
                possible_moves.append(new_state)
        return possible_moves

    def heuristic(self, state):
         return np.count_nonzero(state != self.goal_state)


    def solve(self):
        queue = PriorityQueue()
        initial_state = State(self.initial_state, None)
        queue.put((0, initial_state))  # Put State object in queue
        visited = set()

        while not queue.empty():
            priority, current_state = queue.get()
            if self.is_goal(current_state.state):
                return current_state  # Return final state
            for move in self.get_possible_moves(current_state.state):
                move_state = State(move, current_state)  # Create new State for move
                if str(move_state.state) not in visited:
                    visited.add(str(move_state.state))
                    priority = self.heuristic(move_state.state)
                    queue.put((priority, move_state))  # Put State object in queue
        return None

# Test the function
initial_state = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
goal_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
puzzle = Puzzle(initial_state, goal_state)
solution = puzzle.solve()
move1 = -1
if solution is not None:
    moves = []
    while solution is not None:  # Go through parents to get moves
        moves.append(solution.state)
        solution = solution.parent
    for move in reversed(moves): 
        move1+=1 # Print moves in correct order
        puzzle.print_state(move)
    print("no of moves: ",move1)
else:
    print("No solution found.")