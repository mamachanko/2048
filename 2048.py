from itertools import permutations


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


def move(row):
    without_zeroes = filter(bool, row)
    return right_pad(merge(without_zeroes))


def merge(row):
    result = []
    digit_stack = list(reversed(row))
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
