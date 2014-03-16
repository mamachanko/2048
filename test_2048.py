from itertools import permutations
from copy import deepcopy

from p2048 import Board


from p2048 import merge, right_pad, move, rotate


def test_single_digit_move():
    assert [2, 0, 0, 0] == move([0, 0, 2, 0])


def test_multi_digit_move():
    assert [2, 4, 0, 0] == move([0, 0, 2, 4])


def test_idempotent_move():
    assert [2, 4, 8, 0] == move([2, 4, 8, 0])


def test_move_closes_small_gap():
    assert [4, 2, 8, 0] == move([4, 0, 2, 8])


def test_move_closes_big_gap():
    assert [2, 8, 0, 0] == move([2, 0, 0, 8])


def test_move_with_simple_merge():
    for permutation in permutations([2, 2, 0, 0]):
        assert [4, 0, 0, 0] == move(list(permutation))


def test_left_padded_merge_move():
    assert [4, 0, 0, 0] == move([0, 0, 2, 2])


def test_simple_merge():
    assert [4] == merge([2, 2])
    assert [4, 2] == merge([2, 2, 2])
    assert [2, 8] == merge([2, 4, 4])
    assert [4, 4] == merge([2, 2, 2, 2])
    assert [4, 4, 4] == merge([4, 2, 2, 4])


def test_right_pad_empty_list_to_four():
    assert [0, 0, 0, 0] == right_pad([])


def test_right_pad_list_to_four():
    assert [2, 4, 0, 0] == right_pad([2, 4])


def test_right_pad_list_to_defined_length():
    assert [2, 4, 0] == right_pad([2, 4], size=3)


def test_idempotent_right_pad():
    assert [2, 4] == right_pad([2, 4], size=2)
    assert [2, 4, 8] == right_pad([2, 4, 8], size=2)


def test_rotates_board_clockwise():
    board = [[2,]*4, [4,]*8, [8,]*4, [16,]*4]
    assert [[16, 8, 4, 2]]*4 == rotate(board)


def test_four_rotations_equal_no_rotation():
    board = [[2,]*4, [4,]*4, [8,]*4, [16,]*4]
    _board = deepcopy(board)
    for x in range(4):
        _board = rotate(_board)
    assert board == _board


def test_Board_init():
    board = Board()
    assert 4 == len(board.board)
    for row in board.board:
        4 == len(board.board)
    assert 2 == board.serialize().count(2)
    assert 14 == board.serialize().count(0)


def test_board_serialization():
    board = Board()
    serialized_board = board.serialize()
    assert 16 == len(serialized_board)
    split_indices = map(lambda x: 4*x, range(4))
    deserialized = [serialized_board[index:index+4] for index in split_indices]
    assert deserialized == board.board


def test_board_rotate():
    board = Board()
    initial_state = deepcopy(board.board)
    board.rotate()
    assert rotate(initial_state) == board.board


def test_move_left():
    board = Board()
    initial_state = deepcopy(board.board)
    board.move_left()
    for initial_row, moved_row in zip(initial_state, board.board):
        assert move(initial_row) == moved_row
