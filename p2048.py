import random


class Board(object):
    """
    Represents a 4x4 game board
    """

    def __init__(self, state=None):
        if state is None:
            self.state = self._get_random_init_state()
        else:
            self.state = state

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

    def move_left(self):
        """
        Performs the 'left' move on the board
        """
        self.state = map(move, self.state)

    def move_right(self):
        """
        Performs the 'right' move on the board
        """
        self.state = rotate(rotate(map(move, rotate(rotate(self.state)))))

    def move_down(self):
        """
        Performs the 'down' move on the board
        """
        self.state = rotate(rotate(rotate(map(move, rotate(self.state)))))

    def move_up(self):
        """
        Performs the 'up' move on the board
        """
        self.state = rotate(map(move, rotate(rotate(rotate(self.state)))))

    def _perform_commands(commands):
        """
        """
        state = list(self.state)
        for command in commands:
            state = command(state)
        self.state = list(self.state)

    def __repr__(self):
        return '\n'.join(map(lambda row: '{}'.format(row), self.state))


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
    return map(list, zip(*board))
