class Message:
    def __init__(self):
        self.type = 'Message'
        pass

    def build(self):
        pass

    @staticmethod
    def parse(self):
        pass


class MessageClientConnectRequest(Message):
    def __init__(self, name='sample_client'):
        self.type = "ClientConnectRequest"
        self.client_name = name

    def build(self):
        msg = {"message_type": self.type, "value": {"name": self.client_name}}
        str_msg = str.encode(str(msg))
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(str(coded_msg.decode("utf-8")))
        if msg['message_type'] == "ClientConnectRequest":
            message = MessageClientConnectRequest(msg['value']['name'])
            return True, message
        return False, None


class MessageClientConnectResponse(Message):
    def __init__(self, id, ground_config):
        self.type = "MessageClientConnectResponse"
        self.id = id
        self.ground_config = ground_config

    def build(self):
        msg = {"message_type": self.type, "value": {"id": self.id, 'ground_config': self.ground_config}}
        str_msg = str.encode(str(msg))
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(str(coded_msg.decode("utf-8")))
        if msg['message_type'] == "MessageClientConnectResponse":
            message = MessageClientConnectResponse(msg['value']['id'], msg['value']['ground_config'])
            return True, message
        return False, None


class MessageClientDisconnect(Message):
    def __init__(self):
        self.type = "MessageClientDisconnect"

    def build(self):
        msg = {"message_type": self.type, "value": {}}
        str_msg = str.encode(str(msg))
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(str(coded_msg.decode("utf-8")))
        if msg['message_type'] == "MessageClientDisconnect":
            message = MessageClientDisconnect()
            return True, message
        return False, None


class MessageMonitorConnectRequest(Message):
    def __init__(self):
        self.type = "MessageMonitorConnectRequest"

    def build(self):
        msg = {"message_type": self.type, "value": {}}
        str_msg = str.encode(str(msg))
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(str(coded_msg.decode("utf-8")))
        if msg['message_type'] == "MessageMonitorConnectRequest":
            message = MessageMonitorConnectRequest()
            return True, message
        return False, None


class MessageMonitorConnectResponse(Message):
    def __init__(self, ground_config):
        self.type = "MessageMonitorConnectResponse"
        self.ground_config = ground_config

    def build(self):
        msg = {"message_type": self.type, "value": {'ground_config': self.ground_config}}
        str_msg = str.encode(str(msg))
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(str(coded_msg.decode("utf-8")))
        if msg['message_type'] == "MessageMonitorConnectResponse":
            message = MessageMonitorConnectResponse(msg['value']['ground_config'])
            return True, message
        return False, None


class MessageMonitorDisconnect(Message):
    def __init__(self):
        self.type = "MessageMonitorDisconnect"

    def build(self):
        msg = {"message_type": self.type}
        str_msg = str.encode(str(msg))
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(str(coded_msg.decode("utf-8")))
        if msg['message_type'] == "MessageMonitorDisconnect":
            message = MessageMonitorDisconnect()
            return True, message
        return False, None


class MessageClientWorld(Message):
    def __init__(self, cycle, world, score, name_id):
        self.type = "MessageClientWorld"
        self.cycle = cycle
        self.world = world
        self.score = score
        self.name_id = name_id

    def build(self):
        msg = {"message_type": self.type,
               "value": {"cycle": self.cycle, "score": self.score, "world": self.world, "name_id": self.name_id}}
        str_msg = str.encode(str(msg))
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(str(coded_msg.decode("utf-8")))
        if msg['message_type'] == "MessageClientWorld":
            cycle = msg['value']['cycle']
            world = msg['value']['world']
            score = msg['value']['score']
            name_id = msg['value']['name_id']
            message = MessageClientWorld(cycle, world, score, name_id)
            return True, message
        return False, None


class MessageClientAction(Message):
    def __init__(self, string_action='', string_message=''):
        self.type = "MessageClientAction"
        self.string_action = string_action
        self.string_message = string_message

    def build(self):
        msg = {"message_type": self.type, "value": {"action": self.string_action}}
        str_msg = str.encode(str(msg))
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(str(coded_msg.decode("utf-8")))
        if msg['message_type'] == "MessageClientAction":
            string_action = msg['value']['action']
            message = MessageClientAction(string_action=string_action, string_message=str(coded_msg.decode("utf-8")))
            return True, message
        return False, None


class MessageRCGHeader(Message):
    def __init__(self, teams, ground_config):
        self.type = "MessageRCGHeader"
        self.teams = teams
        self.ground_config = ground_config

    def build(self):
        msg = {"message_type": self.type, "value": {"teams": self.teams, "ground_config": self.ground_config}}
        str_msg = str.encode(str(msg))
        str_msg = str(msg)
        return str_msg

    @staticmethod
    def parse(coded_msg):
        # msg = eval(str(coded_msg.decode("utf-8")))
        try:
            msg = eval(coded_msg)
            if msg['message_type'] == "MessageRCGHeader":
                teams = msg['value']['teams']
                ground_config = msg['value']['ground_config']
                message = MessageRCGHeader(teams, ground_config)
                return True, message
            return False, None
        except:
            print('cant parse rcg header')
            return False, None


class MessageRCGCycle(Message):
    def __init__(self, cycle, world, score, name_id):
        self.type = "MessageRCGCycle"
        self.cycle = cycle
        self.world = world
        self.score = score
        self.name_id = name_id

    def build(self):
        msg = {"message_type": self.type,
               "value": {"cycle": self.cycle, "score": self.score, "world": self.world, "name_id": self.name_id}}
        str_msg = str(msg)
        return str_msg

    @staticmethod
    def parse(coded_msg):
        msg = eval(coded_msg)
        if msg['message_type'] == "MessageRCGCycle":
            cycle = msg['value']['cycle']
            world = msg['value']['world']
            score = msg['value']['score']
            name_id = msg['value']['name_id']
            message = MessageRCGCycle(cycle, world, score, name_id)
            return True, message
        return False, None


def parse(coded_msg):
    try:
        ret = MessageRCGHeader.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')
        pass

    try:
        ret = MessageRCGCycle.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')

    try:
        ret = MessageClientConnectRequest.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')

    try:
        ret = MessageClientConnectResponse.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')

    try:
        ret = MessageClientDisconnect.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')

    try:
        ret = MessageMonitorConnectRequest.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')

    try:
        ret = MessageMonitorConnectResponse.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')

    try:
        ret = MessageClientAction.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')

    try:
        ret = MessageClientWorld.parse(coded_msg)
        if ret[0]:
            return ret[1]
    except:
        print('big error in parse')

    return Message()
