# Pong Cup Games

## How to run game?
> cd Pong

> change Conf/conf.py to select game

> python3 server.py or ./server.py

> python3 client.py or ./client.py

> python3 client.py or ./client.py

> python3 monitor.py or ./monitor.py (if load speed of your monitor is slow, please remove "/usr/bin/ibus-daemon" why? I don't know)

## Simple Game
> change game to 'Simple' in conf.py

> change server config in ./Conf/Server_Simple_Conf.py

> run server.py

> run client.py for each client

> run monitor.py and press ctrl+c to connect

> to change algorithm in python ...

> in monitor_config
```python
monitor_height=800  # set height for monitor window
monitor_width=800   # set width for monitor window
```
#### Your client
> change YourClient.py in get_action function \
function should return one of ** u, d ** directions \
run your code with `./start.sh your (my_team)` \
**your** is type of the team (default is **auto**) \
**my_team** is team name that is optional
 
#todo
- [] add encryption to connection (Method exist)
- [] callculate time connection in vmware mode and on local network mode
- [] ui more fun
- [] more fun roll
