import numpy as np
import lib


class BinaryDiagnostics:
    def __init__(self, fname):
        self.data = lib.read_data(fname)
        
        self.gamma_binary = lib.find_common(self.data)
        self.epsilon_binary = ~self.gamma_binary

        self.gamma = lib.binary_array_to_int(self.gamma_binary)
        self.epsilon = lib.binary_array_to_int(self.epsilon_binary)
    

def test():

    diag = BinaryDiagnostics('test_input.txt')

    assert diag.gamma == 22
    assert diag.epsilon == 9


if __name__ == '__main__':

    test()
    
    diag = BinaryDiagnostics('input.txt')
    result = diag.gamma * diag.epsilon

    print(f'Result: {result}')

    assert result == 3882564

