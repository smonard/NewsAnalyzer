import sys

sys.path.append('./server')

from flask import Flask
import controller.news_analyzer_controller
from controller.news_analyzer_controller import APP

if __name__ == '__main__':
    APP.run()
