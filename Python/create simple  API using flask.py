# Creating first API call using flask framework (API --> Application Programming Interface)
# for this first you need to install flask in your python editor by using the command pip install flask in your respective terminal

# importing the flask
from flask import Flask

web_app = Flask(__name__)

# @ --> used for defining the API route
# / --> base route
@web_app.route('/')

# below function will return the statement when server will be initialized
def myfirstAPI():
    return 'Hi everyone! I made my first API using flask'


def main():
    # run() function will initiate our server to start the flask application
    web_app.run()

if __name__ == "__main__":
    main()
