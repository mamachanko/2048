import random


class Board(object):
    """
    Represents a 4x4 game board
    """

    def __init__(self):
        self.board = self._get_random_init_state()

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
        return sum(self.board, [])

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
        self.board = rotate(self.board)

    def move_left(self):
        """
        Performs the 'left' move on the board
        """
        self.board = map(move, self.board)

    def move_down(self):
        """
        Performs the 'down' move on the board
        """
        self.board = rotate(rotate(map(move, rotate(self.board))))

    def __repr__(self):
        return '\n'.join(map(lambda row: '{}'.format(row), self.board))


def move(row):
    without_zeroes = filter(bool, row)
    return right_pad(merge(without_zeroes))


def merge(row):
    result = []
    row = row[:]
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
    reversed_board = board[::-1]
    return map(list, zip(*reversed_board))
