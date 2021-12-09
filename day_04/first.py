import lib

if __name__ == '__main__':

    fname = lib.file_path('input.txt')
    boards, numbers = lib.read_bingo_data(fname)
    game = lib.BingoGame(boards)

    for number in numbers:
        game.update(number)
        if game.found:
            break

    assert game.product == 51034