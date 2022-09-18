from aima.search import *

class MissionariesCanibals(Problem):

    def __init__(self, initial, goal=(0, 0, 0)):

        self.goal = goal
        Problem.__init__(self, initial, goal)

    def actions(self, state):
        # M-missionar C-canibal
        possible_actions = ['MM', 'MC', 'CC', 'M', 'C']
        offset = [(2, 0), (1, 1), (0, 2), (1, 0),
                  (0, 1)]  # represents how many missionars or canibals crossed if the boat is at the first riverbank
        offsetOppos = [(-2, 0), (-1, -1), (0, -2), (-1, 0), (0, -1)]  # represents the opposite than offset
        if state[2] == 0:
            offset = offsetOppos

        for i in range(4, -1, -1):
            new_state = (state[0] - offset[i][0], state[1] - offset[i][1], 1 - state[2])
            if new_state[0] < 0 or new_state[0] > 3 or new_state[1] < 0 or new_state[
                1] > 3:  # if the action led to an impossible state
                del possible_actions[i]
                del offset[i]
            elif (new_state[0] < new_state[1] and new_state[0] > 0) or (
                    new_state[0] > new_state[1] and new_state[0] < 3):  # if there are more canibals than missionars
                del possible_actions[i]
                del offset[i]

        return possible_actions

    def result(self, state, action):

        possible_actions = ['MM', 'MC', 'CC', 'M', 'C']
        offset = [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1)]
        possible_actions_index = possible_actions.index(action)
        # check there are enough missionaries/canibals where the boat is
        if state[2] == 1:
            new_state = (
                state[0] - offset[possible_actions_index][0], state[1] - offset[possible_actions_index][1], 1 - state[2])
        else:
            new_state = (
                state[0] + offset[possible_actions_index][0], state[1] + offset[possible_actions_index][1], 1 - state[2])

        return new_state

    def goal_test(self, state):

        return state == self.goal

    def heuristics(self, node):

        return node.state[0] + node.state[1] - 1


if __name__ == '__main__':
    problem = MissionariesCanibals((3, 3, 1))
    print(astar_search(problem))
