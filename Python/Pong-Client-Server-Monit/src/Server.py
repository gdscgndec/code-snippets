import random

from src.Base.Math import *
from src.Base.Server import *


def action_to_vector(string_action):
    if string_action is 'u':
        action = Vector2D(-1, 0)
    elif string_action is 'd':
        action = Vector2D(1, 0)
    else:
        action = Vector2D(0, 0)  # do nothing
    return action


"""
mode 1 mean horizontal
mode 2 mean vertical
"""


class Wall:
    def __init__(self, i, j, h=1, w=1, mode=1):
        self.i = i
        self.j = j
        self.h = h
        self.w = w
        self.mode = mode
        self.body = [Vector2D(ii, jj) for ii in range(i, i + h) for jj in range(j, j + w)]

    def is_conflict(self, wall_list):
        if type(wall_list) == Wall:
            if wall_list.i >= self.i + self.h:
                return False
            if wall_list.j >= self.i + self.w:
                return False
            if wall_list.i + wall_list.h <= self.i:
                return False
            if wall_list.j + wall_list.w <= self.j:
                return False
            return True
        if type(wall_list) == list:
            for w in self.body:
                if w in wall_list:
                    return True
            return False
        if type(wall_list) == Vector2D:
            if wall_list.i >= self.i and wall_list.i < self.i + self.h:
                if wall_list.j >= self.j and wall_list.j < self.j + self.w:
                    return True
            return False

    def is_in_game(self):
        if self.i <= 0:
            return False
        if self.i + self.h >= Conf.max_i - 1:
            return False
        if self.j <= 0:
            return False
        if self.j + self.w >= Conf.max_j - 1:
            return False
        return True

    def __repr__(self):
        return '{} {} {} {}, {}'.format(self.i, self.j,
                                        self.h, self.w,
                                        self.body)


""""" # todo change to Vx and Vy to have more flexible
direction
# up right 1
# up left 2
# down right 3
# down left 4
"""""


class PongBall(Wall):

    def __init__(self, i, j, direction=1):
        super().__init__(int(i), int(j))
        self.direction = direction

    def update_next(self):
        if self.direction is 1:
            self.next_i = self.i + 1
            self.next_j = self.j + 1
        elif self.direction is 2:
            self.next_i = self.i + 1
            self.next_j = self.j - 1
        elif self.direction is 3:
            self.next_i = self.i - 1
            self.next_j = self.j + 1
        elif self.direction is 4:
            self.next_i = self.i - 1
            self.next_j = self.j - 1
        self.nextbody = [Vector2D(ii, jj) for ii in range(self.next_i, self.next_i + self.h) for jj in
                         range(self.next_j, self.next_j + self.w)]

    def update_comiit(self):
        self.i = copy.deepcopy(self.next_i)
        self.j = copy.deepcopy(self.next_j)
        self.body = copy.deepcopy(self.nextbody)

    def change_horizental(self):
        if self.direction is 1:
            self.direction = 2
        elif self.direction is 2:
            self.direction = 1
        elif self.direction is 3:
            self.direction = 4
        else:
            self.direction = 3

    def change_Vertical(self):
        if self.direction is 1:
            self.direction = 3
        elif self.direction is 2:
            self.direction = 4
        elif self.direction is 3:
            self.direction = 1
        else:
            self.direction = 2

    def is_conflict(self, wall_list):
        if type(wall_list) == Wall:
            if wall_list.i >= self.next_i + self.h:
                return False
            if wall_list.j >= self.next_i + self.w:
                return False
            if wall_list.i + wall_list.h <= self.next_i:
                return False
            if wall_list.j + wall_list.w <= self.next_j:
                return False
            return True
        if type(wall_list) == list:
            for w in self.nextbody:
                if w in wall_list:
                    return True
            return False
        if type(wall_list) == Vector2D:
            if wall_list.i >= self.next_i and wall_list.i < self.next_i + self.h:
                if wall_list.j >= self.next_j and wall_list.j < self.next_j + self.w:
                    return True
            return False


class PongAgent(Agent):
    def __init__(self):
        super().__init__()
        self.last_action = Vector2D(0, 0)
        self.head = Vector2D(0, 0)  # up of body
        self.next_head = Vector2D(0, 0)
        self.last_action_cycle = 0
        self.body = []
        self.size = Conf.pong_lean

    def update_next(self):
        logging.debug('id {} pos {} action {} to {}'.format(self.id, self.head, self.last_action, self.next_head))
        self.next_head.i = self.head.i + self.last_action.i
        self.next_head.j = self.head.j + self.last_action.j
        logging.debug('id {} pos {} action {} to {}'.format(self.id, self.head, self.last_action, self.next_head))

    def reset(self, snake_server):
        for pos in self.body:
            snake_server.world['board'][pos.i][pos.j] = 0
        self.body.clear()
        self.body = copy.deepcopy(snake_server.start_snake_body[self.id])
        self.head = copy.deepcopy(self.body[0])
        self.size = 3

        for p in self.body:
            snake_server.world['board'][p.i][p.j] = self.id

    def update_world(self, world):
        pass


class PongServer(Server):
    def __init__(self):
        print('Server __init')
        super().__init__()
        self.null_agent = PongAgent()
        self.dict_conf = {'max_i': Conf.max_i, 'max_j': Conf.max_j,
                          'team_number': Conf.agent_numbers, 'goal_id': Conf.agent_numbers + 1}
        self.world = {'board': None, 'heads': {}}
        self.start_snake_body = {1: [Vector2D(2, 2), Vector2D(3, 2), Vector2D(4, 2)],
                                 2: [Vector2D(2, Conf.max_j - 3), Vector2D(3, Conf.max_j - 3),
                                     Vector2D(4, Conf.max_j - 3)],
                                 3: [Vector2D(Conf.max_i - 5, 2), Vector2D(Conf.max_i - 4, 2),
                                     Vector2D(Conf.max_i - 3, 2)],
                                 4: [Vector2D(Conf.max_i - 5, Conf.max_j - 3), Vector2D(Conf.max_i - 4, Conf.max_j - 3),
                                     Vector2D(Conf.max_i - 3, Conf.max_j - 3)],
                                 }
        self.goal_id = 5
        self.goal_ate = False
        self.last_cycle_ate = 0
        self.ball = PongBall(Conf.max_i / 2, Conf.max_j / 2)

    def update(self):
        logging.debug('Update World')
        self.ball.update_next()

        self.goal_ate = False
        keys = list(self.agents.keys())
        agent_reseted = []
        random.shuffle(keys)
        for key in keys:
            if key in agent_reseted:
                continue
            self.agents[key].update_next()
            self.agents[key].next_head = self.normalize_pos(self.agents[key].next_head)
            logging.error(
                'agent {} go body {}'.format(self.agents[key].id, [str(x) for x in self.agents[key].body]))
            sw = False
            for wall in self.walls:
                if wall.is_conflict(self.agents[key].next_head):
                    sw = True
                elif wall.is_conflict(self.agents[key].next_head + Vector2D(self.agents[key].size, 0)):
                    sw = True

            if sw:
                if self.ball.is_conflict(self.agents[key].body):
                    self.ball.change_horizental()
                continue
            for x in self.agents[key].body:
                self.world['board'][x.i][x.j] = 0

            self.agents[key].body.clear()
            self.agents[key].head = copy.deepcopy(self.agents[key].next_head)
            for x in range(self.agents[key].size):
                self.agents[key].body.append(Vector2D(self.agents[key].next_head.i + x, self.agents[key].next_head.j))
                self.world['board'][self.agents[key].next_head.i + x][self.agents[key].next_head.j] = self.agents[
                    key].id
            logging.error(
                'agent {} go body {}'.format(self.agents[key].id, [str(x) for x in self.agents[key].body]))
            if self.ball.is_conflict(self.agents[key].body):
                self.ball.change_horizental()

            self.print_world()

        self.ball.update_next()
        for wall in self.walls:
            if self.ball.is_conflict(wall):
                if wall.mode == 1:
                    self.ball.change_Vertical()
                else:
                    self.ball.change_horizental()

                self.ball.update_next()
                for key in keys:
                    if self.ball.is_conflict(self.agents[key].body):
                        self.ball.change_horizental()
                break

        self.ball.update_next()
        for x in self.ball.body:
            self.world['board'][x.i][x.j] = 0
        self.ball.update_comiit()
        for x in self.ball.body:
            self.world['board'][x.i][x.j] = self.goal_id

        self.world['heads'].clear()
        for key in self.agents:
            self.world['heads'][self.agents[key].name] = [self.agents[key].head.i, self.agents[key].head.j]

        if self.ball.j == 1:
            self.reset_game()
            for key in keys:
                if self.agents[key].head.j <= 3:  # agent add side left add score
                    self.agents[key].score += 1

        elif self.ball.j == Conf.max_j - 1:
            self.reset_game()
            for key in keys:
                if self.agents[key].head.j >= Conf.max_j - 3:
                    self.agents[key].score += 1

        for key in keys:
            if self.agents[key].score >= Conf.max_score:
                global is_run
                is_run = False
                # todo send massage win to monitor
        self.cycle += 1

        if self.cycle % Conf.add_wall is 0:
            self.addRandomWall()

    def addRandomWall(self):
        while True:
            wall_i = random.randint(3, Conf.max_i - 3)
            wall_j = random.randint(3, Conf.max_j - 3)
            wall_size = random.choice([3, 5, 7, 9])
            wall_mode = random.choice([1, 2])
            if wall_mode == 1:
                wall = Wall(wall_i, wall_j, 1, wall_size, wall_mode)
            else:
                wall = Wall(wall_i, wall_j, wall_size, 1, wall_mode)
            wall_conflict = False
            for w in self.walls:
                if wall.is_conflict(w):
                    wall_conflict = True
                    break
            if wall_conflict:
                continue
            self.walls.append(wall)
            for w in wall.body:
                self.wall_poses.append(w)
            break
        pass

    def make_world(self):
        logging.info('make new world')
        self.world['board'] = [[0 for x in range(Conf.max_j)] for y in range(Conf.max_i)]
        self.wall_poses = []
        self.walls = []

        print(Conf.max_i, Conf.max_j)
        wallUp = Wall(1, 1, 1, Conf.max_j - 2)
        wallDown = Wall(Conf.max_i - 2, 1, 1, Conf.max_j - 2)
        self.walls.append(wallUp)
        self.walls.append(wallDown)

        self.ball = PongBall(Conf.max_i / 2, Conf.max_j / 2)

        for w in wallUp.body:
            self.wall_poses.append(w)
        for w in wallDown.body:
            self.wall_poses.append(w)

        for w in self.wall_poses:
            self.world['board'][w.i][w.j] = -1

        for key in self.agents:
            self.agents[key].reset(self)

        self.reset_game()

        self.world['heads'].clear()

        for key in self.agents:
            self.world['heads'][self.agents[key].name] = [self.agents[key].head.i, self.agents[key].head.j]
        self.print_world()

    def action_parse(self, msg):
        message = parse(msg[0])
        address = msg[1]
        if address not in self.agents:
            logging.error('message from invalid address, address: {}'.format(address))
            return False
        if message.type is not 'MessageClientAction':
            logging.error('message type is not action, client: {}'
                          .format(self.agents.get(address, Agent()).name))
            if self.agents[address].last_action_cycle < self.cycle:
                self.agents[address].last_action_cycle = self.cycle
                self.receive_action += 1
            return False

        action = action_to_vector(message.string_action)
        self.save_rcl(self.agents[address].id, message.string_message, action)
        if action is None:
            action = self.agents[address].last_action
        self.agents[address].last_action = action
        if self.agents[address].last_action_cycle < self.cycle:
            self.agents[address].last_action_cycle = self.cycle
            self.receive_action += 1
        return True

    def reset_game(self):
        try:
            if not self.goal_ate:
                self.world['board'][self.ball.i][self.ball.j] = 0
        except:
            print()
        dir = random.choice([1, 2, 3, 4])
        self.ball = PongBall(Conf.max_i / 2, Conf.max_j / 2, dir)

        for goal in self.ball.body:
            self.world['board'][goal.i][goal.j] = self.goal_id

    @staticmethod
    def normalize_pos(pos):
        if pos.i >= Conf.max_i:
            pos.i = Conf.max_i - 1
        if pos.i < 0:
            pos.i = 0
        if pos.j >= Conf.max_j:
            pos.j = Conf.max_j - 1
        if pos.j < 0:
            pos.j = 0
        return pos

    def print_world(self):
        logging.info('cycle:{}'.format(self.cycle))
        for key in self.agents:
            logging.info('score {} : {}'.format(self.agents[key].name, str(self.agents[key].score)))
        for c in self.world['board']:
            logging.info(str(c))
