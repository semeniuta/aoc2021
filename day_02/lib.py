import pathlib


def evolve_state(state, fname='input.txt'):
    
    fpath = pathlib.Path('.') / 'data' / fname
    with fpath.open() as f:
        for line in f.readlines():
            state.update(line)


def parse_command(command):
    action, num_str = command.split()
    delta = int(num_str)

    if action == 'forward':
        return delta, 0

    if action == 'down':
        return 0, delta
    
    if action == 'up':
        return 0, -delta