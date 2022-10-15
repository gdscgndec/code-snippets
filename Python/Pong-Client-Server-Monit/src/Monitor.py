import src.Conf.Monitor_Pong_Conf as conf
from src.Base.Math import *
from src.Base.Monitor import *


class Ground:
    def __init__(self, main, ground_config):
        self.main = main
        self.ground = Frame(main.root, height=conf.monitor_height - 110, width=conf.monitor_width, background='green4')
        self.ground.place(x=0, y=90)
        # self.ground.bind("<Motion>", self.show_mouse_position)
        self.ground_config = ground_config
        if ground_config is None:
            self.last_max_i = 0
            self.last_max_j = 0
        self.boards = {}
        for i in range(self.last_max_i):
            for j in range(self.last_max_j):
                self.boards[(i, j)] = Frame(self.ground, width=conf.monitor_width / self.last_max_j - 1,
                                            height=(conf.monitor_height - 110) / self.last_max_i - 1,
                                            bg='black')
                self.boards[(i, j)].place(x=j * conf.monitor_width / self.last_max_j,
                                          y=i * (conf.monitor_height - 110) / self.last_max_i)
                self.boards[(i, j)].bind("<Motion>",
                                         lambda event, arg=(i, j): self.show_mouse_board(event, arg))

    def show_mouse_position(self, event):
        self.main.statusbar.change_mouse_position(event.x, event.y)

    def show_mouse_board(self, event, arg):
        self.main.statusbar.change_mouse_position_ij(arg[0], arg[1])

    def show_board(self, world):
        for i in range(self.ground_config['max_i']):
            for j in range(self.ground_config['max_j']):
                if world['board'][i][j] == -1:
                    self.boards[(i, j)]['background'] = simple_color['w']
                elif world['board'][i][j] > self.ground_config['team_number']:
                    self.boards[(i, j)]['background'] = simple_color['g']
                else:
                    if world['board'][i][j] is 0:
                        self.boards[(i, j)]['background'] = simple_color[world['board'][i][j]]
                    else:
                        print(world)
                        if [i, j] in world['heads'].values():
                            self.boards[(i, j)]['background'] = advance_color[world['board'][i][j]][1]
                        else:
                            self.boards[(i, j)]['background'] = simple_color[world['board'][i][j]]

    def reset(self, ground_config):
        self.ground_config = ground_config
        for i in range(self.last_max_i):
            for j in range(self.last_max_j):
                self.boards[(i, j)].destroy()

        self.last_max_i = ground_config['max_i']
        self.last_max_j = ground_config['max_j']
        self.boards.clear()
        for i in range(self.last_max_i):
            for j in range(self.last_max_j):
                self.boards[(i, j)] = Frame(self.ground, width=conf.monitor_width / self.last_max_j - 1,
                                            height=(conf.monitor_height - 110) / self.last_max_i - 1,
                                            bg='black')
                self.boards[(i, j)].place(x=j * conf.monitor_width / self.last_max_j,
                                          y=i * (conf.monitor_height - 110) / self.last_max_i)
                self.boards[(i, j)].bind("<Motion>",
                                         lambda event, arg=(i, j): self.show_mouse_board(event, arg))
