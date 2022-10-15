import copy
import datetime
import queue
import signal
import socket
import threading
import time

import src.Conf.Server_Pong_Conf as Conf
from src.Base.Logger import *
from src.Base.Message import *

is_run = True


def signal_handler(sig, frame):
    global is_run
    print('You pressed Ctrl+C!')
    is_run = False


signal.signal(signal.SIGINT, signal_handler)

log_file_name = datetime.datetime.now().strftime('{}-%Y-%m-%d-%H-%M-%S'.format(Conf.game_name))
rcg_logger = setup_logger('rcg_logger', log_file_name + '.rcg')
rcl_logger = setup_logger('rcl_logger', log_file_name + '.rcl')


def listener(socket, msg_size, action_queue):
    global is_run
    logging.info('Port Listener Started')
    while is_run:
        try:
            msg = socket.recvfrom(msg_size)
            action_queue.put(msg)
        except:
            continue


def monitor_listener(socket, msg_size, action_queue):
    global is_run
    logging.info('Port Listener Started')
    while is_run:
        try:
            msg = socket.recvfrom(msg_size)
            action_queue.put(msg)
        except:
            continue


class Agent:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.score = 0
        self.last_action = None
        self.address = ''
        self.pos = None
        self.next_pos = None
        self.last_action_cycle = 0


class Server:
    def __init__(self):
        print('Server __init')
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
        self.game_name = Conf.game_name
        self.agents = {}
        self.monitors = []
        self.world = []
        self.cycle = 1
        self.player_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.player_socket.settimeout(1)
        self.player_socket.bind((Conf.ip, Conf.player_port))
        self.monitor_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.monitor_socket.settimeout(1)
        self.monitor_socket.bind((Conf.ip, Conf.monitor_port))
        self.action_queue = queue.Queue(0)
        self.monitor_queue = queue.Queue(0)
        self.msg_size = 4096
        self.listener = threading.Thread(target=listener,
                                         args=(self.player_socket, self.msg_size, self.action_queue,))
        self.listener.start()
        self.monitor_listener = threading.Thread(target=monitor_listener,
                                                 args=(self.monitor_socket, self.msg_size, self.monitor_queue,))
        self.monitor_listener.start()
        self.start = False
        self.receive_action = 0

    def connect(self):
        logging.info('Wait for Agents')
        for i in range(100):
            if not is_run:
                return
            self.check_monitor_connected()
            try:
                msg_address = self.action_queue.get(block=True, timeout=1)
                message = parse(msg_address[0])
                address = msg_address[1]
            except Exception as c:
                logging.debug('Did not Receive msg:{}'.format(c))
                continue

            if not message.type == 'ClientConnectRequest':
                logging.error('message_type is not connect')
                continue

            self.add_agent(address, message)

            if len(self.agents) == Conf.agent_numbers:
                break
            time.sleep(1)

        if Conf.auto_mode:
            self.start = True
        while not self.start and is_run:
            self.check_monitor_connected()
            time.sleep(0.1)

        logging.info('{} agents connected'.format(len(self.agents)))

    def disconnect(self):
        self.send_disconnected()

    def run(self):
        global is_run
        if not is_run:
            return
        logging.info('Game Started')
        self.save_rcg_header()
        start_time = time.time()
        self.make_world()
        self.print_world()
        for s in range(Conf.max_cycle):
            if not is_run:
                return
            self.check_monitor_connected()
            self.send_world()
            self.send_visual_to_monitors()
            self.save_rcg_cycle()
            start_time_cycle = time.time()

            self.receive_action = 0
            while (Conf.sync_mode and (self.receive_action < Conf.agent_numbers)) \
                    or (not Conf.sync_mode and time.time() - start_time_cycle < Conf.think_time):
                try:
                    msg = self.action_queue.get(block=True, timeout=0.001)
                    logging.debug('Receive {}'.format(msg))
                except KeyboardInterrupt:
                    is_run = False
                    self.send_disconnected()
                    break
                except:
                    continue
                self.action_parse(msg)
                if Conf.sync_mode and (time.time() - start_time_cycle > Conf.think_time * 10):
                    break

            while self.action_queue.qsize() > 0:
                self.action_queue.get()
            logging.debug('Receive Action Finished')
            self.update()

            self.print_world()
        self.send_disconnected()
        end_time = time.time()
        logging.info('run time is {}'.format(end_time - start_time))
        is_run = False

    def update(self):
        pass

    def make_world(self):
        pass

    def add_agent(self, address, message):
        if address not in self.agents:
            duplicate_name = False
            for ag in self.agents:
                if self.agents[ag].name is message.client_name:
                    duplicate_name = True
            if duplicate_name:
                logging.error('Client {} Duplicate Name'.format(address))
                action_resp = MessageClientConnectResponse(-1, self.dict_conf).build()
            else:
                self.agents[address] = copy.deepcopy(self.null_agent)
                self.agents[address].name = message.client_name
                self.agents[address].address = address
                self.agents[address].id = len(self.agents)
                print(self.dict_conf)
                action_resp = MessageClientConnectResponse(self.agents[address].id, self.dict_conf).build()
                logging.info('agent {} connected on port number {}'
                             .format(self.agents[address].name, self.agents[address].address))
            self.player_socket.sendto(action_resp, address)
        else:
            logging.error('Client {} Want to Reconnect'.format(address))

    def check_monitor_connected(self):
        if self.monitor_queue.qsize() > 0:
            try:
                msg_address = self.monitor_queue.get(block=True, timeout=0.001)
                message = parse(msg_address[0])
                if message.type == 'MessageMonitorConnectRequest':
                    if msg_address[1] not in self.monitors:
                        self.monitors.append(msg_address[1])
                    self.player_socket.sendto(MessageMonitorConnectResponse(self.dict_conf)
                                              .build(), msg_address[1])
                    self.start = True
                elif message.type == 'MessageMonitorDisconnect':
                    if msg_address[1] in self.monitors:
                        self.monitors.remove(msg_address[1])
            except:
                return

    def action_parse(self, msg):
        pass

    def send_visual_to_monitors(self):
        score = dict([(self.agents[key].name, self.agents[key].score) for key in self.agents])
        message = MessageClientWorld(self.cycle, self.world, score,
                                     {self.agents[key].name: self.agents[key].id for key in self.agents}).build()
        for key in self.monitors:
            self.player_socket.sendto(message, key)

    def send_world(self):
        score = dict([(self.agents[key].name, self.agents[key].score) for key in self.agents])
        message = MessageClientWorld(self.cycle, self.world, score,
                                     {self.agents[key].name: self.agents[key].id for key in self.agents}).build()
        for key in self.agents:
            self.player_socket.sendto(message, key)

    def send_disconnected(self):
        message = MessageClientDisconnect().build()
        for key in self.agents:
            self.player_socket.sendto(message, key)
        for key in self.monitors:
            self.player_socket.sendto(message, key)

    def save_rcg_header(self):
        if not Conf.rcg_logger:
            return
        teams = []
        for key in self.agents:
            team = {'name': self.agents[key].name, 'id': self.agents[key].id}
            teams.append(team)
        message = MessageRCGHeader(teams, self.dict_conf).build()
        rcg_logger.info(message)

    def save_rcg_cycle(self):
        if not Conf.rcg_logger:
            return
        score = dict([(self.agents[key].name, self.agents[key].score) for key in self.agents])
        rcg_logger.info('{}'.format(MessageRCGCycle(self.cycle, self.world, score,
                                                    {self.agents[key].name: self.agents[key].id for key in
                                                     self.agents}).build()))

    def save_rcl(self, id, string_message, vector_action):
        if not Conf.rcl_logger:
            return
        rcl_logger.info('cycle:{} id:{} message:{} action:{}'.format(self.cycle, id, string_message, vector_action))

    def print_world(self):
        pass
