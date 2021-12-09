import numpy as np
import lib


def bit_criteria_selection(data, reversed=False):

    n_numbers, n_bits = data.shape
    selected = np.ones(n_numbers, dtype=bool)
    x = data

    for j in range(n_bits):

        x = x[selected]

        col = x[:, j]
        common = lib.find_common(col)
        if reversed:
            common = ~common
        selected = (col == common)

        if np.sum(selected) == 1:
            binary_res = x[selected].ravel()
            return lib.binary_array_to_int(binary_res)


if __name__ == '__main__':

    data = lib.read_data('input.txt')
    
    rating_oxygen = bit_criteria_selection(data)
    rating_co2 = bit_criteria_selection(data, reversed=True)
    result = rating_oxygen * rating_co2

    assert result == 3385170

    print(f'Oxygen: {rating_oxygen}')
    print(f'CO2: {rating_co2}')
    print(f'Result: {result}')