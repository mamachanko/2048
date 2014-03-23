[![Build Status](https://travis-ci.org/mamachanko/2048.png?branch=master)](https://travis-ci.org/mamachanko/2048)
[![Coverage Status](https://coveralls.io/repos/mamachanko/2048/badge.png)](https://coveralls.io/r/mamachanko/2048)
2048
====

This is a Python game engine implementation of the rather popular game [2048](http://gabrielecirulli.github.io/2048/).

```python
>>> from p2048 import Board
>>> board = Board()
>>> board
<Board [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0]]>
>>> def pretty_board(board):
        print '\n'.join(map(str, board.state))
>>> pretty_board(board)
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 2, 2, 0]
[0, 0, 0, 0]
>>> board.move_left()
>>> pretty_board(board)
[0, 0, 0, 0]
[0, 0, 0, 4]
[4, 0, 0, 0]
[0, 0, 0, 0]
>>> board.move_right()
>>> pretty_board(board)
[0, 0, 0, 0]
[0, 2, 0, 4]
[0, 0, 0, 4]
[0, 0, 0, 0]
>>> board.move_down()
>>> pretty_board(board)
[0, 0, 0, 0]
[2, 0, 0, 0]
[0, 0, 0, 0]
[0, 2, 0, 8]
```

Features
--------
 * adds new elements (2 or 4) after each move
 * counts moves
 * raises GameOverException once no more move is possible

Todos
-----
 * fix coverage report via travis
 * add score report
