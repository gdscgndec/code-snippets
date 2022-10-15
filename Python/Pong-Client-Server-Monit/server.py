#!/usr/bin/python3

import src.Server as Game

def main():
    g = Game.PongServer()
    g.connect()
    g.run()
    g.disconnect()

if __name__ == "__main__":
    main()
