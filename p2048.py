from functools import partial
import random


def board_move(move_func):
    def wrapper(*args, **kwargs):
        board = args[0]
        board.move_count += 1
        return_value = move_func(*args, **kwargs)
        board.add_random()
        return return_value
    return wrapper


class Board(object):
    """
    Represents a 4x4 game board
    """

    def __init__(self, state=None):
        if state is None:
            self.state = self._get_random_init_state()
        else:
            self.state = state
        self.move_count = 0

    def _get_random_init_state(self):
        """
        Returns an initial board state with everything being zeroes except
        two '2's
        """
        initial_board = [0]*16
        for index in random.sample(range(16), 2):
            initial_board[index] = 2
        return self.deserialize(initial_board)

    def serialize(self):
        """
        Returns the serialized state of the board being the rows joined
        into one flat list
        """
        return sum(self.state, [])

    def deserialize(self, flat_list):
        """
        Returns a 'deserialized' board state from the given flat list
        """
        split_indices = map(lambda x: 4*x, range(4))
        return [flat_list[index:index+4] for index in split_indices]

    def rotate(self):
        """
        Rotates the board by 90 deegrees clockwise
        """
        self.state = rotate(self.state)

    @board_move
    def move_left(self):
        """
        Performs the 'left' move on the board, increments the move counter and
        adds a new random element
        """
        self._move_left()

    def _move_left(self):
        self.apply([partial(map, move)])

    @board_move
    def move_right(self):
        """
        Performs the 'right' move on the board, increments the move counter and
        adds a new random element
        """
        self._move_right()

    def _move_right(self):
        self.apply([rotate, rotate, partial(map, move), rotate, rotate])

    @board_move
    def move_down(self):
        """
        Performs the 'down' move on the board, increments the move counter and
        adds a new random element
        """
        self._move_down()

    def _move_down(self):
        self.apply([rotate, partial(map, move), rotate, rotate, rotate])

    @board_move
    def move_up(self):
        """
        Performs the 'up' move on the board, increments the move counter and
        adds a new random element
        """
        self._move_up()

    def _move_up(self):
        self.apply([rotate, rotate, rotate, partial(map, move), rotate])

    def apply(self, functions):
        """
        Applies the list of functions to the board's state in the given order
        """
        state = list(self.state)
        for function in functions:
            state = function(state)
        self.state = list(state)

    def __repr__(self):
        return '<Board {}>'.format(self.state)

    def add_random(self):
        serialized = self.serialize()
        indexed = zip(range(len(serialized)), serialized)
        zeroes = filter(lambda x: not bool(x[1]), indexed)
        index, _ = random.choice(list(zeroes))
        digit = random.choice((2, 4))
        serialized[index] = digit
        self.state = self.deserialize(serialized)




def move(row):
    without_zeroes = filter(bool, row)
    return right_pad(merge(without_zeroes))


def merge(row):
    result = []
    row = list(row)  # copy the row
    row.reverse()
    digit_stack = row
    while digit_stack:
        if len(digit_stack) == 1:
            result.append(digit_stack.pop())
            break
        a = digit_stack.pop()
        b = digit_stack.pop()
        if a == b:
            result.append(a+b)
        else:
            result.append(a)
            digit_stack.append(b)
    return result


def right_pad(input_list, size=4):
    result = input_list[:]
    extension = [0,] * (size - len(result))
    result.extend(extension)
    return result


def rotate(board):
    """
    Returns the given board rotated by 90 degrees clockwise.
    """
    board = list(board)  # copy the board
    board.reverse()
    rotated_board = map(list, zip(*board))
    return list(rotated_board)
