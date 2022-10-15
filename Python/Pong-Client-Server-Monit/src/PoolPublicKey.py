import pickle

__nameFile = "Key.txt"
__key = {}


# todo check Client or Server say True or not
# todo Use hashlib

def addKey(name, key):
    with open('obj/' + __nameFile + '.pkl', 'rb') as f:
        __key = pickle.load(f)
    __key.update(name, key)
    with open('obj/' + __nameFile + '.pkl', 'wb') as f:
        pickle.dump(__key, f, pickle.HIGHEST_PROTOCOL)


def getKey(name):
    with open('obj/' + __nameFile + '.pkl', 'rb') as f:
        __key = pickle.load(f)
    return __key.get(name)
