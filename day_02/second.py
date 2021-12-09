from lib import evolve_state
from lib import parse_command


class CorrectState:

    def __init__(self):
        self.position = 0
        self.depth = 0
        self.aim = 0

    def update(self, command):
        
        forward, down = parse_command(command)

        self.aim += down

        self.position += forward
        self.depth += (self.aim * forward)


if __name__ == '__main__':

    state = CorrectState()
    evolve_state(state, fname='input.txt')

    answer = state.depth * state.position

    print(f'Position: {state.position}')
    print(f'Depth: {state.depth}')
    print(f'Product: {answer}')

    assert(answer == 1759818555)