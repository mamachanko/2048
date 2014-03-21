[![Build Status](https://travis-ci.org/mamachanko/2048.png?branch=master)](https://travis-ci.org/mamachanko/2048)
[![Coverage Status](https://coveralls.io/repos/mamachanko/2048/badge.png)](https://coveralls.io/r/mamachanko/2048)
2048
====

This is a Python game engine implementation of the rather popular game [2048](http://gabrielecirulli.github.io/2048/).

```python
>>> from p2048 import Board
>>> board = Board()
>>> print board
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 2, 2, 0]
[0, 0, 0, 0]
>>> board.move_left()
>>> print board
[0, 0, 0, 0]
[0, 0, 0, 4]
[4, 0, 0, 0]
[0, 0, 0, 0]
>>> board.move_right()
>>> print board
[0, 0, 0, 0]
[0, 2, 0, 4]
[0, 0, 0, 4]
[0, 0, 0, 0]
>>> board.move_down()
>>> print board
[0, 0, 0, 0]
[2, 0, 0, 0]
[0, 0, 0, 0]
[0, 2, 0, 8]
```

todos
-----
 * adding new elements after each moves
 * counting moves
 * raising GameOverException once no more move is possible
 * change board dimension from 4 to n
 * tag version
 * add to PyPi with version and downloads badge(http://codeinthehole.com/writing/pypi-readme-badges/)
