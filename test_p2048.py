from copy import deepcopy
from itertools import permutations
from functools import partial

import pytest

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
    assert 4 == len(board.state)
    for row in board.state:
        4 == len(board.state)
    assert 2 == board.serialize().count(2)
    assert 14 == board.serialize().count(0)


def test_board_serialization():
    board = Board()
    serialized_board = board.serialize()
    assert 16 == len(serialized_board)
    split_indices = map(lambda x: 4*x, range(4))
    deserialized = [serialized_board[index:index+4] for index in split_indices]
    assert deserialized == board.state


@pytest.fixture(scope='function')
def default_board_state():
    """
    Returns the default initial board state for testing
    """
    return [[2, 0, 2, 0],
            [0, 0, 0, 0],
            [4, 0, 8, 0],
            [0, 0, 0, 0]]


def test_board_rotate(default_board_state):
    board = Board(state=default_board_state)
    board.rotate()
    rotated_board = [[0, 4, 0, 2],
                     [0, 0, 0, 0],
                     [0, 8, 0, 2],
                     [0, 0, 0, 0]]
    assert rotated_board == board.state


def test_move_left(default_board_state):
    board = Board(state=default_board_state)
    board._move_left()
    moved_left = [[4, 0, 0, 0],
                  [0, 0, 0, 0],
                  [4, 8, 0, 0],
                  [0, 0, 0, 0]]
    assert moved_left == board.state


def test_move_right(default_board_state):
    board = Board(state=default_board_state)
    board._move_right()
    moved_right = [[0, 0, 0, 4],
                   [0, 0, 0, 0],
                   [0, 0, 4, 8],
                   [0, 0, 0, 0]]
    assert moved_right == board.state


def test_move_down(default_board_state):
    board = Board(state=default_board_state)
    board._move_down()
    moved_down = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [2, 0, 2, 0],
                  [4, 0, 8, 0]]
    assert moved_down == board.state


def test_move_up(default_board_state):
    board = Board(state=default_board_state)
    board._move_up()
    moved_up = [[2, 0, 2, 0],
                [4, 0, 8, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    assert moved_up == board.state


def test_add_random():
    board = Board()
    initial_state = board.serialize()
    board.add_random()
    assert initial_state != board.serialize()
    conflicts = get_positional_diff(initial_state, board.serialize())
    assert 1 == len(conflicts)
    assert 0 == conflicts[0][0]
    assert conflicts[0][1] in (2, 4)


def test_move_adds_random_digit():
    board = Board()
    copied_board = Board(state=list(board.state))
    board.move_left()
    copied_board._move_left()
    assert copied_board.state != board.state
    conflicts = get_positional_diff(copied_board.serialize(),
                                    board.serialize())
    assert 1 == len(conflicts)
    assert 0 == conflicts[0][0]
    assert conflicts[0][1] in (2, 4)


def test_initial_move_count():
    board = Board()
    assert board.move_count == 0


def test_move_counting():
    board = Board()
    board.move_left()
    board.move_right()
    board.move_up()
    board.move_down()
    assert 4 == board.move_count


def get_positional_diff(list_a, list_b):
    get_conflicts = partial(filter, lambda x: x[0] != x[1])
    conflicts = list(get_conflicts(zip(list_a, list_b)))
    return conflicts
