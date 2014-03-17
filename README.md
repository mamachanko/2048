[![Build Status](https://travis-ci.org/mamachanko/2048.png?branch=master)](https://travis-ci.org/mamachanko/2048)
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
[0, 0, 0, 0]
[4, 0, 0, 0]
[0, 0, 0, 0]
```


todos
-----
 * write README
 * add all moves
 * add new elements after each move
 * detect idempotent move
 * detect `game over`
 * change board dimension from 4 to n
