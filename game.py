import tdl


class Game:

    FLOOR = 0
    WALL = 1
    FIREPIT = 2
    FINISH = 3

    def __init__(self):
        self.board = [self.FLOOR, self.FLOOR, self.FLOOR, self.FINISH,
                      self.FLOOR, self.WALL., self.FLOOR, self.FIREPIT,
                      self.FLOOR, self.FLOOR, self.FLOOR, self.FLOOR]
        self.position = (0, 2)
        tdl.init(80, 40, title='CodersAI Game')



def run():
    g = Game()


if __name__ == "__main__":
    run()
