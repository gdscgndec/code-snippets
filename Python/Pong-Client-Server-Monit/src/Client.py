import random
import signal
import socket
from argparse import ArgumentParser

from src.Base.Message import *
from src.Base.World import *

is_run = True


def signal_handler(sig, frame):
    global is_run
    print('You pressed Ctrl+C!')
    is_run = False


signal.signal(signal.SIGINT, signal_handler)


def run():
    # https://docs.python.org/3/howto/argparse.html
    parser = ArgumentParser()
    parser.add_argument("-n", "--name", dest="name", type=str, default='team_name' + str(random.randint(0, 10000)),
                        help="Client Name", metavar="NAME")
    parser.add_argument("-c", "--client", dest="client_type", type=str, default='random',
                        help="greedy, random, hand, best, your", metavar="ClientType")
    parser.add_argument("-p", "--port", dest="server_port", type=int, default=20002,
                        help="server port", metavar="ServerPort")
    parser.add_argument("-s", "--server", dest="server_address", type=str, default='localhost',
                        help="server address", metavar="ServerAddress")
    parser.add_argument("-ku", "--keyUp", dest="key_for_up", type=str, default='w',
                        help="Keyboard Key for up Move", metavar="KeyboardMoveChange")
    parser.add_argument("-kd", "--keyDown", dest="key_for_down", type=str, default='s',
                        help="Keyboard Key for down Move", metavar="KeyboardMoveChange")
    args = parser.parse_args()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    server_address = (args.server_address, args.server_port)

    world = World()
    message_snd = MessageClientConnectRequest(args.name).build()

    while is_run:
        sock.sendto(message_snd, server_address)
        try:
            message_rcv = sock.recvfrom(4096)
        except:
            continue
        message = parse(message_rcv[0])
        if message.type == 'MessageClientConnectResponse':
            if message.id == -1:
                print('your name is duplicated!!!')
                exit(-1)
            print('my id is ' + str(message.id))
            world.set_id(message.id, message.ground_config['goal_id'])
            break

    while is_run:
        try:
            r = sock.recvfrom(4096)
        except:
            continue
        message = parse(r[0])
        if message.type == 'MessageClientDisconnect':
            break
        elif message.type == 'MessageClientWorld':
            world.update(message)  # for auto play
            world.print()
            action = ""
            if args.client_type == 'type1':
                k = input('enter your action: w or s:')
                if k == "w":
                    action = "u"
                elif k == "s":
                    action = "d"

            elif args.client_type == 'custom':
                k = input('enter your action:')
                if k == args.key_for_up:
                    action = "u"
                elif k == args.key_for_down:
                    action = "d"
            elif args.client_type == 'auto':
                mypos = world.pongs[world.self_id].body[int(len(world.pongs[world.self_id].body) / 2)].i
                if mypos > world.goal_position.i:
                    action = "u"
                elif mypos < world.goal_position.i:
                    action = "d"
            else:  # rando mode
                action = random.choice(["d", "u"])
            sock.sendto(MessageClientAction(string_action=action).build(), server_address)
