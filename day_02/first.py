from lib import evolve_state
from lib import parse_command


class State:

    def __init__(self):
        self.position = 0
        self.depth = 0

    def update_position(self, delta):
        self.position += delta

    def update_depth(self, delta):
        self.depth += delta

    def update(self, command):
        pos_delta, depth_delta = parse_command(command)

        if pos_delta != 0:
            self.update_position(pos_delta)

        if depth_delta != 0:
            self.update_depth(depth_delta)


if __name__ == '__main__':

    state = State()
    evolve_state(state)

    answer = state.depth * state.position

    print(f'Position: {state.position}')
    print(f'Depth: {state.depth}')
    print(f'Product: {answer}')

    assert(answer == 1648020)