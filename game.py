import copy
import logging
import time

import tdl

X, Y = 0, 1


def logger(level=logging.DEBUG):
    """
    A logger.
    :param level: debugging level
    :return: a logger instance.
    """
    _logger = logging.getLogger(__name__)
    _logger.setLevel(level)
    _hdlr = logging.StreamHandler()
    _fmt = logging.Formatter(
        "[%(asctime)s][%(levelname)s][%(name)s] %(message)s"
    )
    _hdlr.setFormatter(_fmt)
    _logger.addHandler(_hdlr)

    return _logger


LOG = logger(logging.DEBUG)


def human():
    user_input = tdl.event.key_wait()
    return user_input.key


class Game:

    FLOOR = 0
    WALL = 1
    FIREPIT = 2
    FINISH = 3

    def __init__(self):
        self.size = (4, 3)
        self.board = [self.FLOOR, self.FLOOR, self.FLOOR, self.FINISH,
                      self.FLOOR, self.WALL, self.FLOOR, self.FIREPIT,
                      self.FLOOR, self.FLOOR, self.FLOOR, self.FLOOR]
        self.position = [0, 2]
        self.console = tdl.init(40, 24, title='CodersAI Game')

    def get(self, x: int, y: int) -> int:
        return self.board[self._pos(x, y)]

    def set(self, x: int, y: int, value: int) -> None:
        self.board[self._pos(x, y)] = value

    def render(self) -> None:
        for y in range(0, self.size[Y]):
            for x in range(0, self.size[X]):
                field = self.get(x, y)
                # LOG.debug("(%s, %s) -> %s", x, y, field)
                if field == self.FLOOR:
                    self.console.draw_char(x, y, " ",
                                           fg=(0, 0, 0), bg=(128, 128, 128))
                elif field == self.WALL:
                    self.console.draw_char(x, y, " ",
                                           fg=(0, 0, 0), bg=(64, 64, 64))
                elif field == self.FIREPIT:
                    self.console.draw_char(x, y, "!",
                                           fg=(255, 0, 0), bg=(64, 0, 0))
                elif field == self.FINISH:
                    self.console.draw_char(x, y, "^",
                                           fg=(0, 192, 0), bg=(0, 32, 0))
        self.console.draw_char(*self.position, "@",
                               fg=(0, 0, 0), bg=(128, 128, 128))
        tdl.flush()

    def move(self, signal):

        # zwykłe przypisanie zwraca wskaźnik
        position = copy.deepcopy(self.position)
        if signal == "UP" and position[Y] > 0:
            position[Y] -= 1
        elif signal == "DOWN" and position[Y] < self.size[Y] - 1:
            position[Y] += 1
        elif signal == "LEFT" and position[X] > 0:
            position[X] -= 1
        elif signal == "RIGHT" and position[X] < self.size[X] - 1:
            position[X] += 1

        if self.get(*position) != self.WALL:
            self.position = position

    def main_loop(self, sig_function):
        while not tdl.event.is_window_closed():
            self.render()
            self.move(sig_function())

    def _pos(self, x: int, y: int) -> int:
        return x + y * self.size[X]


def run():
    g = Game()
    g.main_loop(human)


if __name__ == "__main__":
    run()
